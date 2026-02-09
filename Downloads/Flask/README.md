# 📔 Flask 일상 관리 앱

Python Flask 기반 개인 일상 관리 웹 애플리케이션

---

## 🎯 주요 기능

### 1. 📔 일상 기록
- 날짜별 일기 작성 및 조회
- 기분 이모지 선택 (😊😢😡😴🤗😰)
- 힘들었던 일 / 좋았던 일 / 오늘의 이야기 기록
- 날짜별 일기 상세보기

### 2. 📚 독서 메모
- 책 제목, 저자 정보 관리
- 읽기 상태 (읽을 예정/읽는 중/완독)
- 평점 시스템 (⭐ 1~5점)
- 독서 메모 작성

### 3. 💬 응원 메시지
- 랜덤 응원 메시지 표시 (20개 기본 제공)
- 서버사이드 렌더링 (Python random)
- 페이지 새로고침으로 새 메시지

### 4. ✅ 할일 목록
- 날짜/시간별 할일 관리
- 하루 할일 / 한달 할일 구분
- **브라우저 알람 기능**
  - 설정 시간 도달 시 자동 알림
  - 🔊 비프음 3회 재생
  - 📳 진동 5회 (안드로이드)
  - 💬 브라우저 알림창 표시
- 완료/미완료 상태 관리

### 5. 🌡️ 현재 기온
- **2025년 2월 9일 기온 데이터** 표시
- 고속도로 휴게소 날씨 API 사용
- 실시간 시계 (1초마다 갱신)
- 기온에 따른 아이콘 자동 변경
- 5분마다 자동 새로고침

---

## 🚀 빠른 시작

### 1. 필수 요구사항
```
Python 3.7 이상
pip (Python 패키지 관리자)
```

### 2. 설치
```bash
# 라이브러리 설치
pip install Flask requests

# 또는
pip install -r requirements.txt
```

### 3. 실행
```bash
# Flask 폴더로 이동
cd C:\Users\사용자이름\Downloads\Flask

# 서버 실행
python app.py
```

### 4. 접속
```
컴퓨터: http://localhost:5000
안드로이드: http://[컴퓨터IP]:5000
```

---

## 📂 프로젝트 구조

```
Flask/
├── app.py                    # Flask 메인 애플리케이션
├── config.py                 # API 설정 (날씨 API 키)
├── requirements.txt          # 필요한 라이브러리
├── README.md                # 프로젝트 설명서
├── test_weather_api.py      # 날씨 API 테스트
├── test_weather_multi.py    # 여러 시간대 테스트
├── check_api_structure.py   # API 구조 확인
├── fix_imports.py           # 문제 진단 스크립트
├── data/                    # 데이터 저장 폴더 (자동 생성)
│   ├── diary.json          # 일기 데이터
│   ├── books.json          # 독서 메모 데이터
│   └── todos.json          # 할일 데이터
├── static/
│   ├── css/
│   │   └── style.css       # 스타일시트
│   ├── manifest.json       # PWA 설정
│   └── sw.js              # Service Worker
└── templates/
    ├── index.html          # 메인 페이지
    ├── diary.html          # 일기 목록
    ├── diary_write.html    # 일기 작성
    ├── diary_view.html     # 일기 상세
    ├── books.html          # 독서 목록
    ├── books_add.html      # 책 추가
    ├── messages.html       # 응원 메시지
    ├── todos.html          # 할일 목록
    └── weather.html        # 날씨 (기온)
```

---

## 📱 안드로이드 접속 방법

### 1. 컴퓨터 IP 확인
```bash
ipconfig
```
→ IPv4 주소 확인 (예: 172.16.1.101)

### 2. 방화벽 허용
```powershell
# PowerShell 관리자 권한으로 실행
netsh advfirewall firewall add rule name="Flask" dir=in action=allow protocol=TCP localport=5000
```

### 3. 같은 Wi-Fi 연결
- 컴퓨터와 안드로이드를 같은 Wi-Fi에 연결

