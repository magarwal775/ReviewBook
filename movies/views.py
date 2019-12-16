from django.shortcuts import get_object_or_404,render,redirect
from django.urls import reverse
from movies.models import MovieReview, Movie
from movies.forms import GiveReviewForm
from accounts.models import Account

def index(request):
    movie_list= Movie.objects.order_by('-name')
    context = {'movie_list':movie_list}
    return render(request,'movies/movielist.html',context)

def details(request,movie_id):
    movie= get_object_or_404(Movie,pk=movie_id)
    return render(request,'movies/details.html',{'movie':movie})

def give_movie_review(request, movie_id):

    context = {}

    user = request.user
    movie = get_object_or_404(Movie, id=movie_id)
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = GiveReviewForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.movie = movie
        obj.author = user
        obj.save()
        form = GiveReviewForm()

    context['form']=form

    return render(request, 'give_movie_review.html', context)

def select_movie(request):

    movies = Movie.objects.all()
    context ={'movies':movies}

    return render(request, 'select_movie.html', context)
