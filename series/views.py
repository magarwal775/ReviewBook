from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from series.models import EpisodeReview, Series, Episode
from series.forms import GiveReviewForm, UpdateReviewForm
from accounts.models import Account

def give_episode_review(request, episode_id):

    context = {}

    user = request.user
    episode = get_object_or_404(Episode, id=episode_id)
    if not user.is_authenticated:
        return redirect('accounts:must_authenticate')

    review = EpisodeReview.objects.filter(episode_id=episode_id, author=request.user)
    if len(review)==0:
        form = GiveReviewForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.episode = episode
            obj.author = user
            obj.save()
            form = GiveReviewForm()
            return redirect('series:review_detail', obj.slug)

        context['form']=form
        return render(request, 'give_episode_review.html', context)
    else:
        return redirect('series:review_detail', review[0].slug)

def select_series(request):
    series = Series.objects.all()
    context = {'series':series}

    return render(request, 'select_series.html', context)

def select_episode(request, series_id):
    episodes = Episode.objects.filter(show_name_id=series_id)
    context = {'episodes':episodes}

    return render(request, 'select_episode.html', context)

def review_detail(request, slug):
    context = {}
    review = get_object_or_404(EpisodeReview, slug=slug)
    context['review']=review

    return render(request, 'series/review_detail.html', context)

def edit_review(request, slug):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('accounts:must_authenticate')

    review = get_object_or_404(EpisodeReview, slug=slug)
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
    return render(request, 'series/edit_review.html', context)
