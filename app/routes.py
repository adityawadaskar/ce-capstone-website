import os
from app import app
from flask import render_template, redirect, send_from_directory
from app.models import Student, Project, Sponsor

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/projects')
def projects():
    project = Project.query.all()
    return render_template('projects.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/sponsors')
def sponsors():
    return render_template('sponsors.html')

@app.route('/students')
def students():
    students = Student.query.all()
    return render_template('students.html')

@app.route('/capstoneday')
@app.route('/capstone-day')
def capstone_day():
    return redirect("https://www.ce.ucsb.edu/undergrad/curriculum/capstone/events/ece189", code=302)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'),
                          'favicon.png',mimetype='image/vnd.microsoft.icon')