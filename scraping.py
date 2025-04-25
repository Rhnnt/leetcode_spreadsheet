from selenium import webdriver
from bs4 import BeautifulSoup
import json
import gspread
from gspread import Cell
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os

load_dotenv()

PATH_TO_CREDENTIAL_JSON = os.getenv('PATH_TO_CREDENTIAL_JSON')


scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(PATH_TO_CREDENTIAL_JSON, scope)
client = gspread.authorize(creds)

spreadsheet = client.open("LeetCode Top Interview 150")
sheet = spreadsheet.sheet1 

sheet.append_row(["Title"])

driver = webdriver.Chrome()
driver.get("https://leetcode.com/studyplan/top-interview-150/")
driver.implicitly_wait(5)

soup = BeautifulSoup(driver.page_source, "html.parser")

scripts = soup.find("script", {"id": "__NEXT_DATA__"})

json_data = json.loads(scripts.string)
subgroups = json_data["props"]["pageProps"]["dehydratedState"]["queries"][0]["state"]["data"]["studyPlanV2Detail"]["planSubGroups"] #subgroupsはカテゴリごとの配列

titles = []
links = []

for group in subgroups:
    for q in group['questions']:
        titles.append(q['title'])
        link = f'https://leetcode.com/problems/{q['titleSlug']}'
        links.append(link)

cells = []
for i, (title, link) in enumerate(zip(titles, links)):
    formula = f'=HYPERLINK("{link}", "{title}")'
    cell = Cell(row=i + 2, col=1, value=formula)  # A列＝col=1
    cells.append(cell)





sheet.update_cells(cells, value_input_option="USER_ENTERED")

# print(titles)
# print(links)








