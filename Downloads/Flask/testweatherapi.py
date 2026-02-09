"""
고속도로 휴게소 날씨 API 테스트 스크립트 (HTTPS)
"""

import requests
import urllib3
from datetime import datetime

# SSL 경고 비활성화
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# API 설정
API_URL = "https://data.ex.co.kr/openapi/restinfo/restWeatherList"
API_KEY = "1663676750"

# 현재 시간
now = datetime.now()
sdate = now.strftime('%Y%m%d')  # 예: 20260209

# 현재 시각의 이전 정시 사용
current_hour = now.hour
if now.minute < 10:  # 정시 데이터가 아직 업데이트 안 되었을 수 있음
    stdHour = f"{current_hour - 1:02d}"  # 1시간 전
else:
    stdHour = f"{current_hour:02d}"  # 현재 시각

print("=" * 60)
print("고속도로 휴게소 날씨 API 테스트")
print("=" * 60)
print(f"API URL: {API_URL}")
print(f"API KEY: {API_KEY}")
print(f"날짜: {sdate}")
print(f"시간: {stdHour}시")
print(f"현재 시각: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 60)

# 파라미터 설정
params = {
    "key": API_KEY,
    "type": "json",
    "sdate": sdate,
    "stdHour": stdHour
}

print("\n요청 파라미터:")
for key, value in params.items():
    print(f"  {key}: {value}")

try:
    print("\nAPI 호출 중... (HTTPS, SSL 검증 우회)")
    response = requests.get(API_URL, params=params, timeout=10, verify=False)
    
    print(f"응답 상태 코드: {response.status_code}")
    
    if response.status_code == 200:
        print("\n✅ API 호출 성공!")
        
        # JSON 응답 파싱
        data = response.json()
        
        print("\n전체 응답 데이터:")
        print("-" * 60)
        import json
        print(json.dumps(data, indent=2, ensure_ascii=False))
        print("-" * 60)
        
        # 데이터 추출
        if 'list' in data:
            items = data['list']
            print(f"\n총 {len(items)}개의 데이터 조회됨")
            
            if len(items) > 0:
                print("\n첫 번째 데이터:")
                first_item = items[0]
                
                print(f"  휴게소명: {first_item.get('unitName', '정보없음')}")
                print(f"  기온: {first_item.get('airTemperature', '--')}°C")
                print(f"  습도: {first_item.get('humidity', '--')}%")
                print(f"  풍속: {first_item.get('windSpeed', '--')} m/s")
                print(f"  강수량: {first_item.get('rainfall', '0')} mm")
                print(f"  날씨: {first_item.get('weather', '정보없음')}")
                
                print("\n✅ 테스트 성공! 날씨 데이터를 정상적으로 받아왔습니다.")
            else:
                print("\n⚠️ 날씨 데이터가 비어있습니다.")
        else:
            print("\n⚠️ 응답에 'list' 키가 없습니다.")
            print("응답 구조 확인 필요")
    else:
        print(f"\n❌ API 호출 실패 (상태 코드: {response.status_code})")
        print("응답 내용:", response.text)

except requests.exceptions.Timeout:
    print("\n❌ 요청 시간 초과")
    
except requests.exceptions.RequestException as e:
    print(f"\n❌ 요청 오류: {e}")
    
except Exception as e:
    print(f"\n❌ 오류 발생: {e}")

print("\n" + "=" * 60)
print("테스트 완료")
print("=" * 60)