import time
import json
from urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


def request(url, max_error_count=3):
    while(max_error_count > 0):
        try:
            request = urlopen(url)
            return request
        except HTTPError:
            return None
        except URLError:
            return None
        except:
            print('No response, waiting 10 seconds...')
            time.sleep(10)
            max_error_count -= 1
            print('Retrying...')
    return None


def scrap_request(url, max_error_count=3):
    try:
        expect_request = Request(url, headers={'User-Agent': '  Mozilla/5.0'})
        html = request(expect_request, max_error_count).read()
        return BeautifulSoup(html, "lxml")
    except:
        return None


def api_request(url, max_error_count=3):
    try:
        response = request(url, max_error_count)
        return json.loads(response.read())
    except:
        return None
