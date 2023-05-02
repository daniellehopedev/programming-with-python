import requests

user_name_input = input("Enter GitHub user name to list their public repos:\n")
user_name = user_name_input

response = requests.get(f"https://api.github.com/users/{user_name}/repos")

github_repos = response.json()

# print the whole object list
# print(github_repos)
# print(type(github_repos))

# print just the names and urls
for repo in github_repos:
    print(f"Repository Name: {repo['name']}\nRepository Url: {repo['owner']['html_url']}/{repo['name']}\n")