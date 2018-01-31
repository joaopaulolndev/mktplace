from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from portal.models import Product, Category


def home(request):
    categories = Category.objects.filter(hidden=False, parent__isnull=True) \
        .exclude(categories__isnull=True) \
        .order_by('name')

    context = {
        'categories': categories
    }

    return render(request, 'portal/home.html', context)
