from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/ff', methods=['GET'])
def get_ff_info():
    uid = request.args.get('id')
    if not uid:
        return jsonify({"status": "error", "message": "Vui lòng nhập ID"}), 400
    
    # Nguồn lấy dữ liệu từ hệ thống ffhx.in
    url = f"https://ffhx.in/api/api.php?uid={uid}"
    
    try:
        # Gửi yêu cầu với Header để giả lập trình duyệt
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()
        
        # Nếu lấy thành công dữ liệu từ ffhx
        if "name" in data or "nickname" in data:
            return jsonify({
                "status": "success",
                "nickname": data.get("name") or data.get("nickname"),
                "level": data.get("level", "N/A"),
                "last_login": data.get("lastlogin", "N/A"),
                "uid": uid,
                "source": "ffhx.in"
            })
        else:
            return jsonify({"status": "error", "message": "ID không hợp lệ hoặc không có dữ liệu"}), 404
            
    except Exception as e:
        return jsonify({"status": "error", "message": "Nguồn ffhx đang bận", "detail": str(e)}), 500

@app.route('/')
def home():
    return "API FF đang chạy nguồn FFHX! Dùng: /api/ff?id=SO_ID"

if __name__ == '__main__':
    app.run()

