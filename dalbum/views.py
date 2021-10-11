from django.shortcuts import render

from dalbum.forms import AddForms
from .models import Album
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView,DeleteView,UpdateView
from django.urls import reverse

from dalbum import models
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class AlbumCreate(LoginRequiredMixin,CreateView):
    model = Album
    form_class = AddForms
    template_name = 'dalbum/create.html'
    success_url = '/dalbum'


class Delete(DeleteView):
    template_name = 'dalbum/delete.html'

    def get_object(self):

        id = self.kwargs.get("id")
        return get_object_or_404(Album, id=id)

    def get_success_url(self):
        return reverse('dalbum:index')


class Update(UpdateView):
    
    template_name = 'dalbum/update.html'
    form_class = AddForms
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Album, id=id)
    
    def get_success_url(self):
        return reverse('dalbum:index')



def index(request):

    album_data = Album.objects.all()
    contex={
        'album_data' : album_data
    }

    return render(request,'dalbum/index.html',contex)