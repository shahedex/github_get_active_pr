from github import Github
from dotenv import load_dotenv
import csv
import os

load_dotenv()
g = Github(os.getenv('GITHUB_TOKEN'))
repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))

pulls = repo.get_pulls(state='open', sort='created', base='master')

with open('generated_csv/pr-list.csv', mode='w') as csv_file:
    fieldnames = ['PR No.', 'Title', 'Created']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for pr in pulls:
        print("PR#" + str(pr.number) + \
        " Title: " + pr.title + " Created: " + \
        pr.created_at.strftime("%d %B, %Y, %H:%M:%S"))

        writer.writerow({
            'PR No.': str(pr.number),
            'Title': pr.title,
            'Created': pr.created_at.strftime("%d %B, %Y, %H:%M:%S")
        })
