from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/ff', methods=['GET'])
def get_ff_info():
    uid = request.args.get('id')
    if not uid:
        return jsonify({"status": "error", "message": "Vui lòng nhập ID"}), 400
    
    # Sử dụng nguồn API dự phòng khác
    url = f"https://api.vinh09.com/ff/info?id={uid}"
    
    try:
        response = requests.get(url, timeout=15)
        # Nếu nguồn này trả về JSON trực tiếp
        return jsonify(response.json())
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Nguồn dữ liệu đang bận, thử lại sau",
            "id": uid
        }), 500

@app.route('/')
def home():
    return "API FF Online! Dung: /api/ff?id=SO_ID"

