# CE Capstone Website

The goal of this repo is to simplify the addition of new students, projects, and sponsors to the UCSB CE Capstone website.
This repository generates the *capstone* subfolder within [Prof. Isukapalli's website](https://www.ece.ucsb.edu/~yoga/).

## Setup

1. Make sure you have python installed (ideally 3.5+).
2. Clone this repository locally.
3. Within the cloned repo, [create a python virtualenv](https://sourabhbajaj.com/mac-setup/Python/virtualenv.html) called *venv*. If using a different name, add it to the .gitignore file.
4. Enter the ce-capstone-website directory. Activate the venv by entering "source venv/bin/activate". You'll do this every time you work on this repo.
5. Use the below command to install all needed packages into your local venv.
```bash
pip install -r requirements.txt
```
6. Install the [SQLite DB Browser](https://sqlitebrowser.org/) on your local machine. This will be needed to make changes to the *app.db* file.

## Execution

### Step 1: Make needed changes to *app.db*
Using the SQLite DB Browser, first explore the current table setup. At the time of writing, the DB contains the following tables:
* project: Contains project information like name, year, description, etc. It also contains two other fields:
  * student_project: Set to 1 if this is a student project (which most projects are). This field exists to enable sponsor support where the sponsorship is for the overall capstone program (and not a specific team). If you look through the table, you'll notice that this field is set to 0 for certain projects, and those projects are all titled "Lead Sponsor of CE Capstone".
  * ordering: Specifies placement of this project relative to other projects on the website for that specific year.
* sponsor: Contains sponsor information like name, logo, and a link to the website.
* student: Contains student information like name, image, and a link to the personal website.

The *project*, *sponsor*, and *student* tables are independent. To connect these tables, the DB also contains the following relation tables:
* projects_sponsors: Specify project sponsors. This table allows for multi sponsor support under each project.
* students_projects: Specify project members. This table allows displaying students that work in multiple projects.
* teamleads_projects: Specify project leads. Their name and picture will appear first under each project on the website.

Once you have finished entering the updated information into the tables, save your changes.

If you wish to add additional functionality to the website, you may need to insert additional tables or columns. You'll need to do so in both *app.db* and *models.py*. Please use this detailed [tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database).

### Step 2: Make needed changes to _app/routes.py_
This file contains the following global variables at the top:
* CURRENT_PROJECT_YEAR: Set this variable to the latest project year that you wish to publish to the website.
* MINIMUM_SPONSOR_YEAR: Cutoff year for sponsor logos to be displayed in the Sponsors page.
* File path information (e.g. relative path to project logos, group pictures, etc.): Unless you want to add additional functionality to the website, there's no need to change these.

### Step 3: Make needed changes to *config.py*
When deploying the website, one must set the FREEZER_BASE_URL variable. This is the URL that leads to the capstone website. At the time of writing, this variable is set to "https://www.ece.ucsb.edu/~yoga/capstone/".

### Step 4: Generate build files
We will generate static files that can be deployed to any HTTP server, and don't need a backend python server setup.

Build the capstone folder by running the below command from within the repo. This will generate an *app/build* subfolder and if successful, begin to run the website locally.
```bash
python ce-capstone.py
```
If this step fails, the most likely cause is that incorrect information (such as a filename) was entered into the DB or the app has a bug. Make sure the filenames provided in app.db match the files present in the *app/static* folder.

### Step 5: Update build files
Certain components of the website (specifically the *Resources* page) need to be added in the post-processing: Without affecting the *app/build/resources/index.html* file, copy the contents of *app/static/resources/* into *app/build/resources/* 

### Step 6: Include build files within overall personal website.
1. From your existing deployed code base, delete all files and folders within the *capstone* directory.
2. Copy the contents of *app/build/* folder into the *capstone/* folder.
3. The code base is now ready to be deployed.
