import os
import sys
import time
import itertools

import lark

from github import Github

if not os.environ.get("USER_AUTH"):
    print("No Github credentials. Probably a PR?")
    exit(0)

g = Github(os.environ["USER_AUTH"])
r = g.get_repo("buildingSMART/IFC4.3.x-output")

def alnum(s):
    return "".join(c for c in s if c.isalnum())

class issue:  
    def __init__(self, *args):
        self.len = self.format.count("%s")
        assert(len(args) == (self.len + 1) or len(args) == 0)
        
        self.data = (type(self).__name__,) + tuple(map(alnum, args[:-1]))
        self.body = args[-1] if len(args) else None
        
        parts = self.format.split("%s")
        parts = [p.strip() for p in parts]
        parts = list(itertools.chain(*zip(parts, ["ref"] * len(parts))))[:-1]
        parts = [p for p in parts if p]
        parts = [(x if x == "ref" else ('"%s"' % x)) for x in parts]
        
        self.grammar = lark.Lark('start: %s\nref: /[A-Za-z0-9_]+/\n%%ignore " "\n' % " ".join(parts))
        
    def __hash__(self):
        return hash(self.data)
        
    def __eq__(self, other):
        return self.data == other.data
        
    def construct(self, sleep=1.0):
        print("Creating issue:")
        print(self.format % self.data[1:])
        print("="*len(self.format % self.data[1:]))
        print(self.body)
        return r.create_issue(self.format % self.data[1:], body=self.body)
    
    def parse(self, issue):
        self.data = (type(self).__name__,) + tuple(map(lambda t: str(t.children[0]), self.grammar.parse(issue.title).children))
        self.body = issue.body
        
    def __repr__(self):
        return "issue(%s)" % repr(self.format % tuple("<%s>" % s for s in self.data[1:]))
        

class missing_documentation_for_attribute(issue):
    format = "Entity %s has no documentation for attribute %s"

class missing_documentation_for_entity(issue):
    format = "Entity %s has no documentation"
    
issue_templates = [missing_documentation_for_entity, missing_documentation_for_attribute]

def parse_issue(i):
    exceptions = []
    for t in issue_templates:
        try:
            x = t()
            x.parse(i)
            return x
        except lark.exceptions.LarkError as e:
            exceptions.append(str(e))
    print("Unable to parse issue")
    for e in exceptions: print(e)


issues = list(r.get_issues(state='all'))
parsed_issues = map(parse_issue, issues)
parsable_issues = filter(lambda ab: ab[0] is not None, zip(parsed_issues, issues))
issue_mapping = dict(parsable_issues)

from generators.util.xmi_document import xmi_document

try:
    fn = sys.argv[1]
except:
    print("Usage: python sanity_checker.py <schema.xml>", file=sys.stderr)
    exit()

def generate_issues():
    xmi_doc = xmi_document(fn)

    for item in xmi_doc:
        
        if item.type == "ENTITY":
        
            print("checking", item.name, flush=True)
            
            md = item.markdown_definition_html
            if not md:
                yield missing_documentation_for_entity(item.name, str(md))
                
            for child in item.children:
                
                md = child.markdown_definition_html
                if not md:
                    yield missing_documentation_for_attribute(item.name, child.name, str(md))
            
discovered_issues = set(generate_issues())

issue_changes = []

for old_issue, gh_handle in issue_mapping.items():
    open_on_gh = gh_handle.state == 'open'
    issue_exists = old_issue in discovered_issues
    if open_on_gh != issue_exists:        
        issue_changes.append((gh_handle, ('open' if issue_exists else 'closed')))

new_issues = list(discovered_issues - issue_mapping.keys())
n_issue_changes = len(new_issues) + len(issue_changes)

print("New issues", len(new_issues))
print("Changed issues", len(issue_changes))
print("Changing", n_issue_changes, "issues")

if n_issue_changes == 0:
    print("No changes in issue state, exiting")
    exit(0)

total_runtime = 20 * 60
# clamp sleep time to max 20 secs
sleep_time = min(20, total_runtime / n_issue_changes)

def pause():
    # If you're making a large number of POST, PATCH,
    # PUT, or DELETE requestsfor a single user or client
    # ID, wait at least one second between each request.
    # https://docs.github.com/en/free-pro-team@latest/rest/guides/best-practices-for-integrators
    
    # Requests that create content which triggers notifications,
    # such as issues, comments and pull requests, may be further
    # limited and will not include a Retry-After header in the
    # response. Please create this content at a reasonable pace
    # to avoid further limiting.
    # https://docs.github.com/en/free-pro-team@latest/rest/guides/best-practices-for-integrators
    
    # We wait for the max amount of time to have the issues created in 20mins.
    time.sleep(sleep_time)
    
for gh_handle, state in issue_changes:
    print("Changing", gh_handle, "->", state, flush=True)
    gh_handle.edit(state=state)
    pause()
    
for new_issue in new_issues:
    new_issue.construct()
    pause()
