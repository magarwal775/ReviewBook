from django.shortcuts import get_object_or_404,render,redirect
from django.urls import reverse
from .models import Game



def index(request):
    game_list= Game.objects.order_by('-name')
    context = {'game_list':game_list}
    return render(request,'games/gamelist.html',context)

def details(request,game_id):
    game= get_object_or_404(Game,pk=game_id)
    return render(request,'games/details.html',{'game':game})
