from json import loads, dumps

old_path = "jugyoListCredit"

old = {}
with open(old_path + ".json", "r", encoding="utf-8") as f:
    old = loads(f.read())

new = {}
for c, cv in old.items():
    new[c] = {}
    for k, v in cv.items():
        try:
            isSenmon = False
            if v["科目種別"] == "一般":
                pass
            elif v["科目種別"] == "専門":
                isSenmon = True
            else:
                raise Exception("%s/%s 一般/専門じゃない" % (c, k))

            isGakushu = False
            if v["履修"] == True:
                pass
            elif v["履修"] == False:
                isGakushu = True
            else:
                raise Exception("%s/%s 履修/学修じゃない" % (c, k))

            item = {
                "ID": v["ID"],
                "専門": isSenmon,
                "必修": v["必修"],
                "学修": isGakushu,
                "単位数": v["単位数"]
            }
        except KeyError:
            raise Exception("%s/%s キー不足" % (c, k))
        new[c].update({k: item})

print(new)

with open(old_path + "_reload.json", "w", encoding="utf-8") as wf:
    wf.write(dumps(new, ensure_ascii=False, indent=2))
#     pass