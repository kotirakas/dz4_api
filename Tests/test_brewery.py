import requests
import pytest


@pytest.mark.parametrize('postal', [('44107'), ('45402-2105'), ('45231-3559')])
def test_state(postal):
    response = requests.get("https://api.openbrewerydb.org/breweries?by_postal=postal")
    assert (response.status_code) == 200


def test_type():
    response = requests.get("https://api.openbrewerydb.org/breweries?by_type=bar")
    assert (response.json()[0]['brewery_type']) == 'bar'


def test_country():
    response = requests.get('https://api.openbrewerydb.org/breweries/5494')
    assert (response.json()['country']) == 'United States'


@pytest.mark.parametrize('pages', [('12'), ('17'), ('25')])
def test_len(pages):
    response = requests.get("https://api.openbrewerydb.org/breweries?page=pages")
    assert (len(response.json())) == 20


def test_tag():
    response = requests.get("https://api.openbrewerydb.org/breweries?by_tag=patio")
    assert (response.json()[0]['tag_list']) == ['patio']
