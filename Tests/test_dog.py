import requests
import pytest


def test_success():
    response2 = requests.get("https://dog.ceo/api/breeds/image/random")
    assert response2.status_code == 200


def test_status():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    assert (response.json()['status']) == 'success'


def test_len():
    response2 = requests.get("https://dog.ceo/api/breed/hound/images/random/3")
    assert (len(response2.json()['message'])) == 3


@pytest.mark.parametrize('breed',
                         [
                             ('https://dog.ceo/api/breed/akita/images/random'),
                             ('https://dog.ceo/api/breed/hound/images/random'),
                             ('https://dog.ceo/api/breed/boxer/images/random')

                         ])
def test_4(breed):
    response3 = requests.get(breed)
    assert response3.json()['message'].endswith('.jpg')


@pytest.mark.parametrize('sub_breed',
                         [
                             ('https://dog.ceo/api/breed/hound/list'),
                             ('https://dog.ceo/api/breed/bulldog/list'),
                             ('https://dog.ceo/api/breed/mastiff/list')

                         ])
def test_5(sub_breed):
    response = requests.get(sub_breed)
    assert ((len(response.json()['message']))) > 2
