# CE Capstone Website

The goal of this repo is to simplify the addition of new students, projects, and sponsors to the UCSB CE Capstone website.
This repository generates the *capstone* subfolder within [Prof. Isukapalli's website](https://www.ece.ucsb.edu/~yoga/).

## Setup

1. Make sure you have python installed (ideally 3.5+).
2. Clone this repository locally.
3. Within the cloned repo, [create a python virtualenv](https://sourabhbajaj.com/mac-setup/Python/virtualenv.html) called *venv*. If using a different name, add it to the .gitignore file.
4. Activate the venv. You'll do this every time you work on this repo.
5. Use the below command to install all needed packages into your local venv.
```bash
pip install -r requirements.txt
```

## Execution

It is important to follow a [model-view-controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) format within projects. This way, when adding new elements (like student projects, pictures, sponsors, etc.), the developer simply inputs this into a local database file without having to hard-code HTML/CSS elements.

Run the following command from the local repository. This will generate a *build* subfolder within the *app* folder and run the website locally.

```bash
python ce-capstone.py
```
The *build* folder contains static files that can be deployed to any HTTP server, and don't need a backend python server setup.
