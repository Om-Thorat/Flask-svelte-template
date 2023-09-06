from flask import Flask, send_from_directory, request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def root():
    return send_from_directory('./client/dist', 'index.html')

@app.route('/<path:path>')
def assets(path):
    return send_from_directory('./client/dist',path)

@app.route('/time')
def gettime():
    return str(datetime.now().strftime("%H:%M:%S"))

if __name__ == "__main__":
    app.run(debug=True)