import pytest
import requests
# from trivia.models import Game
from setup.settings import BASE_URL
# import json


@pytest.mark.parametrize('name', 'test game')
def test_create_game(name):
    url = BASE_URL + 'games/'
    data = {'name': name}
    response = requests.post(url, json=data)
    print(response)
    assert response.status_code == 201
    game = response.json()
    assert game is not None and game['name'] == name.strip()


def test_get_games():
    url = BASE_URL + 'games/'
    response = requests.get(url)
    games = response.json()
    assert games is not None and len(games) > 0



