# Get a list of active PR's from a GitHub repository

## Clone the repository
```bash
$ git clone https://github.com/shahedex/github_get_active_pr.git
```
## Create and activate a Virtual Environment
```bash
$ cd github_get_active_pr
$ python3 -m venv venv
$ source venv/bin/activate
```

## Install the required dependencies
```bash
$ pip install -r requirements.txt
```
## Create a ENV file in the project directory
```bash
$ touch .env
$ nano .env
```
## Add the following to the .env file
```bash
GITHUB_TOKEN="your_github_personal_token"
GITHUB_REPOSITORY="the_repository_name"  # i.e, the-ionicus/tini
```
## Run the program to get the screenshot
```bash
$ python app.py
```

Open **generated_csv** directory to get the **CSV** format file.
