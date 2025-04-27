from selenium import webdriver
from bs4 import BeautifulSoup
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os
import gspread
from gspread_formatting import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

PATH_TO_CREDENTIAL_JSON = os.getenv('PATH_TO_CREDENTIAL_JSON')


scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(PATH_TO_CREDENTIAL_JSON, scope)
client = gspread.authorize(creds)

spreadsheet = client.open("LeetCode Top Interview 150")
sheet = spreadsheet.sheet1 

headers = ["Title", "Count", "Status", "Last Attempted"]
sheet.update([headers], 'A1:D1')

driver = webdriver.Chrome()
driver.get("https://leetcode.com/studyplan/top-interview-150/")

# 完全にロードされる前に解析してしまうのを防ぐ
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "__NEXT_DATA__"))
)

soup = BeautifulSoup(driver.page_source, "html.parser")

scripts = soup.find("script", {"id": "__NEXT_DATA__"})

json_data = json.loads(scripts.string)
subgroups = json_data["props"]["pageProps"]["dehydratedState"]["queries"][0]["state"]["data"]["studyPlanV2Detail"]["planSubGroups"] #subgroupsはカテゴリごとの配列

# A列　ハイパーリンク
titles = []
links = []

for group in subgroups:
    for q in group['questions']:
        titles.append(q['title'])
        link = f'https://leetcode.com/problems/{q['titleSlug']}'
        links.append(link)

problems_len = len(titles)

formulas = [[f'=HYPERLINK("{link}", "{title}")'] for (title, link) in zip(titles, links)]
sheet.update(formulas, f'A2:A{problems_len+1}', value_input_option="USER_ENTERED")
set_column_width(sheet, 'A', 300)

# B列　解いた回数
count_values = [[0] for _ in range(problems_len)]
sheet.update(count_values, f'B2:B{problems_len+1}', value_input_option="USER_ENTERED")
set_column_width(sheet, 'B', 80)

# C列　ステータスのプルダウン
status_range = f'C2:C{problems_len+1}'
rule = DataValidationRule(
    BooleanCondition('ONE_OF_LIST', ['やってない!', '怪しい🤔', '理解💡']),
    showCustomUi=True
)
set_data_validation_for_cell_range(sheet, status_range, rule)

fmt = cellFormat(
    backgroundColor=color(0.93, 0.98, 1), 
    horizontalAlignment='CENTER',
    textFormat=textFormat(
        bold=False,
        fontSize=10
    ),
    borders=borders(
        top=border('SOLID', color=Color(0.8, 0.8, 0.8)),   
        bottom=border('SOLID', color=Color(0.8, 0.8, 0.8))
    )
)

format_cell_range(sheet, status_range, fmt)

init_values = [['やってない!'] for _ in range(problems_len)]
sheet.update(init_values, f'C2:C{problems_len+1}', value_input_option="USER_ENTERED")

# D列　Last Attempted
last_attempted_range = f'D2:D{problems_len+1}'

date_rule = DataValidationRule(
    condition=BooleanCondition('DATE_IS_VALID'),
    showCustomUi=True
)

date_fmt = cellFormat(
    backgroundColor=color(1, 0.95, 0.95),
    numberFormat=numberFormat(type='DATE', pattern='yyyy-mm-dd'),
    horizontalAlignment='CENTER',
    textFormat=textFormat(
        bold=False,
        fontSize=10
    ),
    borders=borders(
        top=border('SOLID', color=Color(0.8, 0.8, 0.8)),   
        bottom=border('SOLID', color=Color(0.8, 0.8, 0.8))
    )
)

from datetime import datetime

cur_datetime = datetime.now()
cur_str_date = cur_datetime.strftime("%Y-%m-%d")
last_attempted_values = [[cur_str_date] for _ in range(problems_len)]
sheet.update(last_attempted_values, f'D2:D{problems_len+1}', value_input_option="USER_ENTERED")

set_data_validation_for_cell_range(sheet, last_attempted_range, date_rule)
format_cell_range(sheet, last_attempted_range, date_fmt)













