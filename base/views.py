from django.shortcuts import render, redirect
from django.urls import reverse
from movies.models import MovieReview
from games.models import GameReview
from series.models import EpisodeReview

def base(request):
    return render(request, 'base.html')

def home(request):

    context = {}
    moviereview = MovieReview.objects.order_by('-date_published')
    gamereview = GameReview.objects.order_by('-date_published')
    episodereview = EpisodeReview.objects.order_by('-date_published')

    context['moviereview'] = moviereview
    context['gamereview'] = gamereview
    context['episodereview'] = episodereview

    return render(request, 'home.html', context)

def select_category(request):
    return render(request, 'select_category.html')
