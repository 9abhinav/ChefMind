# myapp/views.py
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout
from .models import Recipe


def home(request):
    query = request.GET.get('search', '')  # Get the search term from the request
    if query:
        recipes = Recipe.objects.filter(name__icontains=query)  # Case-insensitive search on the name
    else:
        recipes = Recipe.objects.all()  # Return all recipes if no search term
        
        # Add a 'is_favorited' field for each recipe
        for recipe in recipes:
            recipe.is_favorited = recipe.favorites.filter(id=request.user.id).exists() if request.user.is_authenticated else False
    return render(request, 'home.html', {'recipes': recipes, 'query': query})

def recipe_details(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipe_details.html', {'recipe': recipe})

@login_required
def add_to_favorites(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.favorites.filter(id=request.user.id).exists():
        recipe.favorites.remove(request.user)  # Remove if already in favorites
    else:
        recipe.favorites.add(request.user)  # Add to favorites
    return redirect('home')  # Redirect to the recipe list page

@login_required
def favorite_recipes(request):
    recipes = request.user.favorite_recipes.all()  # Get all recipes favorited by the user
    return render(request, 'favorite_recipes.html', {'recipes': recipes})

def recipe_search(request):
    recipes = []
    query = request.GET.get('ingredients', '')  # Get ingredients input from the user
    if query:
        ingredients = query.split(',')  # Split ingredients by comma
        # Filter recipes that contain any of the ingredients
        for ingredient in ingredients:
            ingredient = ingredient.strip()  # Remove extra spaces
            recipes += Recipe.objects.filter(ingred_html__icontains=ingredient)
        # Eliminate duplicates if multiple ingredients matched the same recipe
        recipes = list(set(recipes))
    return render(request, 'recipe_by_ingred.html', {'recipes': recipes, 'query': query})

def pasta(request):
    return render(request, 'recipe_details_pasta.html')
def cake(request):
    return render(request, 'recipe_details_chocolate_cake.html')
def smoothie(request):
    return render(request, 'recipe_details_smoothie.html')
def tacos(request):
    return render(request, 'recipe_details_vegan_tacos.html')
def chicken(request):
    return render(request, 'recipe_details_chicken_curry.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in
            return redirect('home')  # Redirect to profile after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to profile after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile_settings(request):
    return render(request, 'profile.html')

@login_required  # Ensure only logged-in users can access this view
def logout_view(request):
    logout(request)  # Log out the user
    return redirect('login')  # Redirect to the login page

