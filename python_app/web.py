# -*- encoding: utf-8 -*-
import socket

from flask import Flask, jsonify

application = Flask(__name__)

@application.route("/")
def home():
    local_ip = socket.gethostbyname(socket.gethostname())

    return jsonify(ip=local_ip)

if __name__ == "__main__":
    application.run()

