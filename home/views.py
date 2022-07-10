from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Category, Product


# Create your views here.
@login_required
def index(request):
    """ A view to return the index page """

    products = Product.objects.all().order_by(
        'diameter',
        'width',
        'height',
        'rim_diameter',
        'price'
        )
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'home/index.html', context)
