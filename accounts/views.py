from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from accounts.forms import RegistrationForm, AccountAuthenticationForm
from django.urls import reverse

from games.models import GameReview
from movies.models import MovieReview
from series.models import EpisodeReview
from accounts.models import UserFollow, Account
from base.views import get_queryset

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('base:home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)

def logout_view(request):
    logout(request)
    return redirect("base:home")


def login_view(request):

    context = {}

    user=request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("base:home")

    else:
        form=AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'account/login.html', context)

def account_view(request, slug):

    if not request.user.is_authenticated:
        return redirect("accounts:must_authenticate")

    context = {}

    author = Account.objects.get(username=slug)
    movie_review = MovieReview.objects.filter(author=author)
    game_review = GameReview.objects.filter(author=author)
    episode_review = EpisodeReview.objects.filter(author=author)
    context['movie_review'] = movie_review
    context['game_review'] = game_review
    context['episode_review'] = episode_review
    context['user'] = author

    return render(request, "account_view.html", context)

def must_authenticate_view(request):
    return render(request, 'must_authenticate.html', {})


def feed_view(request):
    if not request.user.is_authenticated:
        return redirect("accounts:must_authenticate")
    followers = request.user.Following.all()
    movie_review=MovieReview.objects.filter(author__in= followers).order_by('-date_published')
    context = {'movie_review':movie_review}
    return render(request,'account/feed.html',context)
