from flask import Flask, send_from_directory, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response(send_from_directory('.', 'index.html'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)