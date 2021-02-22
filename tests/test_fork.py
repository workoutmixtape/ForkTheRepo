import pytest
import responses

from requests import HTTPError

from src.fork import forktherepo


@responses.activate
def test_fork_the_repo_success():
    # ARRANGE
    token = 'faketoken'
    responses.add(
        method=responses.POST,
        url='https://api.github.com/repos/psf/requests/forks',
        status=200
    )

    # ACT
    result = forktherepo(oauth_token=token)

    # ASSERT
    assert result is None
    assert len(responses.calls) == 1
    req = responses.calls[0].request
    assert req.headers['Authorization'] == f'token {token}'


@responses.activate
def test_fork_the_repo_raises():
    # ARRANGE
    token = 'faketoken'
    responses.add(
        method=responses.POST,
        url='https://api.github.com/repos/psf/requests/forks',
        status=403
    )

    # ACT/ASSERT
    with pytest.raises(HTTPError):
        forktherepo(oauth_token=token)
