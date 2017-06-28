#!/usr/bin/python
# -*- coding: UTF-8 -*-
# encoding: utf-8

from flask import Flask
from redis import Redis
from redis import RedisError
import os
import socket

###Conexión a REDis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hola():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>No es posible conectarse a REDIS</i>"
        html ="<h1>Hi {name}!</h1>"\
                "<b>Hostname:</b> {hostname}<br/>"\
                "<b>Visits:</b>{visits}"
    return html.format(name=os.getenv("NAME", "mundo"),
                       hostname=socket.gethostname(), visits= visits)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=80)

