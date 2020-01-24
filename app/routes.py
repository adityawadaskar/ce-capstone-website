from app import app
from flask import render_template
from app.models import Student, Project, Sponsor

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/schedule')
def schedule():
    return render_template('index.html')

@app.route('/projects')
def projects():
    project = Project.query.all()
    return render_template('index.html')

@app.route('/resources')
def resources():
    return render_template('index.html')

@app.route('/sponsors')
def sponsors():
    return render_template('index.html')

@app.route('/students')
def students():
    students = Student.query.all()
    return render_template('index.html')

@app.route('/capstoneday')
def capstone_day():
    return render_template('index.html')
