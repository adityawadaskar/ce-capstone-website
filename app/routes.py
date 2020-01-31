import os
import copy
from app import app
from flask import render_template, redirect, send_from_directory, url_for
from sqlalchemy import and_
from app.models import Student, Project, Sponsor

SPONSOR_LOGOS_LARGE = "img/sponsors/sponsors_large"
SPONSOR_LOGOS_SMALL = "img/sponsors/sponsors_small"
STUDENT_IMAGES = "img/students"
PROJECT_POSTER = "img/projects/poster"
PROJECT_SLIDES = "img/projects/slides"
PROJECT_IMAGES = "img/projects/images"
PROJECT_LOGOS = "img/projects/logos/logos_resized"
GROUP_PICTURES = "img/group_pictures"
CURRENT_PROJECT_YEAR = 2020

@app.route('/')
def index():
    projects = Project.query.filter(Project.year==CURRENT_PROJECT_YEAR).all()
    sponsor_images = list()
    for project in projects:
        for sponsor in project.sponsors:
            sponsor_images.append({'name': sponsor.name, 'website': sponsor.website, 'imgpath': "%s/%s" % (SPONSOR_LOGOS_SMALL, sponsor.logo)})
    # Remove duplicates
    sponsor_images = [dict(t) for t in {tuple(d.items()) for d in sponsor_images}]
    return render_template('index.html', sponsors=sponsor_images, current_year=CURRENT_PROJECT_YEAR, title="UCSB CE Capstone")

@app.route('/schedule/')
def schedule():
    return render_template('schedule.html', current_year=CURRENT_PROJECT_YEAR, title="UCSB CE Capstone - Schedule")

@app.route('/projects/')
@app.route('/projects/<int:year>/')
def projects(year=CURRENT_PROJECT_YEAR):
    projects = Project.query.filter(Project.year==year, Project.students != None).all()#.filter(logo!=None).all()
    for prj in projects:
        # Set video/image location
        if prj.image:
            prj.image_path = "%s/%s" % (PROJECT_IMAGES, prj.image)
        # Set logo filepath
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

    return render_template('projects.html', projects=projects, year=year, current_year=CURRENT_PROJECT_YEAR, year_picture=year_picture, title="UCSB CE Capstone - Projects")

def find_year_picture(year):
    path = os.path.join(app.root_path, "static/%s" % GROUP_PICTURES)
    files = os.listdir(path)
    for fname in files:
        if str(year) in fname:
            return "%s/%s" % (GROUP_PICTURES, fname)
    return None

@app.route('/resources/')
def resources():
    return render_template('resources.html', current_year=CURRENT_PROJECT_YEAR, title="UCSB CE Capstone - Resources")

@app.route('/sponsors/')
def sponsors():

    projects = Project.query.order_by(Project.year.desc())
    year = projects[0].year
    year_dict = {'year': year, 'sponsors': list()}
    all_sponsors = list()
    for project in projects:
        if project.year != year:
            year = project.year
            all_sponsors.append(year_dict)
            year_dict = {'year': year, 'sponsors': list()}

        sponsors = project.sponsors
        for sponsor in sponsors:
            sponsor_in_year = False
            for yearly_sponsor in year_dict['sponsors']:
                if sponsor.name == yearly_sponsor['name']:
                    yearly_sponsor['project'] += " and " + project.name
                    sponsor_in_year = True

            if not sponsor_in_year:
                year_dict['sponsors'].append({
                    'project': project.name,
                    'name': sponsor.name,
                    'link': sponsor.website,
                    'logo': "%s/%s" % (SPONSOR_LOGOS_SMALL, sponsor.logo),
                    'logo_large': "%s/%s" % (SPONSOR_LOGOS_LARGE, sponsor.logo),
                    'student_project': project.student_project})

    all_sponsors.append(year_dict)

    return render_template('sponsors.html', yearly_sponsors=all_sponsors, current_year=CURRENT_PROJECT_YEAR, title="UCSB CE Capstone - Sponsors")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'),
                          'favicon.png',mimetype='image/vnd.microsoft.icon')
