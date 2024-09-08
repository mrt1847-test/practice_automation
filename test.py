from appium import webdriver
import time

# 디바이스 및 앱 정보 설정
desired_caps = {
    "platformName": "Android",
    "deviceName": "Android Emulator",  # 실제 디바이스의 이름을 사용
    "app": "/path/to/your/app.apk",   # 테스트하려는 APK 파일 경로
    "appPackage": "com.example",      # 앱의 패키지 이름
    "appActivity": "com.example.MainActivity",  # 앱의 시작 액티비티
    "automationName": "UiAutomator2"  # Android용으로 UiAutomator2 사용
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
