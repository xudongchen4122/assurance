import sqlite3
import requests
import setup.settings as settings
import json


def insert_data():
    BASE_URL = settings.BASE_URL

    questions = [
        [
            '[Movie] What is the highest-grossing film of all time without taking inflation into account?',
            ['Titanic', False],
            ['Avengers: Endgame', True],
            ['Avatar', False],
            ['Star Wars: The Force Awakens', False]
        ],
        [
            '[Movie] Which actor or actress is killed off in the opening scene of the movie Scream?',
            ['Courtney Cox', False],
            ['Neve Campbell', False],
            ['Drew Barrymore', True],
            ['Rose McGowan', False]
        ],
        [
            '[Movie] Which film did Steven Spielberg win his first Oscar for Best Director?',
            ['Jaws', False],
            ['Catch Me If You Can', False],
            ['E.T.', False],
            ['Schindler’s List', True]
        ],
        [
            '[Movie] Which film won the first Academy Award for Best Picture?',
            ['All Quiet on the Western Front', False],
            ['Sunrise', False],
            ['Wings', True],
            ['Metropolis', False]
        ],
        [
            '[Movie] What is the name of Quint’s shark-hunting boat in Jaws?',
            ['The Whale', False],
            ['The Orca', True],
            ['The Dolphin', False],
            ['The Shark', False]
        ],
        [
            '[Disney] What was the first feature-length animated film ever released?',
            ['Pinocchio', False],
            ['Fantasia', False],
            ['Snow White and the Seven Dwarfs ', True],
            ['Dumbo', False]
        ],
        [
            '[Disney] What was the first original Disney song to win an Academy Award for Best Original Song?',
            ['Someday My Prince Will Come', False],
            ['Circle of Life', False],
            ['Beauty and the Beast', False],
            ['When You Wish Upon a Star', True]
        ],
        [
            '[Disney] What short film featured Mickey Mouse’s first appearance?',
            ['Plane Crazy', True],
            ['Wild Waves', False],
            ['The Band Concert', False],
            ['The Barnyard Concert', False]
        ],
        [
            '[Disney] What was the last movie Walt Disney was able to work on before he died?',
            ['Mary Poppins', False],
            ['101 Dalmatians', False],
            ['The Jungle Book', True],
            ['The Sword in the Stone', False]
        ],
        [
            '[Disney] As the Disney princess with the fewest lines, how many lines did Aurora (or “Sleeping Beauty”) have in total?',
            ['11', False],
            ['15', False],
            ['18', True],
            ['20', False]
        ],
        [
            '[Star Wars] What is the name of Han Solo’s ship?',
            ['Flagship', False],
            ['Patrol Cruiser', False],
            ['Empire Ship', False],
            ['Millennium Falcon', True]
        ],
        [
            '[Star Wars] In what month were all six original Star Wars films released?',
            ['March', False],
            ['April', False],
            ['May', True],
            ['June', False]
        ],
        [
            '[Star Wars] Which Star Wars character is partially named after director George Lucas’ son?',
            ['Max Rebo', False],
            ['Rick Olié', False],
            ['Dexter Jettster', True],
            ['Willrow Hood', False]
        ],
        [
            '[Star Wars] Which species stole the plans to the Death Star?',
            ['Sullustan', False],
            ['Bothan', True],
            ['Cerean', False],
            ['Rakata', False]
        ],
        [
            '[Star Wars] How many languages is C-3PO fluent in??',
            ['Over five million', False],
            ['Over six million', True],
            ['Over seven million', False],
            ['Over eight million', False]
        ],
        [
            '[Harry Potter] What is Harry Potter’s patronus?',
            ['A horse', False],
            ['An otter', False],
            ['A hare', False],
            ['A stag', True]
        ],
        [
            '[Harry Potter] What does the Imperius Curse do?',
            ['Mimics', False],
            ['Controls', True],
            ['Kills', False],
            ['Tortures', False]
        ],
        [
            '[Harry Potter] Who dies during the third Tri-wizard Tournament?',
            ['Viktor Krum', False],
            ['Cedric Diggory', True],
            ['Fleur Delacour', False],
            ['Cormac McLaggen', False]
        ],
        [
            '[Harry Potter] What does Dumbledore give to Ron in his will?',
            ['Deluminator', True],
            ['Invisibility cloak', False],
            ['Portrait', False],
            ['Wand', False]
        ],
        [
            '[Harry Potter] Who was the Hogwarts headmaster right before Dumbledore?',
            ['Phineas Nigellus', False],
            ['Armando Dippet', False],
            ['Dolores Umbridge', False],
            ['Dexter Fortescue', False]
        ],
        [
            '[Friends] What song is Phoebe most well known for?',
            ['Smelly Dog', False],
            ['Smelly Rat', False],
            ['Smelly Cat', True],
            ['Smelly Rabbit', False]
        ],
        [
            '[Friends] What is Chandler’s middle name?',
            ['Eustace', False],
            ['Francis', False],
            ['Muriel', True],
            ['Bing', False]
        ],
        [
            '[Friends] Who sings the Friends theme song?',
            ['The Other Ones', False],
            ['Great Buildings', False],
            ['The Rembrandts', True],
            ['The Quick', False]
        ],
        [
            '[Friends] What was Joey’s nickname while working at Alessandro?',
            ['Ken Adams', False],
            ['Dragon', True],
            ['Big Daddy', False],
            ['J-Man', False]
        ],
        [
            '[Friends] What was the name of Ross and Monica’s dog when they were kids?',
            ['Marcel', False],
            ['Tutti', False],
            ['Buddy', False],
            ['Chi Chi', True]
        ]
    ]

    try:
        for question in questions:
            question_json = {
                'description': question[0]
            }
            response = requests.post(BASE_URL + 'questions/', json=question_json)
            response_json = json.loads(response.content)
            question_id = response_json['id']

            if response.status_code == 201:
                for choice in question[1:]:
                    choice_json = {
                        'description': choice[0],
                        'correct_answer': choice[1],
                        'question': question_id
                    }
                    response = requests.post(BASE_URL + 'choices/', json=choice_json)

                    if response.status_code != 201:
                        raise Exception('Error in saving choice')

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:

        print("The SQLite connection is closed")


insert_data()