import requests


def app_local(url):
    try:
        r = requests.get(url)
        return r.status_code
    except requests.exceptions.RequestException as e:
        print(e)


print(app_local(url='http://app.local'))