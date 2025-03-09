from flask import jsonify

from flask import Flask, Response, render_template
from picamera2 import Picamera2
import cv2

app = Flask(__name__)

# Initialize the camera
camera = Picamera2()
camera.configure(camera.create_preview_configuration(
    main={"format": 'XRGB8888', "size": (640, 480)}))
camera.start()


def generate_frames():
    while True:
        frame = camera.capture_array()  # Capture the frame from the camera
        # Encode the frame in JPEG format
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/temp')
def temp():
    return jsonify({"msg": "hello"})


if __name__ == '__main__':
    try:
        # app.run(host='0.0.0.0', port=5000, debug=True)
        app.run(host='0.0.0.0', port=5000)
    finally:
        camera.close()  # Release the camera when the app is stopped
