import os
from urllib import request
from flask import Flask, jsonify, request, render_template
from flask import send_from_directory ,url_for
from flask_bootstrap import Bootstrap
from ydl import ydl



web = Flask(__name__)

bootstrap = Bootstrap(web)

# Index
@web.route('/')
def index():
    return render_template('index.html')

# @web.route('/favicon.ico')
# def favicon():
#     web.add_url_rule('/favicon.ico',
#                  redirect_to=url_for('static', filename='https://avatars.githubusercontent.com/u/25699289?v=4'))

@web.route('/ydl')
def _utubedl():
    _yt_url = request.args.get('url')
    return jsonify(ydl(_yt_url))

# 404


@web.errorhandler(404)
def _not_found(e):
    return "404"


if __name__ == "__main__":
    web.run(debug=True)
