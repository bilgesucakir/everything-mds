#!/usr/bin/env python3
"""Pull chosen domains/parts out of everything-mds into one markdown file (or a zip).

Standard library only. Run from anywhere:
  python3 extractor/extract.py list
  python3 extractor/extract.py get --domain general,web -o rules.md
  python3 extractor/extract.py get --domain general,web --part working-agreements,conventions --zip -o rules.zip
  python3 extractor/extract.py build-page      # regenerates extractor/index.html
  python3 extractor/extract.py check           # every file tagged, tags known

Tags: each .md has front matter (domain, part, summary, adapt). A line
`<!-- tags: domain=ios; part=templates -->` right under a heading overrides
the file's tags for that section (until the next ## heading).
A section is kept when its domain matches ANY chosen domain AND its part
matches ANY chosen part (an omitted filter means "all").
"""
import argparse, json, pathlib, re, sys, zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOMAINS = {"general": "working rules for any project", "web": "websites and web apps",
           "ios": "iPhone apps and the App Store", "backend": "APIs and servers",
           "ops": "hosting, domains, monitoring, costs", "design": "assets, fonts, visual design"}
PARTS = {"working-agreements": "how the assistant should behave", "conventions": "how work is organised",
         "stack-rules": "rules tied to a specific tool or host", "checklists": "tick-box reviews",
         "templates": "fill-in documents", "playbooks": "ordered steps", "reference": "facts, specs, case studies"}

def split_list(v): return [x.strip() for x in v.split(",") if x.strip()]

def parse_tags(s):
    d = {}
    for pair in s.split(";"):
        if "=" in pair:
            k, v = pair.split("=", 1); d[k.strip()] = split_list(v)
    return d

def load():
    """Return list of files: {path, title, meta, sections:[{heading, domains, parts, text}]}"""
    files = []
    for p in sorted(ROOT.glob("*/*.md")):
        txt = p.read_text(encoding="utf-8")
        meta = {}
        m = re.match(r"---\n(.*?)\n---\n+", txt, re.S)
        if m:
            for ln in m.group(1).split("\n"):
                if ":" in ln:
                    k, v = ln.split(":", 1); meta[k.strip()] = v.strip()
            txt = txt[m.end():]
        fd, fp = split_list(meta.get("domain", "")), split_list(meta.get("part", ""))
        title = (re.match(r"# (.*)", txt) or [None, p.stem])[1]
        sections, cur = [], {"heading": "", "domains": fd, "parts": fp, "lines": []}
        for ln in txt.split("\n"):
            if re.match(r"## ", ln):
                sections.append(cur)
                cur = {"heading": ln[3:].strip(), "domains": fd, "parts": fp, "lines": []}
            t = re.match(r"<!-- tags: (.*?) -->", ln)
            if t:
                o = parse_tags(t.group(1))
                cur["domains"] = o.get("domain", cur["domains"]); cur["parts"] = o.get("part", cur["parts"])
                continue
            cur["lines"].append(ln)
        sections.append(cur)
        for s in sections: s["text"] = "\n".join(s.pop("lines")).strip("\n")
        files.append({"path": p.relative_to(ROOT).as_posix(), "title": title, "meta": meta, "sections": sections})
    return files

def select(files, domains, parts):
    out = []
    for f in files:
        secs = [s for s in f["sections"] if s["text"].strip() and
                (not domains or set(domains) & set(s["domains"])) and (not parts or set(parts) & set(s["parts"]))]
        if secs: out.append((f, secs))
    return out

def render_file(f, secs):
    body = "\n\n".join(s["text"] for s in secs)
    note = f.get("meta", {}).get("adapt", "")
    return f"<!-- from everything-mds: {f['path']}" + (f" | adapt: {note}" if note else "") + f" -->\n{body}\n"

def cmd_list(a):
    files = load()
    print("Domains:", *[f"\n  {k:<8} {v}" for k, v in DOMAINS.items()])
    print("Parts:", *[f"\n  {k:<19} {v}" for k, v in PARTS.items()])
    print("\nFiles and sections:")
    for f in files:
        print(f"\n{f['path']}  [{', '.join(split_list(f['meta'].get('domain','')))} | {f['meta'].get('part','')}]\n  {f['meta'].get('summary','')}")
        for s in f["sections"]:
            if s["heading"] and (s["domains"], s["parts"]) != (split_list(f['meta'].get('domain','')), split_list(f['meta'].get('part',''))):
                print(f"    - {s['heading']}  [{', '.join(s['domains'])} | {', '.join(s['parts'])}]")

def cmd_get(a):
    d, p = split_list(a.domain or ""), split_list(a.part or "")
    for x in d:
        if x not in DOMAINS: sys.exit(f"unknown domain {x!r}; run `list`")
    for x in p:
        if x not in PARTS: sys.exit(f"unknown part {x!r}; run `list`")
    skip = set(split_list(a.exclude or ""))
    sel = [(f, s) for f, s in select(load(), d, p) if f["path"] not in skip]
    if not sel: sys.exit("nothing matched")
    head = (f"<!-- Extracted from everything-mds. domains: {', '.join(d) or 'all'}; parts: {', '.join(p) or 'all'}.\n"
            f"     Adapt names/paths to this project; delete what does not apply. -->\n")
    out = pathlib.Path(a.output or ("everything-mds-extract.zip" if a.zip else "everything-mds-extract.md"))
    if a.zip:
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for f, s in sel: z.writestr(f["path"], f"# {f['title']}\n\n" + render_file(f, s))
    else:
        out.write_text(head + "\n" + "\n---\n\n".join(f"# {f['title']}\n\n" + render_file(f, s) for f, s in sel), encoding="utf-8")
    print(f"wrote {out} ({len(sel)} files, {sum(len(s) for _, s in sel)} sections)")

