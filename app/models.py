from app import db

students_projects = db.Table('students_projects', 
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True),
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True)
)

team_leads_projects = db.Table('team_leads_projects',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True),
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True)
)

projects_sponsors = db.Table('projects_sponsors',
    db.Column('sponsor_id', db.Integer, db.ForeignKey('sponsor.id'), primary_key=True),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True)
)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    image = db.Column(db.String(400))
    linkedin = db.Column(db.String(400))
    projects = db.relationship('Project', secondary=students_projects, back_populates='students')
    projects_leading = db.relationship('Project', secondary=team_leads_projects, back_populates='students')

    def __repr__(self):
        return '<Student {}>'.format(self.name)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    year = db.Column(db.Integer)
    description = db.Column(db.String(1000))
    short_summary = db.Column(db.String(200))
    logo = db.Column(db.String(400))
    video = db.Column(db.String(400))
    website = db.Column(db.String(400))
    presentation = db.Column(db.String(400))
    poster = db.Column(db.String(400))
    team_leads = db.relationship('Student', secondary=team_leads_projects, back_populates='projects')
    students = db.relationship('Student', secondary=students_projects, back_populates='projects')
    sponsors = db.relationship('Sponsor', secondary=projects_sponsors, back_populates='projects')

    def __repr__(self):
        return '<Project {}>'.format(self.name)

class Sponsor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    logo = db.Column(db.String(400))
    website = db.Column(db.String(400))
    projects = db.relationship('Project', secondary=projects_sponsors, back_populates='sponsors')

    def __repr__(self):
        return '<Sponsor {}>'.format(self.name)
