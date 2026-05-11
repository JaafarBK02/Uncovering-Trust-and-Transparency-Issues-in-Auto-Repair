import os
from flask import Flask, make_response, jsonify
from google.cloud import storage

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    response = make_response(app.send_static_file('index.html'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate'
    return response

@app.route('/api/data-info')
def data_info():
    client = storage.Client()
    bucket = client.bucket('auto-repair-reviews')
    blob = bucket.blob('reviews_clean.csv')
    return jsonify({
        'file': 'reviews_clean.csv',
        'size_bytes': blob.size,
        'updated': str(blob.updated),
        'location': 'gs://auto-repair-reviews/reviews_clean.csv'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
