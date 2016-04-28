# -*- encoding: utf-8 -*-
import socket

from flask import Flask, jsonify
from datetime import datetime

application = Flask(__name__)

@application.route("/")
def home():
    local_ip = socket.gethostbyname(socket.gethostname())
    print "a"

    return jsonify(ip=local_ip)
@application.route("/ping")
def ping():
    return jsonify(time=datetime.now().isoformat())


if __name__ == "__main__":
    application.run(debug=True)

