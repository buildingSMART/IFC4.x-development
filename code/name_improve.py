from nltk import PorterStemmer
from reversestem import unstem
import re
import os
import json
from copy import deepcopy
import logging
from extract_definition import MARKER


type_words_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".", "type_words.json")
)
with open(type_words_path, "r", encoding="utf-8") as file:
    data = json.load(file)
type_words = sorted(data, key=len)[::-1]

logging.basicConfig(level=logging.INFO)

ps = PorterStemmer()

ALL_CAPS = [
    "ups",
    "gprs",
    "rs",
    "am",
    "gps",
    "dc",
    "tn",
    "url",
    "ac",
    "co",
    "co2",
    "chp",
    "id",
    "led",
    "oled",
    "ole",
    "gfa",
    "tv",
    "msc",
    "ppm",
    "iot",
    "ocl",
    "lrm",
    "cgt",
    "teu",
    "tmp",
    "std",
    "gsm",
    "cdma",
    "lte",
    "td",
    "scdma",
    "wcdma",
    "sc",
    "mp",
    "bm",
    "ol",
    "ep",
    "ir",
    "www",
    "ip",
    "ph",
    "usb",
    "ii",
    "iii",
    "url",
    "uri",
    "ssl",
    "ffl",
    "ty",
    "tz",
    "tx",
    "ipi",
    "ics",
]

SMALL_CAPS = ["for", "of", "and", "to", "with", "or", "at"]

SUBSTITUTIONS = {
    "Rel ": "Relation: ",
    "Min ": "Minimum ",
    "Max ": "Maximum ",
    " Temp": " Temperature",
    "Qto_": "Quantity set: ",
    "Pset_": "Property set: ",
}


def normalise(s):
    """format the text by spliting camelCase into separate words and replacing special prefixes."""
    s = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", s)
    for k, v in SUBSTITUTIONS.items():
        if k in s:
            s = re.sub(k, v, s)
    return re.sub(MULTIPLE_SPACE_PATTERN, " ", s).strip()


def caps_control(s):
    """Turn special words to all caps or small caps using hard-coded lists.
    E.g. Usb -> USB, With -> with"""
    s1 = s.split()
    if isinstance(s1, list):
        for part in s1:
            for a in ALL_CAPS:
                if part.lower() == a:
                    s = re.sub(part, a.upper(), s)
            for b in SMALL_CAPS:
                if part.lower() == b:
                    s = re.sub(part, b.lower(), s)
    return s


def split_at_word(w, s):
    """Try spliting the string s with the word w. Return string s splited with whitespaces."""
    if w != "" and ((ps.stem(w) in s.lower()) or (w in s.lower())):
        # to_keep=False
        # for wtk in words_to_keep:
        #     if wtk in s.lower():
        #         to_keep=True
        # if not to_keep:
        if w in s.lower():
            s = re.sub(w, " " + w + " ", s.lower())
        else:
            vs = unstem(ps.stem(w))
            if isinstance(vs, dict):
                # turn dict to flat list
                vsl = []
                for key, val in vs.items():
                    vsl.append(key)
                    if val:
                        for v in val:
                            vsl.append(v)
                vs = vsl
            if vs:
                vs.append(ps.stem(w))
                vs = sorted(vs, key=len)[::-1]
                for v in vs:
                    if v in s.lower():
                        s = re.sub(w, " " + w + " ", s.lower())
                        break
    if isinstance(s, list):
        s = " ".join(s)
    return s


MULTIPLE_LINEBREAK_PATTERN = re.compile("\n+")
MULTIPLE_SPACE_PATTERN = re.compile(r"\s+")
HTML_TAG_PATTERN = re.compile("<.*?>")
CURLY_BRACKET_PATTERN = re.compile(
    "{.*?}.*"
)  # also removes all text after curly brackets
FIGURE_PATTERN = re.compile(
    "[^.,;]*(Figure|the figure)[^.,;]*"
)  # removes the sentence when it mentiones a Figure.
LIST_PATTERN = re.compile(
    r"[^.,;]*:\s?"
)  # removes the last sentence when it ends with a colon.
# CHANGE_LOG_PATTERN = re.compile(r'\{\s*\.change\-\w+\s*\}.+', flags=re.DOTALL)


replacements = [
    (re.compile(r"\*{2}"), " "),
    (re.compile(r":(?!\s)"), ": "),
    (re.compile(r"SELF\\"), ""),
    (
        re.compile(r"(?<!\.)\.\.(?!\.)"),
        ".",
    ),  # remove double dots but not triple (ellipsis)
    (MULTIPLE_LINEBREAK_PATTERN, "; "),
    (HTML_TAG_PATTERN, " "),
    (CURLY_BRACKET_PATTERN, " "),
    (FIGURE_PATTERN, ""),
    (LIST_PATTERN, ""),
    (MULTIPLE_SPACE_PATTERN, " "),
]


def remove_unwanted(s):
    for pat, subs in replacements:
        s = re.sub(pat, subs, s)
    return s


def clean(s):
    """format the text by removing unwanted characters."""
    # remove all redundant characters (except those listed):
    s = re.sub(MULTIPLE_LINEBREAK_PATTERN, "; ", s)
    s = remove_unwanted(s)
    cleaned = "".join(
        ["", c][c.isalnum() or c in ":.,()-+ —=;α°_/!?$%@<>'\"\\*"] for c in s
    )
    p = re.compile('"')
    cleaned = re.sub(p, "'", cleaned).strip()
    return re.sub(MULTIPLE_SPACE_PATTERN, " ", cleaned).strip()


def split_words(s):
    """Split the phrase using the hard-coded list of words found in enumerations
    to split the ALLCAPS phrases into individual words."""
    found_words = []
    for w in type_words:
        # skip if word is contained in previous words (e.g. EXCHANGE in EXCHANGER)
        previously_found = False
        for fw in found_words:
            if w in fw:
                previously_found = True
        if not previously_found:
            s2 = deepcopy(s)
            s2 = split_at_word(w, s2)
            if s2 != s:
                found_words.append(w)
                s = s2
    s = re.sub("_", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def name_improve(s):
    s = re.split(r"_\w\[", s)[0]
    if s.lower().startswith("ifc"):
        s = s[3:]
    return caps_control(split_words(clean(normalise(s))).title())


def definition_improve(s):
    return clean(s.split(MARKER.strip(), 1)[0].strip())
