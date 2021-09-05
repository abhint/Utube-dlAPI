import os
from urllib import request
from flask import Flask, jsonify, request, render_template
from flask import send_from_directory, url_for
from flask_bootstrap import Bootstrap
from ydl import ydl


web = Flask(__name__)

Bootstrap(web)


@web.route('/')
def index():
    return render_template('index.html')


@web.route('/ydl', methods=["POST"])
def _utubedl():
    _yt_url = request.form['url']
    return jsonify(ydl(_yt_url))


@web.errorhandler(404)
def _not_found(e):
    return "404"


if __name__ == "__main__":
    web.run(host='0.0.0.0', port=os.environ.get(
        "PORT"), use_reloader=True, threaded=True)
