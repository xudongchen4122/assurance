from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    description = models.CharField(null=False, blank=False, max_length=500)


class Choice(models.Model):
    description = models.CharField(null=False, blank=False, max_length=500)
    correct_answer = models.BooleanField(null=False, blank=False, default=False)
    question = models.ForeignKey('Question', related_name='choices', on_delete=models.CASCADE, null=False, blank=False)


class Game(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)


class Round(models.Model):
    game = models.ForeignKey(Game, related_name='rounds', blank=False, null=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='rounds', blank=False, null=False, on_delete=models.CASCADE)
    order = models.IntegerField(null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)


class Player(models.Model):
    game = models.ForeignKey(Game, related_name='players', blank=False, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='players', on_delete=models.CASCADE, null=False, blank=False)
    status = models.CharField(null=True, blank=True, max_length=20)
    last_round = models.IntegerField(null=False, blank=False, default=1)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    player = models.ForeignKey(Player, related_name='answers', on_delete=models.CASCADE, null=False, blank=False)
    round = models.ForeignKey('Round', related_name='answers', on_delete=models.CASCADE, null=False, blank=False)
    choice = models.ForeignKey('Choice', related_name='answers', on_delete=models.CASCADE, null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
