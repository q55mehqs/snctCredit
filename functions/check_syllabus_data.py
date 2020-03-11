from json import loads, dumps
from os import path
import unicodedata

def left(digit: int, msg: str) -> str:
    for c in msg:
        if unicodedata.east_asian_width(c) in ('F', 'W', 'A'):
            digit -= 2
        else:
            digit -= 1
    return msg + ' ' * digit


raw = {}
with open(path.join(path.dirname(__file__) ,"../jugyoListCredit_17s-.json"), "r", encoding="utf-8") as f:
    raw = loads(f.read())

checklist = [
    "1-1", # "1-2", "1-3", # 1年は同じなので省略
    "IS2", "IT2", "IE2",
    "IS3", "IT3", "IE3",
    "IS4", "IT4", "IE4",
    "IS5", "IT5", "IE5"
]

for c in checklist:
    print(c)
    for subj, v in raw[c].items():
        ippan = "専門" if v["専門"] else "一般"
        hisshu = "必修" if v["必修"] else "選択"
        gakushu_circle = "○   " if v["学修"] else "    "
        print("%s||%s|%s|%s|%d" % (ippan, hisshu, left(40, subj), gakushu_circle, v["単位数"]))
        input()
