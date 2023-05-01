#1/usr/bin/python3
"""You must use the GitHub API, here is the documentation https:
    //developer.github.com/v3/repos/commits/
"""

import requests
import sys

if __name__ == "__main__":

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = https://api.github.com/repos/{}/{}/commits"\
        .format(owner_name, repository_name)
    data = requests.get(url)
    for idx, value in enumerate(data.json()):
        if idx == 10:
            break
        print("{}: {}"
              .format(value.get('sha'),
                      value['commit']['author']['name']))

