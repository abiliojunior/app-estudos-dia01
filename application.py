from flask import Flask, render_template
from flask_cors import CORS

application = Flask(__name__)

@application.route('/')
def main():
    return render_template('index.html')