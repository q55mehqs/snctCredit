#!/usr/bin/env python
# coding: utf-8

import bs4
import json
from datetime import date
from os import chdir, path
from enum import Enum, auto

chdir(path.dirname(__file__))

class Course(Enum):
    IS = auto()
    IT = auto()
    IE = auto()
    IN = auto()
    F1 = auto()
    F2 = auto()
    F3 = auto()

    def text(self) -> str:
        if self is self.IS:
            return "情報システム"
        elif self is self.IT:
            return "情報通信"
        elif self is self.IE:
            return "知能エレクトロニクス"


# In[71]: 
today = date.today()
year = 0
if today.month < 4:
    year = today.year - 2001
else:
    year = today.year - 2000

def out_dict(file_name: str, grade: int, course: Course) -> dict:
    with open(file_name, "r", newline="", encoding="utf-8") as f:
        soups = bs4.BeautifulSoup(f.read(), "html.parser")

    soup = soups.select("#sytablenc > tbody > tr")
    grade_data = [{},{},{},{},{}]
    for i, s in enumerate(soup[3:-3]):
        l = s.find_all("td")
        data = {
            l[2].a.text: {
                "ID": "%d%s%d%s" % (year, course.name, grade, str(i+1).zfill(4)),
                "専門": "%s" % l[0].text == "専門",
                "必修": l[1].text == "必修",
                "学修": l[4].text == "学修単位",
                "単位数": int(l[5].text),
                "シラバスURL": l[2].a.get("href"),
                "先生": l[16].text.strip().split(",")
            }
        }

        if s.get("data-course-value") == course.text() or not s.get("data-course-value"):
            if l[6].text.strip() or l[7].text.strip():
                grade_data[0].update(data)
            elif l[8].text.strip() or l[9].text.strip():
                grade_data[1].update(data)
            elif l[10].text.strip() or l[11].text.strip():
                grade_data[2].update(data)
            elif l[12].text.strip() or l[13].text.strip():
                grade_data[3].update(data)
            elif l[14].text.strip() or l[15].text.strip():
                grade_data[4].update(data)

    return grade_data[grade-1]

#%%

exp_value = {}

exp_value.update({"1-1": out_dict("syllabus.html", 1, Course.F1)})
exp_value.update({"1-2": out_dict("syllabus.html", 1, Course.F2)})
exp_value.update({"1-3": out_dict("syllabus.html", 1, Course.F3)})
exp_value.update({"IS2": out_dict("syllabus.html", 2, Course.IS)})
exp_value.update({"IT2": out_dict("syllabus.html", 2, Course.IT)})
exp_value.update({"IE2": out_dict("syllabus.html", 2, Course.IE)})
exp_value.update({"IS3": out_dict("syllabus.html", 3, Course.IS)})
exp_value.update({"IT3": out_dict("syllabus.html", 3, Course.IT)})
exp_value.update({"IE3": out_dict("syllabus.html", 3, Course.IE)})
exp_value.update({"IS4": out_dict("syllabus.html", 4, Course.IS)})
exp_value.update({"IT4": out_dict("syllabus.html", 4, Course.IT)})
exp_value.update({"IE4": out_dict("syllabus.html", 4, Course.IE)})


#%%
print(exp_value)

#%%
with open("jugyoList.json", "w", encoding="utf-8", newline="") as f:
    f.write(json.dumps(exp_value, indent=2, ensure_ascii=False))