from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "API cua ban dang hoat dong!"

@app.route('/api/ff')
def get_info():
    uid = request.args.get('id')
    # Cho nay ban se dan code lay thong tin FF vao sau
    return jsonify({"id": uid, "name": "Nhan Vat Mau", "level": 99})

app = app # Dong nay de Vercel hieu day la ung dung Flask

