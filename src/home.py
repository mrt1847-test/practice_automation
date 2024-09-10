from appium.webdriver.common.appiumby import AppiumBy
from src.gtas_python_core.gtas_python_core_package import *
from src.gtas_python_core.gtas_python_core_vault import Vault
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from assertpy import assert_that
import assertpy
import unicodedata
import time
import re


class HomePage():
    button_1 = (AppiumBy.ACCESSIBILITY_ID, "button_1")
    button_1_touch = (AppiumBy.ACCESSIBILITY_ID, "touch!")  # 버튼1 클릭하면 변경됨
    button_2 = (AppiumBy.ACCESSIBILITY_ID, "button_2")
    text_edit = (AppiumBy.XPATH, "//android.widget.EditText")
    check_box = (AppiumBy.XPATH, "//android.widget.CheckBox")
    switch_button = (AppiumBy.XPATH, "//android.widget.Switch")

    def click_button_1(self):
        self.click(self.button_1)

    def click_button_2(self):
        self.click(self.button_2)

    def input_text_edit(self, text: str):
        self.click(self.text_edit)
        self.send_keys(self.text_edit, text)

    def click_check_box(self):
        self.click(self.check_box)

    def click_switch_button(self):
        self.click(self.switch_button)

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
