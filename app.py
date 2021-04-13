from github import Github
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta
import gspread
import csv
import os

load_dotenv()
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('github_sheets.json', scope)
client = gspread.authorize(creds)
sheet = client.open('github_data')
sheet_instance = sheet.get_worksheet(0)

g = Github(os.getenv('GITHUB_TOKEN'))
repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))

pulls = repo.get_pulls(state='all', sort='created', base='master')
end_date = datetime.today().replace(day=1) - timedelta(days=1)
start_date = datetime.today().replace(day=1) - timedelta(days=end_date.day)
with open('generated_csv/pr-list.csv', mode='w') as csv_file:
    fieldnames = ['PR No.', 'Title', 'Created', 'State']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for pr in pulls:
        if pr.created_at > start_date and pr.created_at < end_date:
            print("PR#" + str(pr.number) + \
            " Title: " + pr.title + " Created: " + \
            pr.created_at.strftime("%d %B, %Y, %H:%M:%S") + " state: " + pr.state)
            sheet_instance.append_row([str(pr.number), pr.title, pr.created_at.strftime("%d %B, %Y, %H:%M:%S"), pr.state])
            writer.writerow({
                'PR No.': str(pr.number),
                'Title': pr.title,
                'Created': pr.created_at.strftime("%d %B, %Y, %H:%M:%S"),
                'State': pr.state
            })
