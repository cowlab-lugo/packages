import requests
import validators


def check(url):
    try:
        if(validators.url(url)):
            r = requests.get(url)
            if(r.status_code is 200):
                return True
            return False
        else:
            return False
    except:
        return False
