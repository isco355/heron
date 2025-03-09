from flask import Flask, jsonify
from helpers.coordinates import currentCoordinates
import subprocess
app = Flask(__name__)

subprocess.Popen(["sudo", "python3", "./helpers/livestream/camera.py", " &"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/status")
def handle_status():
    current_status = currentCoordinates()
    return jsonify(current_status)


@app.route('/gate')
def handle_gate():
    print('set gate')
    return 'gate'
