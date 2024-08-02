from flask import render_template, Flask, request

app = Flask(__name__)


@app.route('/')


def index():
    return "hello World"