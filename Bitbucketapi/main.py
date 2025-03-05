from adapters.bitbucket_adapter import BitbucketAdapter

#BIT_BUCKET_USERNAME = 'Sushanth K S' #FILL
#BIT_BUCKET_PASSWORD = ' ' #FILL
#BIT_BUCKET_REPO = 'obe-hcr-ifd'     #FILL
BRANCH = "master"         #FILL
BIT_BUCKET_GIT_URL = 'https://rndwww.nce.amadeus.net/git/scm/ahfr/obe-hcr-ifd.git' #FILL

def fetch_commits(adapter,repo_name,branch):
    commits=adapter.get_commits(branch)
    if 'error' in commits:
        print('Error:',commits['error'])
        return
    else:
        print("Commits:")
        for commit in commits[:5]:
            print(f"Commit:f{commit['hash']}")
            print(f"Author:f{commit['author']}")
            print(f"Message:f{commit['message']}")
            print(f"Date:f{commit['date']}")

if __name__ == '__main__':
    adapter = BitbucketAdapter(BIT_BUCKET_GIT_URL)
    fetch_commits(adapter,BRANCH)

