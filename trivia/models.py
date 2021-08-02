from django.db import models
from django.contrib.auth.models import User


"""
Question Model
"""
class Question(models.Model):
    description = models.CharField(null=False, blank=False, max_length=500)


"""
Choice Model
"""
class Choice(models.Model):
    description = models.CharField(null=False, blank=False, max_length=500)
    correct_answer = models.BooleanField(null=False, blank=False, default=False)
    question = models.ForeignKey('Question', related_name='choices', on_delete=models.CASCADE, null=False, blank=False)


"""
Game Model
"""
class Game(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)


"""
Round Model
"""
class Round(models.Model):
    game = models.ForeignKey(Game, related_name='rounds', blank=False, null=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='rounds', blank=False, null=False, on_delete=models.CASCADE)
    # sequential order of the rounds
    order = models.IntegerField(null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)


"""
Player Model
Note: Player is not user. When a user start/join a game, the user 
becomes a player.
"""
class Player(models.Model):
    # The game the player is playing
    game = models.ForeignKey(Game, related_name='players', blank=False, null=False, on_delete=models.CASCADE)
    # The user this player is
    user = models.ForeignKey(User, related_name='players', on_delete=models.CASCADE, null=False, blank=False)
    # THe status of the player (Started, Won, Lost)
    status = models.CharField(null=True, blank=True, max_length=20)
    # last_round the player is playing
    last_round = models.IntegerField(null=False, blank=False, default=1)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)


"""
Answer Model
"""
class Answer(models.Model):
    player = models.ForeignKey(Player, related_name='answers', on_delete=models.CASCADE, null=False, blank=False)
    round = models.ForeignKey('Round', related_name='answers', on_delete=models.CASCADE, null=False, blank=False)
    choice = models.ForeignKey('Choice', related_name='answers', on_delete=models.CASCADE, null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    # even though we could check if this Answer is correct through choice table
    # it would be much easier to just record if it's correct in Answer object
    # Otherwise, we need extra calls to get all the choices and then determine if it's correct from frontend
    correct_answer = models.BooleanField(null=False, blank=False, default=False)