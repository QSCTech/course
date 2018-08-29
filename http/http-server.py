from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify({'name': 'qsc', 'words': 'hello'})


if __name__ == '__main__':
    app.run(port=8000)
