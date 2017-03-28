# -*- encoding: utf-8 -*-
from datetime import datetime
import os
import socket
from flask import Flask, jsonify
import redis

application = Flask(__name__)
redis_conn = redis.from_url(os.environ.get('REDIS_URL'))


@application.route("/")
def home():
    local_ip = socket.gethostbyname(socket.gethostname())
    redis_conn.incr('API_COUNTER')
    return jsonify(ip=local_ip, counter=redis_conn.get('API_COUNTER'))


@application.route("/ping")
def ping():
    return jsonify(time=datetime.now().isoformat())


if __name__ == "__main__":
    application.run(debug=True)
