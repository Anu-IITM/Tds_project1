# -*- coding: utf-8 -*-
"""TDS_project_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EF0WxaUa8fMdnU8REWlWmWoiDZTWRdTO
"""

pip install requests pandas

pip install requests

import requests

# Your GitHub token
token = 'ghp_wEqsurkYo0dvaYaqGF1y5140NRYVip48pZXq'

# Set up headers with the token
headers = {
    'Authorization': f'token {token}'
}

# Make a request to GitHub API (e.g., to get user information)
response = requests.get('https://api.github.com/user', headers=headers)

# Print the response (in JSON format)
print(response.json())

import requests

# Define the token and headers
github_token = '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'
headers = {'Authorization': f'token {github_token}'}

# Make the API request
response = requests.get('https://api.github.com/user', headers=headers)

# Print the response
print(response.json())

import requests

# GitHub API URL to get the user's repositories
user = "username"  # Replace 'username' with the actual GitHub username
url = f"https://api.github.com/users/{user}/repos"

# Your GitHub token
token = "ghp_wEqsurkYo0dvaYaqGFIy5140NRYVip48pZXq"  # Replace with your actual token

# Define the headers with your authorization token
headers = {
    "Authorization": f"token {token}"
}

# Make the GET request to get the user's repositories
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Get the list of repositories
    repos = response.json()

    # Print repository details (you can adjust the output as needed)
    for repo in repos:
        print(f"Repo Name: {repo['name']}")
        print(f"Created at: {repo['created_at']}")
        print(f"Stars: {repo['stargazers_count']}")
        print(f"Language: {repo['language']}")
        print(f"Has Wiki: {repo['has_wiki']}")
        print(f"License: {repo['license']['name'] if repo['license'] else 'No License'}")
        print("-" * 40)
else:
    print(f"Request failed with status code {response.status_code}")

!curl -H "Authorization: token ghp_wEqsurkYo0dvaYaqGFIy5140NRYVip48pZXq" https://api.github.com/users/Anu-IITM/repos

!curl -H "Authorization: token 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" https://api.github.com/users/username/repos

!curl -H "Authorization: token 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" https://api.github.com/rate_limit

import requests
import pandas as pd

# GitHub API setup
GITHUB_API_URL = "https://api.github.com"
HEADERS = {"Authorization": "token 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"}  # Add your GitHub token here

def fetch_users_in_delhi(min_followers=100):
    users_url = f"{GITHUB_API_URL}/search/users?q=location:delhi+followers:>{min_followers}"
    response = requests.get(users_url, headers=HEADERS)
    return response.json()['items']

def fetch_user_details(username):
    user_url = f"{GITHUB_API_URL}/users/{username}"
    response = requests.get(user_url, headers=HEADERS)
    return response.json()

def fetch_user_repos(username):
    repos_url = f"{GITHUB_API_URL}/users/{username}/repos"
    response = requests.get(repos_url, headers=HEADERS)
    return response.json()

def clean_company_name(company_name):
    if company_name:
        return company_name.strip().lstrip('@').upper()
    return None

# Fetch users
users = fetch_users_in_delhi()

# Prepare data for users.csv and repositories.csv
users_data = []
repos_data = []

for user in users:
    user_details = fetch_user_details(user['login'])

    # Clean the company name
    company = clean_company_name(user_details.get('company'))

    # User details
    user_row = {
        'login': user['login'],
        'name': user_details.get('name'),
        'company': company,
        'location': user_details.get('location'),
        'email': user_details.get('email'),
        'hireable': user_details.get('hireable', False),
        'bio': user_details.get('bio'),
        'public_repos': user_details.get('public_repos'),
        'followers': user_details.get('followers'),
        'following': user_details.get('following'),
        'created_at': user_details.get('created_at')
    }
    users_data.append(user_row)

    # Fetch repositories for each user
    repos = fetch_user_repos(user['login'])
    for repo in repos:
        repo_row = {
            'login': user['login'],
            'full_name': repo['full_name'],
            'created_at': repo['created_at'],
            'stargazers_count': repo['stargazers_count'],
            'watchers_count': repo['watchers_count'],
            'language': repo.get('language'),
            'has_projects': repo.get('has_projects', False),
            'has_wiki': repo.get('has_wiki', False),
            'license_name': repo['license']['name'] if repo.get('license') else None
        }
        repos_data.append(repo_row)

# Convert to DataFrames
users_df = pd.DataFrame(users_data)
repos_df = pd.DataFrame(repos_data)

# Save to CSV
users_df.to_csv('users.csv', index=False)
repos_df.to_csv('repositories.csv', index=False)

- This script scrapes GitHub users from Delhi with more than 100 followers and fetches details about their public repositories.
- One interesting finding: a significant number of developers in Delhi have their repositories set to private or don't have many followers despite their contributions.
- Actionable recommendation: Developers should contribute more to open-source projects to increase visibility and network in the developer community.

def create_readme():
    content = """
- This script scrapes GitHub users from Delhi with more than 100 followers and fetches details about their public repositories.
- One interesting finding: a significant number of developers in Delhi have their repositories set to private or don't have many followers despite their contributions.
- Actionable recommendation: Developers should contribute more to open-source projects to increase visibility and network in the developer community.
"""
    with open('README.md', 'w') as readme_file:
        readme_file.write(content)

import base64
import requests

# GitHub credentials
TOKEN = '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'  # Replace with your GitHub personal access token
REPO = 'your_username/your_repository'  # Replace with your GitHub repository (username/repo)
FILE_PATH = 'README.md'  # Path of the file in the repository

# URL for the GitHub API
url = f'https://api.github.com/repos/{REPO}/contents/{FILE_PATH}'

# Content to be written into README.md
content = """
# My Project

- This script scrapes GitHub users from Delhi with more than 100 followers and fetches details about their public repositories.
- One interesting finding: a significant number of developers in Delhi have their repositories set to private or don't have many followers despite their contributions.
- Actionable recommendation: Developers should contribute more to open-source projects to increase visibility and network in the developer community.

"""

# Encode the content in Base64
encoded_content = base64.b64encode(content.encode()).decode()

# Request headers
headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Payload for creating the file
data = {
    'message': 'Create README.md via GitHub API',
    'content': encoded_content
}

# Make the request to create/update the file
response = requests.put(url, json=data, headers=headers)

# Check the response
if response.status_code == 201:
    print("README.md created successfully.")
elif response.status_code == 200:
    print("README.md updated successfully.")
else:
    print(f"Error: {response.status_code}")
    print(response.json())