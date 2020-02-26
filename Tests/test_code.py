import requests


def test_answer(paramses, status):
    response = requests.get(paramses)
    assert (response.status_code) == status
