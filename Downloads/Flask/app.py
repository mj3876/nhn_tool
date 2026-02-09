from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime, timedelta
import json
import os
import requests
from config import WEATHER_API_KEY, WEATHER_API_URL, REST_AREAS

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# 데이터 저장 경로
DATA_DIR = 'data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# 데이터 파일 경로
DIARY_FILE = os.path.join(DATA_DIR, 'diary.json')
BOOKS_FILE = os.path.join(DATA_DIR, 'books.json')
MESSAGES_FILE = os.path.join(DATA_DIR, 'messages.json')
TODOS_FILE = os.path.join(DATA_DIR, 'todos.json')

# 데이터 로드 함수
def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# 데이터 저장 함수
def save_data(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 메인 페이지
@app.route('/')
def index():
    today = datetime.now().strftime('%Y-%m-%d')
    return render_template('index.html', today=today)

# 일상 기록
@app.route('/diary')
def diary():
    diaries = load_data(DIARY_FILE)
    return render_template('diary.html', diaries=diaries)

@app.route('/diary/write', methods=['GET', 'POST'])
def diary_write():
    if request.method == 'POST':
        diaries = load_data(DIARY_FILE)
        
        new_diary = {
            'id': len(diaries) + 1,
            'date': request.form.get('date'),
            'mood': request.form.get('mood'),
            'hard_thing': request.form.get('hard_thing'),
            'good_thing': request.form.get('good_thing'),
            'content': request.form.get('content'),
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        diaries.insert(0, new_diary)
    
        save_data(DIARY_FILE, diaries)
        
        return redirect(url_for('diary'))
    today = datetime.now().strftime('%Y-%m-%d')
    return render_template('diary_write.html',today=today)

@app.route('/diary/view/<int:diary_id>')
def diary_view(diary_id):
    diaries = load_data(DIARY_FILE)
    diary = next((d for d in diaries if d['id'] == diary_id), None)
    return render_template('diary_view.html', diary=diary)

@app.route('/diary/delete/<int:diary_id>')
def diary_delete(diary_id):
    diaries = load_data(DIARY_FILE)
    diaries = [d for d in diaries if d['id'] != diary_id]
    save_data(DIARY_FILE, diaries)
    return redirect(url_for('diary'))

# 독서 메모
@app.route('/books')
def books():
    books = load_data(BOOKS_FILE)
    return render_template('books.html', books=books)

@app.route('/books/add', methods=['GET', 'POST'])
def books_add():
    if request.method == 'POST':
        books = load_data(BOOKS_FILE)
        
        new_book = {
            'id': len(books) + 1,
            'title': request.form.get('title'),
            'author': request.form.get('author'),
            'status': request.form.get('status'),
            'memo': request.form.get('memo'),
            'rating': request.form.get('rating'),
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        books.insert(0, new_book)
        save_data(BOOKS_FILE, books)
        
        return redirect(url_for('books'))
    
    return render_template('books_add.html')

@app.route('/books/delete/<int:book_id>')
def books_delete(book_id):
    books = load_data(BOOKS_FILE)
    books = [b for b in books if b['id'] != book_id]
    save_data(BOOKS_FILE, books)
    return redirect(url_for('books'))

# 위로/응원 메시지
@app.route('/messages')
def messages():
    import random
    messages = load_data(MESSAGES_FILE)
    
    # 기본 메시지 15개
    default_messages = [
        {"category": "응원", "content": "오늘도 최선을 다한 당신, 정말 멋져요! 💪"},
        {"category": "위로", "content": "힘든 하루였나요? 괜찮아요, 내일은 더 나을 거예요 🌈"},
        {"category": "격려", "content": "한 걸음씩 나아가는 중이에요. 포기하지 마세요! ✨"},
        {"category": "감사", "content": "오늘도 살아있고, 숨 쉬고 있다는 것에 감사해요 🙏"},
        {"category": "응원", "content": "당신은 생각보다 훨씬 강한 사람이에요! 🌟"},
        {"category": "위로", "content": "완벽하지 않아도 괜찮아요. 지금 그대로도 충분해요 💕"},
        {"category": "격려", "content": "작은 진전도 진전이에요. 자신을 칭찬해주세요! 👏"},
        {"category": "응원", "content": "넘어져도 다시 일어서는 당신이 자랑스러워요 🦋"},
        {"category": "감사", "content": "오늘 하루도 열심히 살아준 나 자신에게 고마워요 💝"},
        {"category": "위로", "content": "모든 게 완벽할 필요는 없어요. 쉬어가도 돼요 🌙"},
        {"category": "격려", "content": "실패는 성공의 어머니! 다시 도전해봐요! 🚀"},
        {"category": "응원", "content": "당신의 노력을 세상이 모를 수 있어도, 당신은 알고 있어요 ⭐"},
        {"category": "위로", "content": "지금 힘들어도, 이것 역시 지나갈 거예요 🌸"},
        {"category": "감사", "content": "작은 것에도 감사할 줄 아는 당신이 아름다워요 🌺"},
        {"category": "응원", "content": "오늘 하루를 버텨낸 것만으로도 대단해요! 🎉"},
        {"category": "위로", "content": "힘들 땐 쉬어가도 괜찮아요. 당신은 충분히 잘하고 있어요 🌻"},
        {"category": "격려", "content": "느린 걸음도 앞으로 가는 걸음이에요. 계속 나아가요! 🚶"},
        {"category": "응원", "content": "오늘의 당신에게 박수를 보냅니다! 👏"},
        {"category": "감사", "content": "지금 이 순간, 여기에 있어주셔서 감사해요 🌟"},
        {"category": "격려", "content": "어제보다 나은 오늘을 살고 있는 당신이 대단해요! 💫"}
    ]
        
    
    # 모든 메시지 합치기
    all_messages = messages + default_messages
    
    # Python에서 랜덤 선택
    random_message = random.choice(all_messages)
    
    # 템플릿에 전달
    return render_template('messages.html', messages=messages, random_message=random_message)

@app.route('/messages/add', methods=['POST'])
def messages_add():
    messages = load_data(MESSAGES_FILE)
    
    new_message = {
        'id': len(messages) + 1,
        'content': request.form.get('content'),
        'category': request.form.get('category'),
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    messages.insert(0, new_message)
    save_data(MESSAGES_FILE, messages)
    
    return redirect(url_for('messages'))

@app.route('/messages/random')
def messages_random():
    import random
    messages = load_data(MESSAGES_FILE)
    if messages:
        message = random.choice(messages)
        return jsonify(message)
    return jsonify({'content': '오늘도 힘내세요! 💪'})

@app.route('/messages/delete/<int:message_id>')
def messages_delete(message_id):
    messages = load_data(MESSAGES_FILE)
    messages = [m for m in messages if m['id'] != message_id]
    save_data(MESSAGES_FILE, messages)
    return redirect(url_for('messages'))

# 캘린더 & 할일 목록

@app.route('/todos')
def todos():
    todos = load_data(TODOS_FILE)
    return render_template('todos.html', todos=todos)

@app.route('/todos/add', methods=['POST'])
def todos_add():
    todos = load_data(TODOS_FILE)
    
    new_todo = {
        'id': len(todos) + 1,
        'title': request.form.get('title'),
        'date': request.form.get('date'),
        'time': request.form.get('time'),
        'type': request.form.get('type'),  # daily or monthly
        'completed': False,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    todos.insert(0, new_todo)
    save_data(TODOS_FILE, todos)
    
    return redirect(url_for('todos'))

@app.route('/todos/toggle/<int:todo_id>')
def todos_toggle(todo_id):
    todos = load_data(TODOS_FILE)
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = not todo['completed']
            break
    save_data(TODOS_FILE, todos)
    return redirect(url_for('todos'))

@app.route('/todos/delete/<int:todo_id>')
def todos_delete(todo_id):
    todos = load_data(TODOS_FILE)
    todos = [t for t in todos if t['id'] != todo_id]
    save_data(TODOS_FILE, todos)
    return redirect(url_for('todos'))

# API - 오늘의 할일 가져오기
@app.route('/api/todos/today')
def api_todos_today():
    todos = load_data(TODOS_FILE)
    today = datetime.now().strftime('%Y-%m-%d')
    today_todos = [t for t in todos if t['date'] == today]
    return jsonify(today_todos)

# API - 이번 달 할일 가져오기
@app.route('/api/todos/month/<year>/<month>')
def api_todos_month(year, month):
    todos = load_data(TODOS_FILE)
    month_todos = [t for t in todos if t['date'].startswith(f'{year}-{month.zfill(2)}')]
    return jsonify(month_todos)

# 날씨 페이지
@app.route('/weather')
def weather():
    cities = ["전국"]  # 고속도로 날씨는 전국 단위
    return render_template('weather.html', cities=cities)

# 날씨 API (고속도로 휴게소 날씨 데이터)
@app.route('/api/weather')
def get_weather():
    try:
        # 현재 시간 기준
        now = datetime.now()
        target_date = datetime(2025, now.month, now.day)
        sdate = now.strftime('%Y%m%d')  # YYYYMMDD
        stdHour = now.strftime('%H')     # HH
        
        # API 파라미터 설정
        params = {
            "key": WEATHER_API_KEY,
            "type": "json",
            "sdate": sdate,
            "stdHour": stdHour
        }
        
        # 고속도로 날씨 API 호출 (HTTPS, SSL 검증 우회)
        response = requests.get(WEATHER_API_URL, params=params, timeout=10, verify=False)
        
        if response.status_code == 200:
            data = response.json()
            
            # 응답 확인
            if 'list' in data:
                items = data['list']
                
                if len(items) > 0:
                    # 첫 번째 데이터 사용 (또는 평균값 계산)
                    first_item = items[0]
                    
                    # 데이터 파싱
                    weather_data = {
                        'temperature': first_item.get('airTemperature', '--'),  # 기온
                        'humidity': first_item.get('humidity', '--'),           # 습도
                        'wind_speed': first_item.get('windSpeed', '--'),        # 풍속
                        'rainfall': first_item.get('rainfall', '0'),            # 강수량
                        'rest_area': first_item.get('unitName', '전국'),       # 휴게소명
                        'weather': first_item.get('weather', '정보없음'),      # 날씨
                        'update_time': f"{sdate[:4]}-{sdate[4:6]}-{sdate[6:8]} {stdHour}:00"
                    }
                    
                    # 날씨 상태 및 아이콘 판단
                    weather_text = weather_data['weather'].lower()
                    if '비' in weather_text or 'rain' in weather_text:
                        weather_data['icon'] = '🌧️'
                        weather_data['status'] = '비'
                    elif '눈' in weather_text or 'snow' in weather_text:
                        weather_data['icon'] = '❄️'
                        weather_data['status'] = '눈'
                    elif '흐림' in weather_text or 'cloud' in weather_text:
                        weather_data['icon'] = '☁️'
                        weather_data['status'] = '흐림'
                    else:
                        weather_data['icon'] = '☀️'
                        weather_data['status'] = '맑음'
                    
                    # 기온이 숫자인지 확인
                    try:
                        temp = float(weather_data['temperature'])
                        weather_data['temperature'] = temp
                    except:
                        weather_data['temperature'] = 0
                    
                    # 습도가 숫자인지 확인
                    try:
                        humidity = int(weather_data['humidity'])
                        weather_data['humidity'] = humidity
                    except:
                        weather_data['humidity'] = 0
                    
                    # 풍속이 숫자인지 확인
                    try:
                        wind_speed = float(weather_data['wind_speed'])
                        weather_data['wind_speed'] = wind_speed
                    except:
                        weather_data['wind_speed'] = 0
                    
                    return jsonify(weather_data)
                else:
                    return jsonify({"error": "날씨 데이터가 없습니다"}), 404
            else:
                return jsonify({"error": "API 응답 형식 오류"}), 500
        else:
            return jsonify({"error": f"API 서버 응답 오류 (상태 코드: {response.status_code})"}), 500
            
    except requests.exceptions.Timeout:
        return jsonify({"error": "API 요청 시간 초과"}), 504
    except Exception as e:
        return jsonify({"error": f"서버 오류: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)