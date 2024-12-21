
# 앱에서 자동화 테스트 수행
# 명령어 python -m pytest .\test.py
def test111(driver):

  from src.home import HomePage
  home_page = HomePage(driver)
  home_page.input_move_login_screen(use_type=2)

  # 테스트 종료
  driver.quit()