def cmd_check(a):
    bad = 0
    for f in load():
        m = f["meta"]
        for s in f["sections"]:
            for x in s["domains"]:
                if x not in DOMAINS: print(f"{f['path']}: unknown domain {x}"); bad += 1
            for x in s["parts"]:
                if x not in PARTS: print(f"{f['path']}: unknown part {x}"); bad += 1
        if not m.get("domain") or not m.get("part") or not m.get("summary"):
            print(f"{f['path']}: missing domain/part/summary"); bad += 1
    print("ok" if not bad else f"{bad} problem(s)"); sys.exit(bool(bad))

PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>everything-mds extractor</title><style>
:root{color-scheme:light dark;font-family:system-ui,sans-serif}body{max-width:46rem;margin:0 auto;padding:1rem 16px 3rem;line-height:1.5}
fieldset{margin:1rem 0;border:1px solid #8885;border-radius:8px}label{display:block;margin:.2rem 0}small{opacity:.7}
button{font:inherit;padding:.5rem 1rem;margin-right:.5rem}pre{white-space:pre-wrap;max-height:22rem;overflow:auto;border:1px solid #8885;padding:.6rem;border-radius:8px}</style></head><body>
<h1>everything-mds extractor</h1><p>Pick domains and parts, then download one markdown file. Nothing leaves your browser.</p>
<fieldset><legend>Domains (any of)</legend><div id="d"></div></fieldset>
<fieldset><legend>Parts (any of; none ticked = all)</legend><div id="p"></div></fieldset>
<button id="dl">Download .md</button><button id="cp">Copy</button><span id="n"></span><pre id="pv"></pre>
<script>const DATA=__DATA__;const $=i=>document.getElementById(i);
for(const [k,v] of Object.entries(DATA.domains))$("d").insertAdjacentHTML("beforeend",`<label><input type=checkbox value="${k}" ${k=="general"?"checked":""}> <b>${k}</b> <small>${v}</small></label>`);
for(const [k,v] of Object.entries(DATA.parts))$("p").insertAdjacentHTML("beforeend",`<label><input type=checkbox value="${k}"> <b>${k}</b> <small>${v}</small></label>`);
const ticked=id=>[...$(id).querySelectorAll("input:checked")].map(x=>x.value);
function build(){const d=ticked("d"),p=ticked("p");let nf=0,out=`<!-- Extracted from everything-mds. domains: ${d.join(", ")||"all"}; parts: ${p.join(", ")||"all"}. Adapt names/paths; delete what does not apply. -->\\n`;
const parts=[];for(const f of DATA.files){const s=f.sections.filter(s=>(!d.length||s.domains.some(x=>d.includes(x)))&&(!p.length||s.parts.some(x=>p.includes(x))));
if(s.length){nf++;parts.push(`# ${f.title}\\n\\n<!-- from everything-mds: ${f.path}${f.adapt?" | adapt: "+f.adapt:""} -->\\n`+s.map(x=>x.text).join("\\n\\n")+"\\n")}}
$("n").textContent=nf+" files";return out+"\\n"+parts.join("\\n---\\n\\n")}
function show(){$("pv").textContent=build()}document.querySelectorAll("input").forEach(i=>i.onchange=show);show();
$("dl").onclick=()=>{const a=document.createElement("a");a.href=URL.createObjectURL(new Blob([build()],{type:"text/markdown"}));a.download="everything-mds-extract.md";a.click()};
$("cp").onclick=()=>navigator.clipboard.writeText(build());</script></body></html>"""

def cmd_build_page(a):
    data = {"domains": DOMAINS, "parts": PARTS, "files": [
        {"path": f["path"], "title": f["title"], "adapt": f["meta"].get("adapt", ""),
         "sections": [s for s in f["sections"] if s["text"].strip()]} for f in load()]}
    out = ROOT / "extractor" / "index.html"
    out.write_text(PAGE.replace("__DATA__", json.dumps(data).replace("</", "<\\/")), encoding="utf-8")
    print("wrote", out.relative_to(ROOT))

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
sub = ap.add_subparsers(dest="cmd", required=True)
sub.add_parser("list").set_defaults(fn=cmd_list)
g = sub.add_parser("get"); g.set_defaults(fn=cmd_get)
g.add_argument("--domain"); g.add_argument("--part"); g.add_argument("--exclude", help="comma-separated file paths to leave out")
g.add_argument("--zip", action="store_true"); g.add_argument("-o", "--output")
sub.add_parser("build-page").set_defaults(fn=cmd_build_page)
sub.add_parser("check").set_defaults(fn=cmd_check)
a = ap.parse_args(); a.fn(a)
