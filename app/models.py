from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    image = db.Column(db.String(400))
    linkedin = db.Column(db.String(400))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    def __repr__(self):
        return '<Student {}>'.format(self.name)

projects_sponsors = db.Table('projects_sponsors',
    db.Column('sponsor_id', db.Integer, db.ForeignKey('sponsor.id'), primary_key=True),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True)
)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    year = db.Column(db.Integer)
    members = db.relationship('Student', backref='project', lazy='dynamic')
    description = db.Column(db.String(1000))
    short_summary = db.Column(db.String(200))
    sponsors = db.relationship('Sponsor', secondary=projects_sponsors, back_populates='projects')
    logo = db.Column(db.String(400))
    video = db.Column(db.String(400))
    website = db.Column(db.String(400))
    presentation = db.Column(db.String(400))
    poster = db.Column(db.String(400))

    def __repr__(self):
        return '<Project {}>'.format(self.name)

class Sponsor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    logo = db.Column(db.String(400))
    website = db.Column(db.String(400))
    description = db.Column(db.String(200))
    projects = db.relationship('Project', secondary=projects_sponsors, back_populates='sponsors')

    def __repr__(self):
        return '<Sponsor {}>'.format(self.name)
