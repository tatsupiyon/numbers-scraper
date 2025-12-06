from bs4 import BeautifulSoup
import requests
import pandas as pd
import glob
import re

# データ格納用リスト
d_list = []

# HTMLが入っているフォルダ（GitHubでは sample_html ）
files = glob.glob(r"./sample_html/*")

# 全てのHTMLを読み込む
for file in files:
    with open(file, "r", encoding="utf-8-sig") as f:
        html = f.read()

    soup = BeautifulSoup(html, "lxml")
    title = soup.select_one("title").text
    print(f"\n=== {title} ===")

    # Bパターン：titleに "ナンバーズ" を含む
    if "ナンバーズ" in title:
        print("→ Bパターンで解析")
        tr_lists = soup.select("tr")

        for tr_list in tr_lists:
            try:
                times = tr_list.select_one("th").text
                date = tr_list.select_one("td:nth-of-type(1)").text
                number = tr_list.select_one("td:nth-of-type(2)").text
            except:
                continue

            d_list.append({"times": times, "date": date, "number": number})

    # Aパターン
    else:
        print("→ Aパターンで解析")
        table_lists = soup.select("table")

        for table_list in table_lists:
            try:
                times = table_list.select_one("tbody > tr > th:nth-of-type(2)").text
                date = table_list.select_one("tbody > tr:nth-of-type(2) > td").text
                number = table_list.select_one("tbody > tr:nth-of-type(3) > td").text
            except:
                continue

            d_list.append({"times": times, "date": date, "number": number})

# DataFrame化
df = pd.DataFrame(d_list)

# 回数の数字だけ抽出 → 数値に変換
df["times"] = df["times"].str.extract(r"(\d+)").astype("Int64")
df = df.dropna(subset=["times"])
df = df.sort_values("times")

print("\n=== 出力データ ===")
print(df)

# CSV保存
df.to_csv("numbers.csv", index=False, encoding="utf-8-sig")

# 欠番チェック
def find_missing_numbers_fast(nums):
    nums_set = set(nums)
    return [i for i in range(min(nums), max(nums) + 1) if i not in nums_set]

print("\n=== 欠番一覧 ===")
print(find_missing_numbers_fast(df["times"]))