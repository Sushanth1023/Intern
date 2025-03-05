from .base_adapter import BaseAdapter
import requests
import os
from git import Repo


class BitbucketAdapter(BaseAdapter):
    def __init__(self,repo_url,):
        self.base_url="https://rndwww.nce.amadeus.net/git/scm/ahfr/obe-hcr-ifd.git" #FILL URL
        self.auth=(username,app_password)

    def get_commits(self, repo_name, branch):
        url = f"https://rndwww.nce.amadeus.net/git/scm/ahfr/obe-hcr-ifd.git"  #FILL URL
        response=requests.get(url,auth=self.auth)
        
        if response.status_code=='200':
            commits=response.json()["values"]
            return [
                {"Hash":commit["hash"],
                 "message":commit["message"],
                 "author":commit["author"]}
                 for commit in commits
            ]
        else: 
            print(f"Failed to retrieve the file: details: {response.json()}")
        
