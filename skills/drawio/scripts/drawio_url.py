"""Print an app.diagrams.net URL that opens a diagram: python3 drawio_url.py <file>"""
import sys, zlib, base64, urllib.parse

xml = open(sys.argv[1], encoding="utf-8").read()
raw = urllib.parse.quote(xml, safe="~()*!.'").encode()
c = zlib.compressobj(9, zlib.DEFLATED, -15)
b64 = base64.b64encode(c.compress(raw) + c.flush()).decode()
print("https://app.diagrams.net/?grid=0&pv=0&border=10&edit=_blank#R" + urllib.parse.quote(b64, safe=""))
