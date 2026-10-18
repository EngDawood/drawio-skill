"""Repair common draw.io XML slips in place: python3 repair_xml.py <file>"""
import re, sys

p = sys.argv[1]
x = open(p, encoding="utf-8").read()
m = re.search(r"<mxfile[\s\S]*?</mxfile>|<mxGraphModel[\s\S]*?</mxGraphModel>", x)
if m:
    x = m.group(0)


def fix(m):
    v = m.group(1).replace("<", "&lt;")
    v = re.sub(r"&(?!(?:amp|lt|gt|quot|apos|#[0-9]+|#x[0-9a-fA-F]+);)", "&amp;", v)
    return '="' + v + '"'


x = re.sub(r'="([^"]*)"', fix, x)
x = re.sub(r'<mxCell id="([^"]+)" parent="\1"\s*/>', r'<mxCell id="\1" parent="0"/>', x)
open(p, "w", encoding="utf-8").write(x)
