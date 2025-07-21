# 📱 Appium & Pytest 기반 모바일 테스트 자동화 프로젝트

본 프로젝트는 Appium과 Pytest를 활용하여 모바일 앱에 대한 테스트 자동화를 수행합니다. 테스트 케이스 설계부터 자동화 코드 작성, 결과 리포트 및 Google Sheets 연동까지 포함된 예제입니다.

---

## 📁 프로젝트 구조

```
practice_automation/
├── img/                 # 테스트 대상 이미지 리소스
├── json/                # 테스트 데이터 및 API 요청 정보
├── src/
│   └── base_pages/      # Page Object Model 기반 테스트 대상 화면 모듈
│       ├── etc.py       # 기타 페이지 정의
│       ├── home.py      # 홈 화면 정의
├── .gitignore
├── Pipfile / Pipfile.lock  # Python 의존성 관리 파일
├── config.json          # 테스트 설정 정보 (디바이스, 플랫폼 등)
├── conftest.py          # Pytest 설정 및 fixture 정의
├── test.py              # 주요 테스트 시나리오 정의
└── README.md
```

---

## ⚙️ 주요 기능

* Appium을 활용한 Android/iOS 앱 테스트
* Pytest 기반 테스트 시나리오 정의
* Page Object Pattern 적용으로 모듈화된 테스트 코드 구성
* 테스트 설정 파일(config.json) 기반의 동적 테스트 환경 제어
* Google Sheets와 연동하여 테스트 결과 자동 기록

---

## 🚀 실행 방법

### 1. 의존성 설치

```bash
pip install -r requirements.txt
# 또는
pipenv install
```

### 2. Appium 서버 실행

```bash
appium
```

### 3. 테스트 실행

```bash
pytest test.py
```

---

## ⚙️ 테스트 설정 (`config.json`)

```json
{
  "platformName": "Android",
  "platformVersion": "11.0",
  "deviceName": "emulator-5554",
  "app": "/path/to/app.apk"
}
```

---

## 📝 테스트 결과 기록 (Google Spreadsheet 연동)

본 프로젝트는 테스트 실행 결과를 아래 Google 스프레드시트에 자동으로 기록하도록 설계되어 있습니다:

📄 [테스트 결과 시트 링크](https://docs.google.com/spreadsheets/d/1Hmrpoz1EVACFY5lHW7r4v8bEtRRFu8eay7grCojRr3E/edit?gid=0#gid=0)

### ✅ 연동 방식

* Google Sheets API를 사용하여 pytest 테스트 결과를 실시간으로 기록
* 각 테스트케이스 수행 후 결과(`PASS`/`FAIL`), 실행 시간, 에러 메시지 등을 시트에 반영

### 📦 필요 패키지

```bash
pip install gspread oauth2client
```

### 🔐 인증 방식

1. [Google Cloud Console](https://console.cloud.google.com/)에서 서비스 계정 생성
2. 서비스 계정에 Sheets API 사용 권한 부여
3. 서비스 계정 키(`credentials.json`)를 프로젝트 루트에 저장
4. 공유 대상 스프레드시트에 서비스 계정 이메일을 `편집자`로 등록

### 🧪 기록 예시

| TC ID | 테스트 설명     | 결과   | 실행 시간 | 오류 메시지        |
| ----- | ---------- | ---- | ----- | ------------- |
| TC001 | 로그인 기능 검증  | PASS | 1.2s  | -             |
| TC002 | 장바구니 담기 동작 | FAIL | 0.8s  | NoSuchElement |

### 🧩 구현 위치

* 결과 기록 로직은 `conftest.py` 또는 후처리용 `pytest hook`에서 구현 가능 (예: `pytest_terminal_summary`, `pytest_runtest_logreport` 활용)
* 연동 코드 예시 필요 시 제공 가능

---

## 🙋 문의

* 작성자: \[작성자 이름]
* 연락처: \[이메일 또는 슬랙 ID]
