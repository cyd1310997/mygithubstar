
######################################
import os
import shutil
import argparse
import sys
import threading
import time
import sqlite3
import re
import uuid
######################################

######################################
from math import ceil
from github import Github


def starred_repos(user):
    starred = user.get_starred()
    total_pages = ceil(starred.totalCount / 30) 

    for page_num in range(0, total_pages):
        for repo in starred.get_page(page_num):
            yield repo

def export_github_stars():
    gh = Github()
    user = gh.get_user('cyd1310997')
    L = []
    for repo in starred_repos(user):
        title = str(repo.description)
        url = str(repo.html_url)

        repo_name = re.sub('^.*/(.*)/(.*)$', '\\1/\\2: ', url)
        
        title = title.replace('`', '')
        title = title.replace('<', '')
        title = title.replace('>', '')
        title = repo_name + title
        
        s = f'<a href="{url}" target="_blank">{title}</a>  |  <br>  '
        L.append(s)
    with open('nav.githubstar.html', 'w') as f:
        f.write('\n'.join(L) + '\n')
    shutil.copy('nav.githubstar.html','nav.githubstar.md')

def main():
    export_github_stars()
    print('ok')
if __name__ == '__main__':
    main()