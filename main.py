from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/ff', methods=['GET'])
def get_ff_info():
    uid = request.args.get('id')
    if not uid:
        return jsonify({"status": "error", "message": "Vui lòng nhập ID"}), 400
    
    # Nguồn check ID Free Fire cực chuẩn của Garena (Napthe.vn)
    url = "https://id.game.garena.vn/api/login/get_player_info"
    payload = {
        "app_id": 100067,
        "player_id": uid
    }
    
    try:
        # Gửi yêu cầu lấy tên thật
        response = requests.post(url, json=payload, timeout=10)
        data = response.json()
        
        if "nickname" in data:
            return jsonify({
                "status": "success",
                "id": uid,
                "nickname": data["nickname"],
                "region": "VN"
            })
        else:
            return jsonify({"status": "error", "message": "ID không tồn tại"}), 404
            
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/')
def home():
    return "API FF Online! Dung: /api/ff?id=SO_ID"

