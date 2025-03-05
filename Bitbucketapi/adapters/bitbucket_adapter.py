from .base_adapter import BaseAdapter
import requests
import os
from git import Repo


class BitbucketAdapter(BaseAdapter):
    def __init__(self,repo_url,local_path=r"C:\Users\sks\OneDrive - Amadeus Workplace\Documents\P_queue\obe-hcr-ifd"):
        self.repo_url="https://rndwww.nce.amadeus.net/git/scm/ahfr/obe-hcr-ifd.git" #FILL URL
        self.local_path=local_path

    def get_commits(self, branch="release/5"):
        #url = f"https://rndwww.nce.amadeus.net/git/scm/ahfr/obe-hcr-ifd.git"  #FILL URL
        #response=requests.get(url,auth=self.auth)
        repo=Repo(self.local_path)
        commits=[]
        #if response.status_code=='200':
        for commit in repo.iter_commits(branch):
            #commits=response.json()["values"]
            commits.append(
                {"Hash":commit.hexsha,
                 "message":commit.message.strip(),
                 "author":commit.author.name}
            )
        return commits
        #else:
            #print(f"Failed to retrieve the file")
        
