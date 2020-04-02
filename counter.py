from json import loads
from os import chdir, path

chdir(path.dirname(__file__))

rd = {}
with open("jugyoListCredit_17s-.json", "r", encoding="utf-8") as f:
    rd = loads(f.read())

i = 0
for clsdata in rd.values():
    for _ in clsdata:
        i+=1

print(i)