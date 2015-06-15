# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template, jsonify
from random import randint

from teensyserial import TeensySerial
teensy_board = TeensySerial(115200)

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_temp():
    temperature = float(teensy_board.recv())
    return jsonify(temperature=temperature)

@app.route('/')
def termo_flask():
    return render_template('termo_flask.html', teensy_port=teensy_board.get_port())

if __name__ == '__main__':
    app.run()
    teensy_board.finish()
