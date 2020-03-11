# 仙台高専広瀬キャンパス単位

## 概要

仙台高専の単位リストがJSONで書いてます

## ファイル詳細

### jugyoListCredit_17s-.json

総合工学科の単位に合わせて4、5年を手打ちで書き換えたもの

### functions/jugyoList.json

シラバスからそのままデータをエクスポートしたもの

書き換えを行わず、基本的に jugyoListCredit_17s- を変更していく

## データ内容

- クラス名
  - 教科名
    - ID 深い意味はない
    - 専門 一般科目なら`false`、専門科目なら`true`
    - 必修 必修科目なら`true`、選択科目なら`false`
    - 学修 履修科目なら`false`、学修科目なら`true`
    - 単位数

## チェック用関数 (Python)

```bash
# for bash (Linux, macOS)
python3 functions/check_syllabus_data.py

# for Windows CMD/PowerShell
python functions/check_syllabus_data.py
```

を実行すると学生便覧 (or PDFで公開されている学修単位記載ファイル) の表示に近い形でデータの確認ができます

Pythonが利用できる環境の方はぜひご利用いただき、ミス/抜けチェックをしていただければ幸いです

33行目の`input()`の位置を替える、削除すると表示を変える事ができます
