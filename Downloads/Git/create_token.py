import requests

def get_nhn_token(tenant_id=None, username=None, password=None):
    """
    NHN Cloud 인증 토큰을 발급받는 함수
    
    Args:
        tenant_id: 테넌트 ID (None이면 입력 요청)
        username: 사용자명 (None이면 입력 요청)
        password: 비밀번호 (None이면 입력 요청)
    
    Returns:
        str: 발급받은 토큰 ID
    """
    # 파라미터가 없으면 사용자 입력 받기
    if tenant_id is None:
        tenant_id = input("tenantID 입력: ")
    if username is None:
        username = input("username 입력: ")
    if password is None:
        password = input("비밀번호를 입력하세요: ")
    
    # 토큰 발급 요청
    url = "https://api-identity-infrastructure.nhncloudservice.com"
    uri = "/v2.0/tokens"
    
    body = {
        "auth": {
            "tenantId": tenant_id,
            "passwordCredentials": {
                "username": username,
                "password": password
            }
        }
    }
    
    try:
        response = requests.post(url + uri, json=body)
        response.raise_for_status()  # HTTP 에러 체크
        
        token_id = response.json()['access']['token']['id']
        print(f"✓ 토큰 발급 성공!")
        return token_id
        
    except requests.exceptions.RequestException as e:
        print(f"✗ API 요청 실패: {e}")
        return None
    except KeyError as e:
        print(f"✗ 토큰 추출 실패: {e}")
        print(f"응답 내용: {response.text}")
        return None