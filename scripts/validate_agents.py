#!/usr/bin/env python3
"""Check every .claude/agents/*.md: frontmatter parses, required fields exist, names match files."""
import glob, os, re, sys
try:
    import yaml
except ImportError:
    sys.exit("pyyaml is required: pip install pyyaml")

MODELS = {"sonnet", "opus", "haiku", "fable", "inherit"}
errors, descriptions = [], {}
for path in sorted(glob.glob(".claude/agents/*.md")):
    stem = os.path.splitext(os.path.basename(path))[0]
    text = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not m:
        errors.append(f"{path}: no frontmatter"); continue
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        errors.append(f"{path}: invalid YAML ({e})"); continue
    for key in ("name", "description", "tools", "model", "maxTurns"):
        if key not in fm:
            errors.append(f"{path}: missing {key}")
    if fm.get("name") != stem:
        errors.append(f"{path}: name {fm.get('name')!r} does not match file name")
    if fm.get("model") not in MODELS:
        errors.append(f"{path}: unknown model {fm.get('model')!r}")
    if not isinstance(fm.get("maxTurns"), int):
        errors.append(f"{path}: maxTurns must be an integer")
    if len(str(fm.get("description", ""))) > 200:
        errors.append(f"{path}: description over 200 characters")
    if "docs/status" not in m.group(2):
        errors.append(f"{path}: body never mentions docs/status")
    descriptions[stem] = str(fm.get("description", ""))
if len(descriptions) != 7:
    errors.append(f"expected 7 agents, found {len(descriptions)}")
if errors:
    print("\n".join(errors)); sys.exit(1)
print(f"{len(descriptions)} agents valid")
