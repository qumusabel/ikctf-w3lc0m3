#!../.env/bin/python

import os
from flask import Flask, abort, flash, url_for, session, redirect, render_template, request, \
                    make_response, send_from_directory
import json


class Task:
    def __init__(self, dict):
        self.category = dict['category']
        self.points = dict['points']
        self.title = dict['title']
        self.desc = dict['desc']
        self.files = dict['files'].split()
        self.flag = dict['flag']
        self.solutions = 0

    def get_id(self):
        return "{}-{}".format(self.category, self.points)

    def check_flag(self, flag):
        return flag == self.flag


app = Flask(__name__)
app.secret_key = os.urandom(16)
app.config['TASKS_DIR'] = os.path.join(os.path.dirname(os.getcwd()), 'tasks')
tasks = [Task(i) for i in json.loads(open(os.path.join(app.config['TASKS_DIR'], 'tasks.json'), encoding='utf-8').read())]


@app.route('/task/<task_id>/<file>')
def deploy(task_id, file):
    task = [i for i in tasks if i.get_id() == task_id]

    task = task[0]
    if file in task.files:
        return send_from_directory(os.path.join(app.config['TASKS_DIR'], task.get_id(), 'deploy'), file)
    else:
        abort(404)


@app.errorhandler(400)
@app.errorhandler(404)
def error(code):
    return render_template('error.html')


# MAIN PLATFORM
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_id, flag = request.form['id'], request.form['flag']

        task = [i for i in tasks if i.get_id() == task_id]
        if len(task) != 1:
            abort(400)
        task = task[0]

        if task.get_id() not in session['solved']:
            if task.check_flag(flag):
                session['solved'].append(task.get_id())
                session['points'] += task.points
                task.solutions += 1
            else:
                flash('Неверный флаг!')

        return redirect(url_for('index'))

    else:
        if 'solved' not in session:
            session['solved'] = []
        if 'points' not in session:
            session['points'] = 0
        return render_template('index.html', tasks=tasks, session=session, host=request.host)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')
