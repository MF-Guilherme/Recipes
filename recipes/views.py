from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
from .models import *


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', {'recipes': recipes})


def category(request, category_id):
    recipes = Recipe.objects.filter(is_published=True).filter(category__id=category_id).order_by('-id')
    return render(request, 'recipes/pages/category.html', {'recipes': recipes})


def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipes/pages/recipe-view.html', {
        'recipe': recipe,
        'is_detail_page': True,
    })
    
