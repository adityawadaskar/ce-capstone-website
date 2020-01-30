import os
import copy
from app import app
from flask import render_template, redirect, send_from_directory, url_for
from app.models import Student, Project, Sponsor

ALL_SPONSOR_LOGOS = "img/sponsors/all_sponsors_resized"
CURRENT_SPONSOR_LOGOS = "img/sponsors/current_sponsors_resized"
STUDENT_IMAGES = "img/students"
PROJECT_POSTER = "img/projects/poster"
PROJECT_SLIDES = "img/projects/slides"
PROJECT_LOGOS = "img/projects/logos"
GROUP_PICTURES = "img/group_pictures"
CURRENT_PROJECT_YEAR = 2020

@app.route('/')
def index():
    current_sponsors_img_dir = os.path.join(app.root_path, "static/%s" % CURRENT_SPONSOR_LOGOS)
    image_filenames = os.listdir(current_sponsors_img_dir)
    sponsors = Sponsor.query.all()
    images = list()
    for filename in image_filenames:
        for sponsor in sponsors:
            if filename == sponsor.logo:
                images.append({'imgpath': "%s/%s" % (CURRENT_SPONSOR_LOGOS, filename), 'website': sponsor.website})
    return render_template('index.html', sponsors=images)

@app.route('/schedule/')
def schedule():
    return render_template('schedule.html')

@app.route('/projects/')
@app.route('/projects/<int:year>/')
def projects(year=CURRENT_PROJECT_YEAR):
    projects = Project.query.filter_by(year=year).all()
    # projects = copy.deepcopy(projects_orig)
    for prj in projects:
        if prj.logo and len(prj.logo) > 1:
            prj.logo_path = "%s/%s" % (PROJECT_LOGOS, prj.logo)
        # Sort by alphabetical order and make team lead appear first
        prj.students = sorted(prj.students, key = lambda i: i.name)
        for team_lead in prj.team_leads:
            prj.students.remove(team_lead)
            prj.students.insert(0, team_lead)
        # Join image path
        for student in prj.students:
            student.image_path = "%s/%s" % (STUDENT_IMAGES, student.image)
        # Check if website, presentation, and/or poster are available
        prj.resources_available = True if (prj.website != None or prj.presentation != None or prj.poster != None) else False
        prj.resources = list()
        if prj.resources_available:
            if prj.website != None:
                prj.resources.append({'link': prj.website, 'info': 'Website'})
            if prj.presentation != None:
                prj.resources.append({'link': url_for('static', filename="%s/%s" % (PROJECT_SLIDES, prj.presentation)), 'info': 'Presentation'})
            if prj.poster != None:
                prj.resources.append({'link': url_for('static', filename="%s/%s" % (PROJECT_POSTER, prj.poster)), 'info': 'Poster'})
    
    year_picture = find_year_picture(year)

    return render_template('projects.html', projects=projects, year=year, current_year=CURRENT_PROJECT_YEAR, year_picture=year_picture)

def find_year_picture(year):
    path = os.path.join(app.root_path, "static/%s" % GROUP_PICTURES)
    files = os.listdir(path)
    for fname in files:
        if str(year) in fname:
            return "%s/%s" % (GROUP_PICTURES, fname)
    return None

@app.route('/resources/')
def resources():
    return render_template('resources.html')

@app.route('/sponsors/')
def sponsors():
    sponsors = Sponsor.query.order_by(Sponsor.name.asc())
    current_sponsors = list()
    for sponsor in sponsors:
        for project in sponsor.projects:
            if project.year == CURRENT_PROJECT_YEAR:
                current_sponsors.append({'project': project.name, 'name': sponsor.name, 'link': sponsor.website, 'logo': "%s/%s" % (CURRENT_SPONSOR_LOGOS, sponsor.logo)})
    return render_template('sponsors.html', current_sponsors=current_sponsors)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'),
                          'favicon.png',mimetype='image/vnd.microsoft.icon')
