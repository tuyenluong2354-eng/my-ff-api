from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/ff', methods=['GET'])
def get_info():
    uid = request.args.get('id')
    if not uid:
        return jsonify({"status": "error", "message": "Thiếu ID"}), 400
    
    # Tự động xóa dấu cách dư thừa nếu bạn lỡ tay nhập nhầm
    uid = uid.strip()
    
    # Danh sách các nguồn dự phòng (Thử nguồn 1 lỗi sẽ nhảy sang nguồn 2)
    sources = [
        f"https://ffhx.in/api/api.php?uid={uid}",
        f"https://freefireapi.com.br/api/search_id?id={uid}"
    ]
    
    for url in sources:
        try:
            res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
            data = res.json()
            # Kiểm tra nếu lấy được tên nhân vật
            nick = data.get("name") or data.get("nickname")
            if nick:
                return jsonify({
                    "status": "thành công",
                    "nickname": nick,
                    "level": data.get("level", "??"),
                    "id": uid
                })
        except:
            continue # Thử nguồn tiếp theo nếu nguồn này lỗi
            
    return jsonify({"status": "lỗi", "message": "Tất cả nguồn dữ liệu đang bận hoặc ID sai"}), 404

@app.route('/')
def home():
    return "API FF đang chạy (Đã sửa lỗi DNS)"

