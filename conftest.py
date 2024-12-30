import time
import subprocess
import pytest
from appium.options.android import UiAutomator2Options
import platform
import os
from appium import webdriver
import psutil

@pytest.fixture
def driver():
    # 디바이스 및 앱 정보 설정pip
    os_version = platform.platform()
    if 'Windows' in os_version:  # windows인 경우
        options = UiAutomator2Options()
        app_path = os.path.abspath("C:/APK/GmarketMobile-debugFinal.09090314.apk")
        options.PlatformName = "Android"
        options.deviceName = "AOS14"  # 에뮬레이터 또는 실제 장치의 이름
        options.app = app_path  # 앱의 APK 파일 경로
        options.appPackage = "com.ebay.kr.gmarket"  # 앱 패키지 이름
        options.appActivity = "com.ebay.kr.gmarket.eBayKoreaGmarketActivity"  # 시작 액티비티 이름
        options.adbExecTimeout = 60000

    elif 'mac' in os_version:
        options = UiAutomator2Options()
        app_path = os.path.abspath("/Users/mrt1847/APK/GmarketMobile_64.06180612.apk")
        options.platformName = "Android"
        options.deviceName = "AOS14"  # 에뮬레이터 또는 실제 장치의 이름
        options.app = app_path  # 앱의 APK 파일 경로
        options.appPackage = "com.ebay.kr.gmarket"  # 앱 패키지 이름
        options.appActivity = "com.ebay.kr.gmarket.eBayKoreaGmarketActivity"  # 시작 액티비티 이름
        options.adbExecTimeout = 60000

    # Appium 서버와 연결
    driver = None
    try:
        driver = webdriver.Remote("http://localhost:4723", options=options)
        print("Driver initialized successfully!")
    except Exception as e:
        print(f"Driver initialization failed: {e}")
        raise
    while driver == None:
        time.sleep(1)

    driver.start_activity("com.ebay.kr.gmarket","com.ebay.kr.gmarket.eBayKoreaGmarketActivity")
    return driver

@pytest.fixture(scope="session", autouse=True)
def manage_appium_server():
    print("테스트 실행 전 준비 작업 시작...")

    # (필요시 Appium 서버 실행 코드 포함 가능)
    # ...
    try:
        os_version = platform.platform()
        # 운영 체제에 따라 명령어 설정
        if 'mac' in os_version:  # 맥 OS인 경우
            a = subprocess.Popen("appium", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        elif 'Windows' in os_version:  # windows인 경우
            a = subprocess.run('start cmd /K "appium"', shell=True)
            time.sleep(5)

    except FileNotFoundError:
        print("Appium이 시스템 경로에 설치되어 있는지 확인하세요.")

    except Exception as e:
        print("오류 발생:", e)
    yield a

    # 테스트 종료 후 Appium 서버 종료
    print("테스트 종료 후 정리 작업 시작...")
    try:
        for proc in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
            try:
                # cmdline 속성의 유효성을 확인합니다.
                if proc.info['cmdline'] and 'appium' in ' '.join(proc.info['cmdline']):
                    # 프로세스를 종료합니다.
                    psutil.Process(proc.info['pid']).terminate()
                    print(f"Appium process with PID {proc.info['pid']} terminated.")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, IndexError):
                pass
    except Exception as e:
        print("Appium 종료 중 오류 발생:", e)