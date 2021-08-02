import requests
from setup.settings import BASE_URL


def test_create_player():
    game_id = 1
    user_id = 1
    url = BASE_URL + 'players/'
    data = {
        'game': game_id,
        'user': user_id
    }
    response = requests.post(url, json=data)
    if game_id < 1 or user_id < 1:
        assert response.status_code == 500
    else:
        assert response.status_code == 201
        player = response.json()
        assert player is not None


def test_get_players():
    url = BASE_URL + 'players/'
    response = requests.get(url)
    players = response.json()
    assert players is not None and len(players) > 0

