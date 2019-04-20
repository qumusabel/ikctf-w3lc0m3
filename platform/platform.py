import os
from flask import Flask, flash, get_flashed_messages, url_for, session, redirect, render_template, request, make_response
import click
import json

app = Flask(__name__)
app.secret_key = os.urandom(16)


class Task:
    def __init__(self, dict):
        self.category = dict['category']
        self.points = dict['points']
        self.title = dict['title']
        self.desc = dict['desc']
        self.files = dict['files'].split()
        self.flag = dict['flag']
        self.solved = False

    def get_id(self):
        return "{}-{}".format(self.category, self.points)

    def check_flag(self, flag):
        self.solved = self.solved or self.flag == flag
        return self.solved


tasks = [Task(i) for i in json.loads(open('tasks.json').read())]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id, flag = request.form['id'], request.form['flag']

        task = [i for i in tasks if i.get_id() == id]
        if len(task) != 1:
            return make_response(render_template('400.html'), 400)

        task = task[0]
        if task.get_id() not in session['solved']:
            if task.check_flag(flag):
                session['solved'].append(task.get_id())
                session['points'] += task.points
            else:
                flash('Неверный флаг!')

        return redirect(url_for('index'))

    else:
        if 'solved' not in session:
            session['solved'] = []
        if 'points' not in session:
            session['points'] = 0
        return render_template('index.html', tasks=tasks, session=session)


if __name__ == '__main__':
    app.run(port='8080', extra_files='templates/index.html')

