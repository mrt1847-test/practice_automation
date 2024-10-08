import os
import platform
import subprocess
import getpass
import pytest
from appium import webdriver
import time
from appium.options.android import UiAutomator2Options
from src.home import *

if 'mac' in os_version:  # 맥 OS인 경우
  a = subprocess.Popen("appium", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
elif 'Windows' in os_version:  # windows인 경우
  a = subprocess.run('start cmd /K "appium"', shell=True)
  time.sleep(5)

if 'mac' in os_version:  # 맥 OS인 경우
  # # 가상 디바이스 활성화
  v = subprocess.Popen("emulator -avd " + json_data[0]["ss_0"]["input_select_android_version"]["aos_version"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

elif 'Windows' in os_version:
  # # 가상 디바이스 활성화
  v = subprocess.Popen("emulator -avd " + json_data[0]["ss_0"]["input_select_android_version"]["aos_version"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
time.sleep(60)

# 디바이스 및 앱 정보 설정pip
os_version=platform.platform()
if 'Windows' in os_version: # windows인 경우
  options = UiAutomator2Options()
  options.platformName = "Android"
  options.deviceName = "AOS14"  # 에뮬레이터 또는 실제 장치의 이름
  options.app = "C:\\APK\\GmarketMobile-debugFinal.09090314.apk"  # 앱의 APK 파일 경로
  options.appPackage = "com.ebay.kr.gmarket"  # 앱 패키지 이름
  options.appActivity = "com.ebay.kr.gmarket.eBayKoreaGmarketActivity"  # 시작 액티비티 이름
elif 'mac' in os_version: 
  options = UiAutomator2Options()
  options.platformName = "Android"
  options.deviceName = "AOS14"  # 에뮬레이터 또는 실제 장치의 이름
  options.app = "C:\\APK\\GmarketMobile-debugFinal.09090314.apk"  # 앱의 APK 파일 경로
  options.appPackage = "com.ebay.kr.gmarket"  # 앱 패키지 이름
  options.appActivity = "com.ebay.kr.gmarket.eBayKoreaGmarketActivity"  # 시작 액티비티 이름

# Appium 서버와 연결
driver = webdriver.Remote('http://localhost:4723', options=options)

# 앱에서 자동화 테스트 수행
time.sleep(100)  # 앱이 로드되기를 기다림

# 예: 특정 버튼 클릭
button = driver.find_element_by_id("com.example:id/button")
button.click()

# 테스트 종료
driver.quit()
