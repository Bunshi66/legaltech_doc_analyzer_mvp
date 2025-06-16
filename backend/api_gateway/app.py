from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    """
    Простейший эндпоинт для проверки работоспособности сервиса.
    """
    return jsonify({"status": "ok", "service": "api-gateway"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)