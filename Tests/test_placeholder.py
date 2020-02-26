import requests
import pytest


def test_status():
    response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1")
    assert (response.status_code) == 200


@pytest.mark.parametrize('input_title, output_title', [('title', 'title'), ('test', 'test'), ('vvv', 'vvv')])
def test(input_title, output_title):
    response = requests.post('https://jsonplaceholder.typicode.com/posts', data={'title': input_title, 'userId': '1', 'id':'5'})
    assert response.json()['title'] == output_title


def test_len():
    response2 = requests.get("https://jsonplaceholder.typicode.com/comments?postId=4")
    assert len(response2.json()) == 5


def test_todos():
    response2 = requests.get("https://jsonplaceholder.typicode.com/users/3/todos")
    assert response2.json()[3]['completed'] == True


@pytest.mark.parametrize('input_body, output_body, userId',
                         [('title', 'title', 4), ('test', 'test', 8), ('vvv', 'vvv', 15)])
def test_body(input_body, output_body, userId):
    response3 = requests.put('https://jsonplaceholder.typicode.com/posts/2',
                             data={'body': input_body, 'userId': userId})
    assert response3.json()['body'] == output_body
