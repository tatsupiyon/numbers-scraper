🎰 Numbers（ナンバーズ）スクレイピング

ナンバーズ当選結果を自動で収集し、CSV で保存する Python スクレイピングツール です。
Selenium を利用してバックナンバー一覧ページを巡回し、各回の HTML を保存。
その後、BeautifulSoup を用いて HTML 解析し、回号、抽選日、当選番号 を抽出します。

🚀 特徴（Features）

✔ Selenium & BeautifulSoup のハイブリッド構成
　JavaScript 必須ページ → Selenium
　個別ページの解析 → BeautifulSoup

✔ 高速化のため HTML をローカル保存して再解析

✔ BeautifulSoup 側で A/B 2 種類の HTML パターンを自動認識

✔ 回号の欠番（欠損回）を自動検出

✔ numbers.csv として保存

✔ ポートフォリオ案件として読みやすいコード構成

📦 収集される項目
項目名	内容
times	回号（例：第1234回 → 1234）
date	抽選日
number	当選番号
🗂 フォルダ構成
project/
│
├─ scraper/  ← SeleniumでHTML収集するコード
│   └─ get_html.py
│
├─ parser/   ← BeautifulSoupで解析するコード
│   └─ parse_numbers.py
│
├─ numbers_HTML/  ← 取得したHTMLファイル
│
└─ numbers.csv   ← 最終出力

▶ 使い方
① HTML収集（Selenium）
python scraper/get_html.py

② HTML解析（BeautifulSoup）
python parser/parse_numbers.py

③ CSV と欠番が生成される

numbers.csv

missing_numbers（標準出力）

🧠 使用技術

Python 3.x

Selenium

BeautifulSoup4

pandas

lxml

📄 ライセンス

MIT License
