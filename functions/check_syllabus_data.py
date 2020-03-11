from json import loads, dumps

raw = {}
with open("../jugyoListCredit_reload.json", "r", encoding="utf-8") as f:
    raw = loads(f.read())

checklist = ["IS4", "IT4", "IE4", "IS5", "IT5", "IE5"]

for c in checklist:
    print(c)
    for subj, v in raw[c].items():
        ippan = "専門" if v["専門"] else "一般"
        hisshu = "必修" if v["必修"] else "選択"
        gakushu_circle = "○\t" if v["学修"] else "\t"
        print("%s||%s|%20s|%s|%d" % (ippan, hisshu, subj, gakushu_circle, v["単位数"]))
        input()