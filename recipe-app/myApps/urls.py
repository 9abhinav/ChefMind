from django.contrib import admin
from django.urls import path
from recipeApp import views  # Import the view
from django.urls import include, path
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Map the root URL to the hello view
    path('recipe/<int:id>/', views.recipe_details, name='recipe-details'),
    path('recipe-search/', views.recipe_search, name='recipe-search'),
    path('add-to-favorites/<int:recipe_id>/', views.add_to_favorites, name='add-to-favorites'),
    path('favorite-recipes/', views.favorite_recipes, name='favorite-recipes'),
    path('pasta/', views.pasta, name='pasta'),  # Map the root URL to the hello view
    path('cake/', views.cake, name='cake'),  # Map the root URL to the hello view
    path('smoothie/', views.smoothie, name='smoothie'),  # Map the root URL to the hello view
    path('tacos/', views.tacos, name='tacos'),  # Map the root URL to the hello view
    path('chicken/', views.chicken, name='chicken'),  # Map the root URL to the hello view
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile-settings/', views.profile_settings, name='profile_settings'),
]

