import logging
from collections import defaultdict
from datetime import date

POT_HEADER = """# Industry Foundation Classes IFC.
# Copyright (C) {year} buildingSMART
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\\n"
"Report-Msgid-Bugs-To: bsdd_support@buildingsmart.org\\n"
"POT-Creation-Date: {date} {time}\\n"
"X-Crowdin-SourceKey: msgstr\\n"
"Language-Team: buildingSMART community\\n"
"""


def dedupe_translations(to_translate):
    kept, deduped = {}, []
    for t in to_translate:
        if not (t["msgid"] and t["msgstr"]):
            continue
        if t["msgid"] not in kept:
            kept[t["msgid"]] = t["msgstr"]
            deduped.append(t)
        elif kept[t["msgid"]] != t["msgstr"]:
            logging.warning("msgid %s: conflicting msgstr dropped", t["msgid"])
    return deduped


def write_pot_files(to_translate, output_dir):
    pot_dir = output_dir / "pot"
    pot_dir.mkdir(parents=True, exist_ok=True)
    by_package = defaultdict(list)
    for t in dedupe_translations(to_translate):
        by_package[t["package"] or "UNSPECIFIED_PACKAGE"].append((t["msgid"], t["msgstr"]))
    now = date.today()
    header = POT_HEADER.format(year=now.strftime("%Y"), date=now.strftime(r"%Y-%m-%d"), time=now.strftime("%H:%M"))
    total = 0
    for package, messages in by_package.items():
        lines = [header]
        for msgid, msgstr in messages:
            lines.append('msgid "%s"\nmsgstr "%s"\n' % (msgid, msgstr))
        (pot_dir / (package + ".pot")).write_text("\n".join(lines), encoding="utf-8")
        total += len(messages)
    print("-- Saved %s terms in %s POT files. --" % (total, len(by_package)))
