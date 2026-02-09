"""
API 설정 파일
"""

# 고속도로 휴게소 날씨 API 키
WEATHER_API_KEY = "1663676750"

# 고속도로 휴게소 날씨 API URL (HTTPS)
WEATHER_API_URL = "https://data.ex.co.kr/openapi/restinfo/restWeatherList"

# 주요 휴게소 코드 (예시)
REST_AREAS = {
    "서울": {"name": "서울", "code": "000"},
    "부산": {"name": "부산", "code": "001"},
    "대구": {"name": "대구", "code": "002"},
    "인천": {"name": "인천", "code": "003"},
    "광주": {"name": "광주", "code": "004"},
    "대전": {"name": "대전", "code": "005"},
    "울산": {"name": "울산", "code": "006"},
}