from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from Music.models import *


def home(request):
    return render(request, 'base.html')


def album(request):
    all_albums = Album.objects.all()
    return render(request,'Home.html',{'albums': all_albums})


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exists")
    return render(request, 'detail.html', {'album': album})


def favorite(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'detail.html', {'album': album,'error_message':"You did not selected any Song"})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'detail.html', {'album': album})

