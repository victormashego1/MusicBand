from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Music, Choice
from django.template import loader


# Create your views here.
def index(request):
    return render(request, "musicband/home.html")


def about(request):
    return render(request, "musicband/about.html")


@login_required(login_url="/user_auth/login")
def records(request):
    # return HttpResponse("Hello world. You're at the  index.")
    latest_record_list = Music.objects.order_by('-pub_date')[:5]
    context = {'latest_record_list': latest_record_list}
    return render(request, "musicband/records.html", context)


def musicband(request):
    template = loader.get_template('musicband/home.html')
    return HttpResponse(template.render())


#
def detail(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    return render(request, 'musicband/detail.html', {'music': music})


# @login_required(login_url="/user_auth/login")
def vote(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    try:
        selected_choice = music.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the music voting form.
        return render(
            request,
            "musicband/detail.html",
            {
                "music": music,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("musicband:index", args=(music.id,)))
