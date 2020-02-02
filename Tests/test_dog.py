import requests


def test_success():
     response2 = requests.get("https://dog.ceo/api/breeds/image/random")
     assert response2.status_code == 200


def test_status():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    assert (response.json()['status']) == 'success'


def test_len():
    response2 = requests.get("https://dog.ceo/api/breed/hound/images/random/3")
#print(len(response2.json()['message']))
    assert (len(response2.json()['message']))==3



