from django.shortcuts import get_object_or_404,render,redirect
from django.urls import reverse
from movies.models import MovieReview, Movie
from movies.forms import GiveReviewForm, UpdateReviewForm
from accounts.models import Account

def index(request):
    movie_list= Movie.objects.order_by('-name')
    context = {'movie_list':movie_list}
    return render(request,'movies/movielist.html',context)

def details(request,movie_id):
    movie= get_object_or_404(Movie,pk=movie_id)
    context = {'movie':movie}
    return render(request,'movies/details.html',context)

def give_movie_review(request, movie_id):

    context = {}

    user = request.user
    movie = get_object_or_404(Movie, id=movie_id)
    if not user.is_authenticated:
        return redirect('accounts:must_authenticate')

    review = MovieReview.objects.filter(movie_id=movie_id, author=request.user)
    if len(review)==0:
        form = GiveReviewForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.movie = movie
            obj.author = user
            obj.save()
            form = GiveReviewForm()
            return redirect('movies:review_detail', obj.slug)

        context['form']=form
        return render(request, 'give_movie_review.html', context)
    else:
        return redirect('movies:review_detail', review[0].slug)

def select_movie(request):

    movies = Movie.objects.all()
    context ={'movies':movies}

    return render(request, 'select_movie.html', context)

def review_detail(request, slug):
    context = {}
    review = get_object_or_404(MovieReview, slug=slug)
    context['review']=review

    return render(request, 'movies/review_detail.html', context)

def edit_review(request, slug):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('accounts:must_authenticate')

    review = get_object_or_404(MovieReview, slug=slug)
    if request.POST:
        form = UpdateReviewForm(request.POST or None, instance=review)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.update()
            context['success_message'] = "Updated"
            review = obj
    form = UpdateReviewForm(
            initial = {
                    "title": review.title,
                    "body": review.body,
                    "rating": review.rating,
                }
    )

    context['form'] = form
    return render(request, 'movies/edit_review.html', context)
