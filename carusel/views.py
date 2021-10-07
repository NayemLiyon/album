from django.shortcuts import render
from .models import Carusel

# Create your views here.
def index(request):

    caru = Carusel.objects.all()
    contex={
      'caru':caru
    }

    return render(request,'carusel/index.html',contex)