### 4. 안드로이드 Chrome에서 접속
```
http://172.16.1.101:5000
```

---

## 🌡️ 날씨 API 설정

### config.py
```python
# 고속도로 휴게소 날씨 API
WEATHER_API_KEY = "1663676750"
WEATHER_API_URL = "https://data.ex.co.kr/openapi/restinfo/restWeatherList"
```

### 데이터 요청
- **날짜:** 2025년 2월 9일 (고정)
- **시간:** 현재 시각 기준 최근 6시간 시도
- **필드:** `lowestTemp` (최저 기온)

### 기온별 아이콘
| 기온 | 아이콘 |
|------|--------|
| 30°C 이상 | 🔥 |
| 25~29°C | ☀️ |
| 20~24°C | 😊 |
| 10~19°C | 🍂 |
| 0~9°C | ❄️ |
| 0°C 미만 | 🥶 |

---

## 🧪 테스트

### 날씨 API 테스트
```bash
# 기본 테스트
python test_weather_api.py

# 여러 시간대 테스트
python test_weather_multi.py

# API 구조 확인
python check_api_structure.py

# 문제 진단
python fix_imports.py
```

---

## 📋 주요 URL

| 페이지 | URL | 설명 |
|--------|-----|------|
| 메인 | `/` | 대시보드 |
| 일상 기록 | `/diary` | 일기 목록 |
| 일기 작성 | `/diary/write` | 새 일기 |
| 독서 메모 | `/books` | 책 목록 |
| 책 추가 | `/books/add` | 새 책 |
| 응원 메시지 | `/messages` | 랜덤 메시지 |
| 할일 목록 | `/todos` | 할일 관리 |
| 기온 | `/weather` | 현재 기온 |

### API 엔드포인트
```
GET /api/weather           # 날씨 데이터
GET /api/todos/today       # 오늘 할일
GET /messages/random       # 랜덤 메시지
```

---

## 🔧 문제 해결

### Q1: requests 모듈 인식 안 됨
```bash
pip install requests
```

### Q2: config.py 인식 안 됨
- `config.py` 파일이 `app.py`와 같은 폴더에 있는지 확인
- 파일명이 정확한지 확인 (대소문자 구분)

### Q3: 안드로이드에서 접속 안 됨
- ✅ 같은 Wi-Fi 연결 확인
- ✅ 방화벽 5000번 포트 허용
- ✅ IP 주소 정확히 입력 (`http://IP:5000`)
- ✅ Flask 서버 실행 중인지 확인

### Q4: 날씨 데이터 표시 안 됨
- API가 2025년 2월 9일 데이터를 제공하는지 확인
- 터미널 로그 확인 (어느 시간대에 데이터 발견되는지)
- 데이터 없으면 자동으로 샘플 데이터 표시

### Q5: 할일 알람 안 울림
- ✅ 브라우저 알림 권한 허용
- ✅ 페이지를 열어두기 (백그라운드)
- ✅ 휴대폰 볼륨 확인
- ✅ 무음 모드 해제

### Q6: SSL 경고 메시지
```
InsecureRequestWarning: Unverified HTTPS request...
```
- 이것은 경고일 뿐, 정상 작동합니다
- 무시해도 됩니다

---

## 💾 데이터 관리

### 데이터 저장 위치
```
Flask/data/
├── diary.json    # 일기
├── books.json    # 독서 메모
└── todos.json    # 할일
```

### 백업 방법
```bash
# data 폴더 복사
xcopy data C:\Backup\Flask_data /E /I /Y

# 또는
robocopy data C:\Backup\Flask_data /E
```

### 복구 방법
```bash
# 백업에서 복사
xcopy C:\Backup\Flask_data data /E /I /Y
```

---

## 🎨 주요 특징

### ✅ 완전한 Python/Flask 기반
- 서버사이드 렌더링
- JavaScript 의존성 최소화
- JSON 파일 기반 데이터 저장

