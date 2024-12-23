
import pydata_google_auth
import gspread
import json
import os
import platform

SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']
credentials = pydata_google_auth.get_user_credentials(SCOPES, auth_local_webserver=True)
credentials.access_token = credentials.token
gc = gspread.authorize(credentials)

spreadsheet_url = "https://docs.google.com/spreadsheets/d/1Hmrpoz1EVACFY5lHW7r4v8bEtRRFu8eay7grCojRr3E/edit?gid=0#gid=0"
sh = gc.open_by_url(spreadsheet_url)
worksheet = sh.worksheet("tc1")
os_version = platform.platform()
if 'Windows' in os_version:  # windows인 경우
  param_json_path = os.path.dirname(__file__) + '\\json\\'
  current_json = param_json_path + os.path.splitext(os.path.basename(__file__))[0] + '.json'
elif 'mac' in os_version:
  param_json_path = os.path.dirname(__file__) + '/json/'
  current_json = param_json_path + os.path.splitext(os.path.basename(__file__))[0] + '.json'

with open(current_json, 'r', encoding='utf-8') as file:
  json_data = json.load(file)

def input_pass(sheet_num):
  worksheet.update([["pass"]], "D{0}".format(sheet_num))
  worksheet.format("D{0}".format(sheet_num), {"textFormat": {"foregroundColor": {"red": 0.0, "green": 0.5, "blue": 0.0}, "bold": True}})

def input_fail(sheet_num, error_reason):
  worksheet.update([["fail"]], "D{0}".format(sheet_num))
  worksheet.format("D{0}".format(sheet_num), {"textFormat": {"foregroundColor": {"red": 1.0, "green": 0.0, "blue": 0.0}, "bold": True}})
  worksheet.update([[str(error_reason)]], "E{0}".format(sheet_num))

# 앱에서 자동화 테스트 수행
# 명령어 python -m pytest .\test.py
def test1(driver):
  from src.home import HomePage
  home_page = HomePage(driver)
  try:
    home_page.input_move_login_screen(use_type=2)
    input_pass(3)
  except Exception as e:
    input_fail(3, e)
  try:
    home_page.input_move_login_screen(use_type=2)
    input_pass(4)
  except Exception as e:
    input_fail(4, e)
  finally:
    # 테스트 종료
    driver.quit()

def test2(driver):
  from src.home import HomePage
  home_page = HomePage(driver)
  try:
    home_page.input_move_login_screen(use_type=2)
    input_pass(5)
  except Exception as e:
    input_fail(5, e)
  finally:
    # 테스트 종료
    driver.quit()
