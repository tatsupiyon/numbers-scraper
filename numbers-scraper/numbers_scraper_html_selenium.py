from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re
import os

chrome_path = r"C:\Users\tatsu\OneDrive\デスクトップ\Lessson\chromedriver-win64\chromedriver.exe"
save_dir = r"C:\Users\tatsu\OneDrive\デスクトップ\Lessson\numbers_HTML"

os.makedirs(save_dir, exist_ok=True)

service = Service(executable_path=chrome_path)
options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(service=service, options=options)
driver.set_page_load_timeout(60)
driver.implicitly_wait(10)

# バックナンバーTOP
driver.get("https://www.mizuhobank.co.jp/takarakuji/check/numbers/backnumber/index.html")
sleep(3)

# URL取得
b_links = driver.find_elements(By.CSS_SELECTOR,
    "tr.section__table-row.js-backnumber-temp-b > td > a"
)

a_links = driver.find_elements(By.CSS_SELECTOR,
    "tr.section__table-row.js-backnumber-temp-a > td:first-of-type > p > a"
)

urls = [tag.get_attribute("href") for tag in (a_links + b_links)]

# 各ページ保存
for url in urls:
    driver.get(url)
    sleep(2)

    # タイトルを安全なファイル名にする
    title = re.sub(r'[\\/*?:"<>|]', '_', driver.title)
    save_path = os.path.join(save_dir, f"{title}.html")

    with open(save_path, "w", encoding="utf-8") as f:
        f.write(driver.page_source)

driver.quit()
print("HTMLの保存が完了しました。")