### ✅ 모바일 친화적
- 반응형 디자인
- 안드로이드 Chrome 지원
- PWA 설치 가능

### ✅ 실시간 기능
- 할일 알람 (소리 + 진동)
- 실시간 시계 (1초마다)
- 자동 날씨 갱신 (5분마다)

### ✅ 2025년 날씨 데이터
- 고속도로 휴게소 API 사용
- 2025년 2월 9일 기온 데이터
- `lowestTemp` 필드 사용
- 자동 샘플 데이터 대체

---

## 📞 주요 명령어

```bash
# 설치
pip install Flask requests

# 실행
python app.py

# 테스트
python test_weather_multi.py

# 진단
python fix_imports.py

# 종료
Ctrl + C
```

---

## 🌡️ 날씨 기능 상세

### 요청 방식
```python
# 2025년 2월 9일 데이터 요청
sdate = "20250209"
stdHour = "15"  # 15시 데이터

# 또는 현재 시각 기준
yesterday = now - timedelta(days=1)
target_date = datetime(2025, yesterday.month, yesterday.day)
```

### 응답 데이터
```json
{
  "temperature": 5,
  "humidity": 45,
  "wind_speed": 2.3,
  "rainfall": "0",
  "weather": "맑음",
  "icon": "❄️",
  "update_time": "2025-02-09 15:00",
  "hours_ago": 0
}
```

### 자동 대체 기능
API 데이터가 없으면 **자동으로 샘플 데이터** 생성:
- 겨울: -5°C ~ 10°C
- 봄: 10°C ~ 20°C
- 여름: 25°C ~ 35°C
- 가을: 10°C ~ 20°C

---

## 🎓 사용 팁

### 일상 기록
- 매일 저녁 하루를 돌아보며 작성
- 기분 아이콘으로 감정 표현
- 좋았던 일도 꼭 기록

### 독서 메모
- 책을 읽기 전에 '읽을 예정'으로 추가
- 읽는 중 인상 깊은 구절 메모
- 완독 후 평점과 총평 작성

### 응원 메시지
- 힘든 날 접속해서 위로받기
- "다른 메시지 보기"로 새 메시지
- 마음에 드는 메시지 캡처

### 할일 목록
- 아침에 하루 할일 정리
- 중요한 일정은 시간 설정 + 알람
- 완료한 일은 체크해서 성취감

### 날씨
- 외출 전 현재 기온 확인
- 자동 갱신으로 실시간 정보
- 기온에 따른 아이콘 확인

---

## 🔄 업데이트 내역

### v1.0 (최종)
- ✅ 일상 기록 기능
- ✅ 독서 메모 기능
- ✅ 응원 메시지 (Python 랜덤)
- ✅ 할일 목록 + 알람 (소리/진동)
- ✅ 기온 표시 (2025년 데이터)
- ✅ 실시간 시계
- ✅ 안드로이드 모바일 지원
- ✅ PWA 지원
- ✅ 자동 샘플 데이터 대체
- ✅ `lowestTemp` 필드 사용

---

## 📄 라이선스

개인 학습 및 사용 목적의 프로젝트입니다.

---

## 👨‍💻 개발 정보

- **언어:** Python 3.7+
- **프레임워크:** Flask 3.0.0
- **라이브러리:** requests, urllib3
- **데이터:** JSON 파일
- **API:** 한국도로공사 고속도로 휴게소 날씨

---

## 🎉 즐거운 일상 관리 되세요!

**주요 명령어 한눈에:**
```bash
pip install Flask requests    # 설치
python app.py                 # 실행
http://localhost:5000         # 접속
```

**안드로이드 접속:**
```bash
ipconfig                                      # IP 확인
http://172.16.1.101:5000                     # 접속
```

**문제 발생 시:**
```bash
python fix_imports.py         # 진단
python test_weather_multi.py  # 날씨 테스트
```
