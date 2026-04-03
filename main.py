from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/ff', methods=['GET'])
def get_ff_info():
    uid = request.args.get('id')
    if not uid:
        return jsonify({"status": "error", "message": "Vui lòng nhập ID"}), 400
    
    # Sử dụng nguồn API Free Fire dự phòng có độ ổn định cao
    url = f"https://freefire-api-five.vercel.app/api/info?id={uid}"
    
    try:
        # Giả lập trình duyệt để tránh bị chặn
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        
        # Kiểm tra xem có phải JSON không trước khi xử lý
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"status": "error", "message": "ID không tồn tại hoặc lỗi nguồn"}), 404
            
    except Exception as e:
        return jsonify({"status": "error", "message": "Nguồn dữ liệu đang bảo trì"}), 500

@app.route('/')
def home():
    return "API FF đang chạy! Dùng: /api/ff?id=SO_ID"

if __name__ == '__main__':
    app.run()

