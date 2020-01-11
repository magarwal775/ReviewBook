from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from movies.models import MovieReview, Movie
from games.models import GameReview, Game
from series.models import EpisodeReview, Series, Episode
from accounts.models import Account

def base(request):
    return render(request, 'base.html')

def home(request):

    context = {}

    query = ""

    if request.GET:
        query = request.GET['q']

    context = get_queryset(str(query))
    context['query'] = str(query)

    return render(request, 'home.html', context)

def select_category(request):
    return render(request, 'select_category.html')

def get_queryset(query=None):
    queryset = {}
    queries = query.split(" ")
    if query:
        for q in queries:
            movies = Movie.objects.filter(
                    Q(name__icontains=q),
            ).distinct()
            games = Game.objects.filter(
                    Q(name__icontains=q),
            ).distinct()
            series = Series.objects.filter(
                    Q(name__icontains=q),
            ).distinct()
            episodes = Episode.objects.filter(
                    Q(episode_name__icontains=q),
            ).distinct()
            users = Account.objects.filter(
                    Q(first_name__icontains=q),
            ).distinct()

            queryset['movies'] = movies
            queryset['games'] = games
            queryset['series'] = series
            queryset['episodes'] = episodes
            queryset['users'] = users
    else:
        moviereview = MovieReview.objects.order_by('-date_published')
        gamereview = GameReview.objects.order_by('-date_published')
        episodereview = EpisodeReview.objects.order_by('-date_published')

        queryset['moviereview'] = moviereview
        queryset['gamereview'] = gamereview
        queryset['episodereview'] = episodereview

    return queryset
