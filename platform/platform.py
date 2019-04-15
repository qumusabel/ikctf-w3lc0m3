import os
from flask import Flask
import click

app = Flask(__name__)





@app.route('/')
def index():
    pass


if __name__ == '__main__':
    # app.config['TASKS_PATH'] = os.path.join(os.path.dirname())
    app.secret_key = os.urandom(16)
    app.run()
