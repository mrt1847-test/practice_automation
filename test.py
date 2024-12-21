import gspread

json_key ="automation-test-practice-31c37bf76e65.json"
gc = gspread.service_account(json_key)
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1Hmrpoz1EVACFY5lHW7r4v8bEtRRFu8eay7grCojRr3E/edit?gid=0#gid=0"
doc = gc.open_by_url(spreadsheet_url)
worksheet = doc.worksheet("tc1")
# 앱에서 자동화 테스트 수행
# 명령어 python -m pytest .\test.py
def test1(driver):
  try:
    from src.home import HomePage
    home_page = HomePage(driver)
    home_page.input_move_login_screen(use_type=2)
    worksheet.update([["pass"]], "C3")
  except:
    worksheet.update([["fail"]], "C3")
  try:
    from src.home import HomePage
    home_page = HomePage(driver)
    home_page.input_move_login_screen(use_type=2)
    worksheet.update([["pass"]], "C4")
  except:
    worksheet.update([["fail"]], "C4")
  finally:
    # 테스트 종료
    driver.quit()

def test2(driver):
  try:
    from src.home import HomePage
    home_page = HomePage(driver)
    home_page.input_move_login_screen(use_type=2)
    worksheet.update([["pass"]], "C5")
  except:
    worksheet.update([["fail"]], "C5")
  finally:
    # 테스트 종료
    driver.quit()
