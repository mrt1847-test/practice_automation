# 📱 Android 앱 테스트 자동화 예제

**practice\_automation**

이 프로젝트는 **Appium**과 **pytest** 기반으로 Android 앱(G마이크앱)의 테스트 자동화를 실습하기 위해 구성된 예제 레퍼지토리입니다. 앱 실행, 환경 설정, 서버 관리, 테스트 실행 전반을 자동화하고 있으며, Page Object Model(POM)을 적용한 구조로 확장이 용이합니다.

---

## 파일 구조

```
practice_automation/
├── img/                     # 테스트 이미지 또는 시각자료 저장 (uc120적)
├── json/                    # 테스트용 JSON 데이터 (uc120적)
├── src/
│   └── base_pages/          # Page Object 정의 모듈
│       ├── etc.py           # 공통 유틸성 페이지 요소
│       └── home.py          # 홈 화면 관련 Page Object
├── config.json              # OS별 앱/크롬드라이버 경로 설정
├── conftest.py              # pytest fixture: Appium 서버 및 드라이버 설정
├── test.py                  # uc0b4포 테스트 스크립트
├── Pipfile / Pipfile.lock   # Pipenv 환경 의정성 설정
├── .gitignore               # Git 제외 파일
└── README.md                # 프로젝트 설명서
```

---

## 환경 세팅

### ✅ 요구상

* Python 3.8+
* Appium 설치
  `npm install -g appium`
* Android Emulator 또는 실기기 연결
* ChromeDriver 필요 시 `--allow-insecure chromedriver_autodownload` 옵션 사용

### 파폭지 설치

```bash
pip install pipenv
pipenv install
```

또는

```bash
pip install -r requirements.txt
```

---

## `config.json` 예시

```json
{
  "win": {
    "app_path": "./apps/MyApp.apk",
    "chrome_path": "./drivers/chromedriver_win.exe"
  },
  "mac": {
    "app_path": "./apps/MyApp.apk",
    "chrome_path": "./drivers/chromedriver_mac"
  }
}
```

OS에 따라 앱 경로와 크롬드라이버 경로를 분기하여 자동 설정합니다.

---

## 테스트 실행

```bash
pytest
```

실행 순서:

1. Appium 서버 자동 실행 (`conftest.py` fixture)
2. 드라이버 설정 및 연결 (`driver()` fixture)
3. 테스트 수행 (`test.py`)
4. 종료 시 Appium 서버 자동 종료

---

## 주요 기능

| 기능                          | 설명                                  |
| --------------------------- | ----------------------------------- |
| ✅ Appium 서버 자동 실행/종료        | `manage_appium_server()` fixture 활용 |
| ✅ 하나의 설정으로 macOS/Windows 지원 | `config.json` 분기 적용                 |
| ✅ 앱 실행 - 드라이버 - 테스트 가정을 자동화 |                                     |
| ✅ Page Object Model 구조      | `src/base_pages/` 파일로 화면별 정의        |
| ✅ pytest 기반 테스트 종합 실행       |                                     |

---

## 테스트 예시 (`test.py`)

```python
def test_launch(driver):
    assert driver.current_activity == "com.ebay.kr.gmarket.eBayKoreaGmarketActivity"
```

---

## Page Object 구조 (`src/base_pages/`)

* `home.py`: 홈 화면 관련 요소 및 메시지 특정
* `etc.py`: 공통 또는 기타 화면의 요소 구성

예시:

```python
# home.py
class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_banner(self):
        self.driver.find_element(...).click()
```

---

## 확장 제안

* `tests/` 디렉토리 분리와 모듈화된 테스트 케이스 관리
* `pytest.mark.smoke`, `pytest.mark.android` 등 마커 등록
* Allure 또는 HTML 리포트 연동
* Testrail 연동 (API 기능)
* iOS 기기와 확장 기능 및 Grid

---

## 기억조 / 기어

번역, 개선사항, 테스트의 확장적 규칙이 필요하다면 PR 또는 issue를 자유롭게 남겨주세요.


가상디바이스 실행 후 python -m pytest .\test.py 실행

https://docs.google.com/spreadsheets/d/1Hmrpoz1EVACFY5lHW7r4v8bEtRRFu8eay7grCojRr3E/edit?gid=0#gid=0

