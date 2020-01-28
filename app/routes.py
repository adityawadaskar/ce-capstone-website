import os
from app import app
from flask import render_template, redirect, send_from_directory
from app.models import Student, Project, Sponsor

CURRENT_SPONSORS = "static/img/sponsors/current_sponsors_resized"
STUDENT_IMAGES = "static/img/students"
PROJECT_POSTER = "static/img/projects/poster"
PROJECT_SLIDES = "static/img/projects/slides"
PROJECT_LOGOS = "static/img/projects/logos"
GROUP_PICTURES = "static/img/group_pictures"
CURRENT_PROJECT_YEAR = 2019

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    current_sponsors_img_dir = os.path.join(app.root_path, CURRENT_SPONSORS)
    image_filenames = os.listdir(current_sponsors_img_dir)
    sponsors = Sponsor.query.all()
    images = list()
    for filename in image_filenames:
        for sponsor in sponsors:
            if filename == sponsor.logo and len(sponsor.logo) > 1:
                images.append({'imgpath': "../%s/%s" % (CURRENT_SPONSORS, filename), 'website': sponsor.website})
    return render_template('index.html', sponsors=images)

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/projects')
@app.route('/projects/<int:year>')
def projects(year=CURRENT_PROJECT_YEAR):
    projects = Project.query.filter_by(year=year).all()
    for prj in projects:
        if prj.logo and len(prj.logo) > 1:
            prj.logo = "../%s/%s" % (PROJECT_LOGOS, prj.logo)
        # Sort by alphabetical order and make team lead appear first
        prj.students = sorted(prj.students, key = lambda i: i.name)
        for team_lead in prj.team_leads:
            prj.students.remove(team_lead)
            prj.students.insert(0, team_lead)
        # Check video
        if len(prj.video) == 0:
            prj.video = None 
        # Join image path
        for student in prj.students:
            student.image = "../%s/%s" % (STUDENT_IMAGES, student.image)
        # Check if website, presentation, and/or poster are available
        prj.resources_available = True if (prj.website != None or prj.presentation != None or prj.poster != None) else False
        prj.resources = list()
        if prj.resources_available:
            if prj.website != None:
                prj.resources.append({'link': prj.website, 'info': 'Website'})
            if prj.presentation != None:
                prj.resources.append({'link': "../%s/%s" % (PROJECT_SLIDES, prj.presentation), 'info': 'Presentation'})
            if prj.poster != None:
                prj.resources.append({'link': "../%s/%s" % (PROJECT_POSTER, prj.poster), 'info': 'Poster'})
    
    year_picture = find_year_picture(year)

    return render_template('projects.html', projects=projects, year=year, current_year=CURRENT_PROJECT_YEAR, year_picture=year_picture)

def find_year_picture(year):
    path = os.path.join(app.root_path, GROUP_PICTURES)
    files = os.listdir(path)
    for fname in files:
        if str(year) in fname:
            return "../%s/%s" % (GROUP_PICTURES, fname)
    return None

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/sponsors')
def sponsors():
    return render_template('sponsors.html')

@app.route('/capstoneday')
@app.route('/capstone-day')
def capstone_day():
    return redirect("https://www.ce.ucsb.edu/undergrad/curriculum/capstone/events/ece189", code=302)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'),
                          'favicon.png',mimetype='image/vnd.microsoft.icon')