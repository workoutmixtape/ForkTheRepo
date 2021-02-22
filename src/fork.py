
import requests


BASE_URL = 'https://api.github.com'


def forktherepo(oauth_token):
    headers = {
        'Authorization': f'token {oauth_token}',
        'Accept': 'application/vnd.github.v3+json',
    }
    response = requests.post(
        url=f'{BASE_URL}/repos/gavinest/forktherepo/forks',
        headers=headers,
    )
    response.raise_for_status()
