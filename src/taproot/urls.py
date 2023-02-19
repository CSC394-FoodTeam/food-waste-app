"""taproot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import RecipeListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login, name='login/'),
    path('logout', views.logout, name='logout'),
    path('callback', views.callback, name='callback'),
    path('profile', views.profile, name='profile'),
    path('inventory', RecipeListView.as_view(), name='inventory'),

    ###
    #path('fridge/create', views.FridgeTestCreate.as_view(), name= "fridgecreate"),
    path('fridgecreate/', views.fridgeCreate, name= "fridgecreate"),
    path("fridgelist/", views.fridge, name = "fridgelist"),
    path("fridgeupdate/<item_name>/", views.updateFridge, name = "fridgeupdate"),
    path("fridgedelete/<item_name>/", views.fridgeDelete, name = "fridgedelete"),

    path("pantrycreate/", views.pantryCreate, name = "pantrycreate"),
    path("pantrylist/", views.pantry, name = "pantrylist"),
    path("pantryupdate/<item_name>/", views.updatePantry, name = "pantryupdate"),
    path("pantrydelete/<item_name>/", views.pantryDelete, name = "pantrydelete"),
     path('faq/', views.faq, name='faq'),
    ###

]
