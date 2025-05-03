import requests
import pandas as pd
from config import GITHUB_TOKEN, ORG_NAME, OUTPUT_CSV

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=100"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_repo_data(repo):
    repo_name = repo['name']
    owner = repo['owner']['login']

    # Last commit
    commits_url = f"https://api.github.com/repos/{owner}/{repo_name}/commits"
    commits = requests.get(commits_url, headers=headers).json()
    last_commit = commits[0]['commit']['committer']['date'] if commits else 'N/A'

    # Issues
    open_issues = repo['open_issues_count']

    # Contributors
    contributors_url = f"https://api.github.com/repos/{owner}/{repo_name}/contributors"
    contributors = requests.get(contributors_url, headers=headers).json()
    contributor_logins = [c.get('login', 'unknown') for c in contributors]

    return {
        'name': repo_name,
        'last_commit': last_commit,
        'open_issues': open_issues,
        'contributors': ', '.join(contributor_logins)
    }

def main():
    print(f"Fetching repos for org: {ORG_NAME}")
    repos = get_repos(ORG_NAME)
    data = [get_repo_data(repo) for repo in repos]
    df = pd.DataFrame(data)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"Report saved to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
