from django.http.response import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    current_page = request.GET.get('page', 1)  # noqa | pegando o page da query string, se não passar nada é 1
    paginator = Paginator(recipes, 9)  # noqa | paginando e exibindo de 9 em 9 por página
    page_obj = paginator.get_page(current_page)
    return render(request, 'recipes/pages/home.html', {'recipes': page_obj})


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(is_published=True, category__id=category_id)
        .order_by('-id'))
    title = f'{recipes[0].category.name} - Category |'

    return render(request, 'recipes/pages/category.html', {
        'recipes': recipes,
        'title': title})


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)

    return render(request, 'recipes/pages/recipe-view.html', {
        'recipe': recipe,
        'is_detail_page': True,
    })


def search(request):
    search_term = request.GET.get('q', '').strip()
    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(title__icontains=search_term) |
        Q(description__icontains=search_term),
    ).filter(Q(is_published=True)).order_by('-id')

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}"',
        'search_term': search_term,
        'recipes': recipes,
    })
