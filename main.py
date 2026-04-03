from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/ff', methods=['GET'])
def get_info():
    uid = request.args.get('id')
    if not uid:
        return jsonify({"status": "error", "message": "Thieu ID"}), 400
    
    # Xóa khoảng trắng nếu có
    uid = uid.strip()
    
    # Nguồn API quốc tế ổn định hơn
    url = f"https://freefireapi.com.br/api/search_id?id={uid}"
    
    try:
        # Giả lập trình duyệt để tránh bị chặn
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        data = res.json()
        
        # Nếu có dữ liệu trả về
        if "nickname" in data or "name" in data:
            return jsonify({
                "status": "success",
                "nickname": data.get("nickname") or data.get("name"),
                "id": uid,
                "level": data.get("level", "N/A")
            })
        else:
            return jsonify({"status": "error", "message": "ID khong ton tai"}), 404
            
    except:
        return jsonify({"status": "error", "message": "Server dang bao tri"}), 500

@app.route('/')
def home():
    return "API FF ONLINE - Dung: /api/ff?id=SO_ID"

if __name__ == '__main__':
    app.run()

