
import pydata_google_auth
import gspread

SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']
credentials = pydata_google_auth.get_user_credentials(SCOPES, auth_local_webserver=True)
credentials.access_token = credentials.token
gc = gspread.authorize(credentials)

spreadsheet_url = "https://docs.google.com/spreadsheets/d/1Hmrpoz1EVACFY5lHW7r4v8bEtRRFu8eay7grCojRr3E/edit?gid=0#gid=0"
sh = gc.open_by_url(spreadsheet_url)
worksheet = sh.worksheet("tc1")
# 앱에서 자동화 테스트 수행
# 명령어 python -m pytest .\test.py
def test1(driver):
  from src.home import HomePage
  home_page = HomePage(driver)
  try:
    home_page.input_move_login_screen(use_type=2)
    worksheet.update([["pass"]], "D3")
  except Exception as e:
    worksheet.update([["fail"]], "D3")
    worksheet.update([[str(e)]], "E3")
  try:
    home_page.input_move_login_screen(use_type=2)
    worksheet.update([["pass"]], "D4")
  except Exception as e:
    worksheet.update([["fail"]], "D4")
    worksheet.update([[str(e)]], "E4")
  finally:
    # 테스트 종료
    driver.quit()

def test2(driver):
  from src.home import HomePage
  home_page = HomePage(driver)
  try:
    home_page.input_move_login_screen(use_type=2)
    worksheet.update([["pass"]], "D5")
  except Exception as e:
    worksheet.update([["fail"]], "D5")
    worksheet.update([[str(e)]], "E5")
  finally:
    # 테스트 종료
    driver.quit()
