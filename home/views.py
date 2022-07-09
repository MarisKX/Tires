from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    """ A view to return the index page """
  
    context = {
    }
    return render(request, 'home/index.html', context)
