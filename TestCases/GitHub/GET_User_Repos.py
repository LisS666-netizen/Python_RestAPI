import json

import requests

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/vnd.github.nightshade-preview+json',
  'Authorization': 'Basic cHJhdmVlbnJlZGR5bmFyYWxhOlByQHZlZW4yNjc4NQ==',
  'Cookie': '_octo=GH1.1.1326905564.1596149133; logged_in=no'
}


def get_request(url_path):
    return requests.get(url_path, headers=headers)


def create_new_repo(url_path):
    payload = {
  "name": "Hello-World",
  "description": "This is your first repository",
  "homepage": "https://github.com",
  "private": False,
  "has_issues": True,
  "has_projects": True,
  "has_wiki": True
}
    return requests.post(url_path, headers=headers, json=payload)


def get_created_repo(ursl_path):
    return requests.get(ursl_path, headers=headers)


def update_repo(url_path):
    payload = {
  "name": "Hello-World",
  "description": "This is your first repository",
  "homepage": "https://github.com",
  "private": True,
  "has_issues": True,
  "has_projects": True,
  "has_wiki": True
}
    return requests.patch(url_path, headers=headers, json=payload)


def delete_repo(url_path):
    return requests.delete(url_path, headers=headers)

def create_file_in_repo(url_path):
    payload = {
  "message": "my first commit message",
  "committer": {
    "name": "Praveen Reddy Narala",
    "email": "praveenreddy.narala@gmail.com"
  },
  "content": "SGVsbG8sIFdvcmxk"
}
    return requests.put(url_path, headers=headers, json=payload)


def update_file_in_repo(url_path, sha):
    payload = {
  "message": "Updated content from Python Requests",
  "committer": {
    "name": "Monalisa Octocat",
    "email": "octocat@github.com"
  },
  "content": "SGVsbG8gUG9zdG1hbi4gSG93IGRvIHlvdSBkbz8=",
  "sha": sha
}
    return requests.put(url_path, headers=headers, json=payload)


def delete_file_in_repo(url_path, sha):
    payload = {
  "message": "delete file",
  "committer": {
    "name": "Praveen Reddy Narala",
    "email": "praveenreddy.narala@gmail.com"
  },
  "sha": sha
}
    return requests.delete(url_path, headers=headers, json=payload)


def get_content_of_repo(url_path):
    return requests.get(url_path, headers=headers)


def test_get_all_repos():
    response = get_request('https://api.github.com/user/repos')
    assert response.status_code == 200
    print(response.json()[0])
    print(response.json()[0].get('owner').get('login'))


def test_create_new_repo():
    response = create_new_repo('https://api.github.com/user/repos')
    assert response.status_code == 201


def test_get_created_repo():
    response = get_created_repo('https://api.github.com/repos/praveenreddynarala/Hello-World')
    assert response.status_code == 200
    assert response.json().get('name') == 'Hello-World'


def test_update_repo():
    response = update_repo('https://api.github.com/repos/praveenreddynarala/Hello-World')
    assert response.status_code == 200


def test_delete_repo():
    response = delete_repo('https://api.github.com/repos/praveenreddynarala/Hello-World')
    assert response.status_code == 204


def test_create_file_in_repo():
    response = create_file_in_repo('https://api.github.com/repos/praveenreddynarala/Hello-World/contents/README.md')
    assert response.status_code == 201
    print(response.json())


def test_update_file_in_repo():
    response = update_file_in_repo('https://api.github.com/repos/praveenreddynarala/Hello-World/contents/README.md',
                                   test_get_content_of_repo())
    assert response.status_code == 200
    print(response.json())


def test_delete_file_in_repo():
    response = delete_file_in_repo('https://api.github.com/repos/praveenreddynarala/Hello-World/contents/README.md',
                                   test_get_content_of_repo())
    assert response.status_code == 200
    print(response.json())


def test_get_content_of_repo():
    response = get_content_of_repo('https://api.github.com/repos/praveenreddynarala/Hello-World/contents')
    assert response.status_code == 200
    print(response.json()[0].get('sha'))
    return response.json()[0].get('sha')

