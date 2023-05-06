from flask import Flask, request, jsonify
from grove_rgb_lcd import *
import grovepi
import time


app = Flask(__name__)
grovepi.set_bus("RPI_1")




@app.route('/success', methods=['GET'])
def success():
    setRGB(0,255,0)
    return jsonify({'response': 'success'})

@app.route('/post', methods=['POST'])
def post():
    message = request.get_json()
    print(message)
    setRGB(160,30,240)
    setText(f"{message['message']}")
    time.sleep(4)
    setText("")
    setRGB(100,100,100)
    res = jsonify("hi")
    res.status_code = 201
    return res

if __name__ == '__main__':
    setRGB(100,100,100)
    setText("")
    app.run(debug=True, port=5000, host='0.0.0.0')
