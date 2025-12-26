from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to the Python App!',
        'status': 'success'
    })

@app.route('/api/hello')
def hello():
    return jsonify({
        'message': 'Hello, World!',
        'status': 'success'
    })

if __name__ == '__main__':
    # For development only. In production, use a WSGI server like gunicorn
    app.run(debug=True, host='0.0.0.0', port=5000)
