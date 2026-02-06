import requests
from create_token import get_nhn_token  # 모듈 임포트

print("본인 인스턴스, 서브넷이 있어야합니다.")

# Step 1: 토큰 발급 (모듈 사용)
token_id = get_nhn_token()

if token_id is None:
    print("토큰 발급 실패. 프로그램을 종료합니다.")
    exit(1)

# Step 2: LB 생성
LB_url = "https://kr1-api-network-infrastructure.nhncloudservice.com"  
LB_uri = "/v2.0/lbaas/loadbalancers"
header = {
    "X-Auth-Token": token_id
}

subnet_id = input("서브넷 아이디를 입력하세요: ")
LB_name = input("LB이름을 입력하세요: ")

LB_body = {
    "loadbalancer": {
        "name": LB_name,
        "vip_subnet_id": subnet_id
    } 
}

res = requests.post(LB_url + LB_uri, headers=header, json=LB_body)

if res.status_code == 201:
    LB_id = res.json()['loadbalancer']['id']
    print(f" LB 생성 완료! ID: {LB_id}")
else:
    print(f" LB 생성 실패: {res.text}")
    exit(1)

# Step 3: 리스너 생성
Lstn_url = "https://kr1-api-network-infrastructure.nhncloudservice.com"
Lstn_uri = "/v2.0/lbaas/listeners"

lister_name = input("리스너 이름을 입력하세요: ")

Lstn_body = {
    "listener": {
        "protocol": "TCP",
        "name": lister_name,
        "loadbalancer_id": LB_id,
        "connection_limit": 2000,
        "keepalive_timeout": 300,
        "protocol_port": 8000
    }
}

res = requests.post(Lstn_url + Lstn_uri, headers=header, json=Lstn_body)

if res.status_code == 201:
    listener_id = res.json()['listener']['id']
    print(f" 리스너 생성 완료! 리스너 ID: {listener_id}")
else:
    print(f" 리스너 생성 실패: {res.text}")