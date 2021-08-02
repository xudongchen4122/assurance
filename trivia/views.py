from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from trivia.models import Game, Round, Question, Choice, Player
from setup.settings import MINIMUM_NUMBER_PLAYERS
import random


def index(request):
    if not request.user.is_authenticated:
        latest_posts = None
        return render(
            request, 'index.html', {
                'posts': latest_posts
            })
    else:
        return HttpResponseRedirect('/me/')


def me(request):
    if request.user.is_authenticated:
        games = Game.objects.all()
        return render(
            request, 'me.html', {
                'user': request.user,
                'games': games,
            })
    else:
        return HttpResponseRedirect('/login/')


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/post/')
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return HttpResponseRedirect('/me/')
            else:
                print('User not found')
        else:
            # If there were errors, we render the form with these
            # errors
            return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/post/')
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/#the-save-method
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/me/')
        else:
            # If there were errors, we render the form with these
            # errors
            return render(request, 'signup.html', {'form': form})


def play_game(request):
    if request.user.is_authenticated:
        game_id = request.GET['game']
        current_round = int(request.GET['round'])
        game = Game.objects.filter(pk=game_id).first()
        rounds = Round.objects.filter(game=game).all()

        used_questions = [round.question_id for round in rounds]
        questions = Question.objects.all()

        player = Player.objects.filter(game=game, user=request.user).first()
        rounds = list(rounds)
        rounds.sort(key=lambda round:-round.order)

        if len(rounds) == 0 or current_round > rounds[0].order:
            not_used_questions = [question for question in questions if question.id not in used_questions]
            question = random.choice(not_used_questions)
            new_round = Round(
                game=game,
                question=question,
                order=1 if len(rounds) == 0 else rounds[0].order + 1
            )
            new_round.save()
        else:
            new_round = [round for round in rounds if round.order == current_round][0]
            question = [question for question in questions if question.id == new_round.question_id][0]

        choices = Choice.objects.filter(question=question.id).all()

        if player is None:
            player = Player (
                game=game,
                user=request.user,
                status='STARTED',
                last_round=new_round.order
            )
            player.save()

        players = Player.objects.filter(game=game, status='STARTED').all()

        return render(
            request, 'play_game.html', {
                'user': request.user,
                'game': game,
                'round': new_round,
                'question': question,
                'choices': choices,
                'player': player,
                'players': players,
                'minimum_number_players': MINIMUM_NUMBER_PLAYERS
            })
    else:
        return HttpResponseRedirect('/login/')