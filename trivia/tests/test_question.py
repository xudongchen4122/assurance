import requests
from setup.settings import BASE_URL


def test_get_questions():
    url = BASE_URL + 'questions/'
    response = requests.get(url)
    questions = response.json()
    assert questions is not None and len(questions) > 0

