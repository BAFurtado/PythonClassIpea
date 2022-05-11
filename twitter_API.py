import requests
import twitter_secrets
import re
import json


bearer_token = twitter_secrets.secrets.get('Bearer Token')
search_url = "https://api.twitter.com/2/tweets/search/recent"
cols_names = ['author_id', 'id', 'text']


def bearer_oauth(bear):
    """
    Method required by bearer token authentication.
    """

    bear.headers["Authorization"] = f"Bearer {bearer_token}"
    bear.headers["User-Agent"] = "v2RecentSearchPython"
    return bear


def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        rt = json.loads(response.text)
        if rt['errors'][0]['parameters']['since_id']:
            params.pop('since_id', None)
            response = requests.get(url, auth=bearer_oauth, params=params)
            print(response.status_code)
        else:
            raise Exception(response.status_code, response.text)
    return response.json()
