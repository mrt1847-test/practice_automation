from src.base_pages.base import *


class HomePage():

    IMPLICIT_WAIT_TIME = 10
    TIMEOUT = 30

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(self.IMPLICIT_WAIT_TIME)
        self.timeout = self.TIMEOUT

    def input_move_login_screen(self, use_type):
        """

        Gmarket 로그인 화면 이동 (팝업 처리 및 로그인 화면 이동)
        :param: 없음
        :return: 없음
        :example: common_page_param.input_move_login_screen(2)

        """

        if use_type == 2:
            # 디바이스 접근 권한 허용 승인
            try:
                time.sleep(2)
                runtext = '디바이스 접근 권한 허용 승인'
                print("#", runtext, "시작")
                id = "com.ebay.kr.gmarket:id/appPermissionBtn"
                element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, id)))
                element.click()
                print("#", runtext, "종료")
            except:
                print("Not Permission popup")
                raise

            # 지마켓 Notification 허용 알림 승인
            try:
                time.sleep(2)
                runtext = '지마켓 Notification 허용 알림 승인'
                print("#", runtext, "시작")
                xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]"
                element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                element.click()
                print("#", runtext, "종료")
            except Exception as e:
                print("Not Notification popup", e)

            # 빅스마일데이 팝업 끄기
            try:
                time.sleep(2)
                runtext = '빅스마일데이 팝업 끄기'
                print("#", runtext, "시작")
                id = "com.ebay.kr.gmarket:id/ivClose"
                element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, id)))
                element.click()
                print("#", runtext, "종료")
            except Exception as e:
                print("Not Notification popup", e)
        else:
            print("#", "권한 팝업 처리하지 않음")
