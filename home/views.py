from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Category, Product


# Create your views here.
@login_required
def index(request):
    """ A view to return the index page """

    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'home/index.html', context)
