from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/ff', methods=['GET'])
def get_info():
    uid = request.args.get('id')
    if not uid:
        return jsonify({"status": "error", "message": "Thiếu ID"}), 400
    
    # Sử dụng nguồn API cộng đồng thường xuyên được cập nhật
    url = f"https://api.vinh09.com/ff/info?id={uid}"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({
                "status": "error", 
                "message": "ID không tồn tại hoặc nguồn dữ liệu đang bận"
            }), 404
    except Exception as e:
        return jsonify({"status": "error", "message": "Lỗi kết nối", "detail": str(e)}), 500

@app.route('/')
def home():
    return "<h1>API Free Fire Online</h1><p>Cách dùng: /api/ff?id=SO_ID</p>"

if __name__ == '__main__':
    app.run()

