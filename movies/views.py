from django.shortcuts import get_object_or_404,render,redirect
from django.urls import reverse
from .models import Movie



def index(request):
    movie_list= Movie.objects.order_by('-name')
    context = {'movie_list':movie_list}
    return render(request,'movies/movielist.html',context)

def details(request,movie_id):
    movie= get_object_or_404(Movie,pk=movie_id)
    return render(request,'movies/details.html',{'movie':movie})


# Create your views here.
