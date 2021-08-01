from flask import Flask


web = Flask(__name__)

@web.route('/')
def indexPage():
    return "hi"

if __name__ == "__main__":
    web.run(debug=True)