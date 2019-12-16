from django.shortcuts import render, get_object_or_404, redirect

from games.models import GameReview, Game
from games.forms import GiveReviewForm
from accounts.models import Account

def give_game_review(request, game_id):

    context = {}

    user = request.user
    game = get_object_or_404(Game, id=game_id)
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = GiveReviewForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.game = game
        obj.author = user
        obj.save()
        form = GiveReviewForm()

    context['form']=form

    return render(request, 'give_game_review.html', context)

def select_game(request):
    games = Game.objects.all()
    context ={'games':games}

    return render(request, 'select_game.html', context)
