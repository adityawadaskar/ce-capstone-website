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
Skip this step if testing/deploying for the first time, as *app.db* should be up-to-date.

Using the SQLite DB Browser, first explore the current table setup. It should be self-explanatory how new information can be added or modified. Once you enter the updated information into the tables, save changes. The files will only build if the correct information is entered within this DB.

### Step 2: Generate build files
We will generate static files that can be deployed to any HTTP server, and don't need a backend python server setup.

Build the capstone folder by running the below command from within the repo. This will generate an *app/build* subfolder and if successful, begin to run the website locally.
```bash
python ce-capstone.py
```
If this step fails, it means that incorrect information was entered into the DB. Make sure to have the correct files present in the *app/static* folder.

### Step 3: Update build files
Certain components of the website (specifically the *Resources* page) need to be added in the post-processing: Without affecting the *app/build/resources/index.html* file, copy the contents of *app/static/resources/* into *app/build/resources/* 

### Step 4: Include build files within overall personal website.
1. From your existing deployed code base, delete all files and folders within the *capstone* directory.
2. Copy the contents of *app/build/* folder into the *capstone/* folder.
3. The code base is now ready to be deployed.
