from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from trivia import views
from trivia.apis.question import QuestionList
from trivia.apis.choice import ChoiceList
from trivia.apis.game import GameList
from trivia.apis.answer import AnswerList
from trivia.apis.player import PlayerList
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^me/', views.me, name='me'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^play_game/$', views.play_game, name='play_game'),
    url(r'^questions/$', QuestionList.as_view()),
    url(r'^choices/$', ChoiceList.as_view()),
    url(r'^games/$', GameList.as_view()),
    url(r'^answers/$', AnswerList.as_view()),
    url(r'^players/$', PlayerList.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
