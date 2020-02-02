import requests


def test_state():
     response = requests.get("https://api.openbrewerydb.org/breweries?by_postal=44107")
     assert (response.json()[1]['state']) == 'Ohio'


def test_type():
    response = requests.get("https://api.openbrewerydb.org/breweries?by_type=bar")
    assert (response.json()[0]['brewery_type']) == 'bar'


#параметризировать по id
def test_country():
    response = requests.get("https://api.openbrewerydb.org/breweries/5494")
    assert (response.json()['country']) == 'United States'


#можно параметризировать по страниц
def test_len():
    response = requests.get("https://api.openbrewerydb.org/breweries?page=12")
    assert (len(response.json())) == 20


def test_tag():
    response = requests.get("https://api.openbrewerydb.org/breweries?by_tag=patio")
    assert (response.json()[0]['tag_list']) == ['patio']


