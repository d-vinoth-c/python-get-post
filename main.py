from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello from Flask in Cloud Function!', 200

@app.route('/echo', methods=['POST'])
def echo():
    if request.is_json:
        data = request.get_json()
        return jsonify({
            'received': data
        }), 200
    else:
        return jsonify({'error': 'Request must be JSON'}), 400

# Required by Google Cloud Functions
def main(request):
    return app(request, start_response=_start_response)
