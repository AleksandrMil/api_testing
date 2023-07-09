import requests
from http import HTTPStatus

def test_registration():
    url = 'https://reqres.in/api/register'
    headers = {
        'Content-Type': 'application/json'
    }
    body = {
        'email': 'eve.holt@reqres.in',
        'password': 'any_password'
    }

    response = requests.post(url, headers=headers, json=body)

    assert response.status_code == HTTPStatus.OK
    assert response.json().get('token') is not None
    print(response.status_code)


def test_incorrect_registration():
    url = 'https://reqres.in/api/register'
    headers = {
        'Content-Type': 'application/json'
    }
    body = {
        'email': 'eve.holt@reqres.in'
    }

    response = requests.post(url, headers=headers, json=body)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json().get('error') == 'Missing password'
    print(response.status_code) #просто для визуальной проверки
