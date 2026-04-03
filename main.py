from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/ff', methods=['GET'])
def get_ff_info():
    uid = request.args.get('id')
    if not uid:
        return jsonify({"status": "error", "message": "Vui lòng nhập ID"}), 400
    
    # API nguồn (Lấy dữ liệu thật)
    api_url = f"https://freefire-api-five.vercel.app/api/info?id={uid}"
    
    try:
        response = requests.get(api_url, timeout=10)
        data = response.json()
        # Trả về kết quả cho bạn
        return jsonify(data)
    except Exception as e:
        return jsonify({
            "status": "error", 
            "message": "Không thể lấy dữ liệu",
            "detail": str(e)
        }), 500

@app.route('/')
def home():
    return "API FF cua ban dang hoat dong! Hay dung: /api/ff?id=SO_ID"

if __name__ == '__main__':
    app.run(debug=True)

