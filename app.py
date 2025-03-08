from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=False)


@app.route("/status")
def handle_status():
    return jsonify({'name': 'test'})


@app.route('/gate')
def handle_gate():
    print('set gate')
    return 'gate'
