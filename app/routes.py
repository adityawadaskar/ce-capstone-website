from app import app
from app.models import Student, Project, Sponsor

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/projects')
def projects():
    project = Project.query.all()
    return "Project"

@app.route('/sponsors')
def sponsors():
    pass

@app.route('/students')
def students():
    pass
