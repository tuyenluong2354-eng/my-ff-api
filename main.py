from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/ff', methods=['GET'])
def get_info():
    uid = request.args.get('id')
    if not uid:
        return jsonify({"status": "error", "message": "Thiếu ID"}), 400
    
    # Kết nối tới nguồn ffhx.in
    # Lưu ý: Đây là link giả lập endpoint của ffhx, bạn có thể cần điều chỉnh link chuẩn của họ
    url = f"https://ffhx.in/api/info?id={uid}" 
    
    try:
        response = requests.get(url, timeout=10)
        # Trả về kết quả từ ffhx.in cho người dùng của bạn
        return jsonify(response.json())
    except:
        return jsonify({
            "status": "error",
            "message": "Không thể lấy dữ liệu từ ffhx.in",
            "id": uid
        }), 500

@app.route('/')
def home():
    return "API FF đang chạy nguồn ffhx.in"

if __name__ == '__main__':
    app.run()

