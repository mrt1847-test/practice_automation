import os


from appium import webdriver
import time

# 디바이스 및 앱 정보 설정pip
desired_caps = {
    "platformName": "Android",
    "deviceName": "AOS14",
    "automationName": "UiAutomator2",
    "app": "C:\\APK\\GmarketMobile-debugFinal.09090314.apk",
    "newCommandTimeout": 900,
    "appPackage": "com.ebay.kr.gmarket",
    "appActivity": "com.ebay.kr.gmarket.eBayKoreaGmarketActivity",
    "acceptInsecureCerts": true,
    "noReset": "false",
    "chromedriverExecutable": "c:\\webdriver\\appium\\chromedriver.exe",
    "appium:chrome_options": {"androidPackage": "com.ebay.kr.gmarket"}

}

# Appium 서버와 연결
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 앱에서 자동화 테스트 수행
time.sleep(5)  # 앱이 로드되기를 기다림

# 예: 특정 버튼 클릭
button = driver.find_element_by_id("com.example:id/button")
button.click()

# 테스트 종료
driver.quit()
