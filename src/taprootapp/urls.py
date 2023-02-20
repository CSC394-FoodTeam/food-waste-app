from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout, name='logout'),

    # path('profile/', views.profile, name='profile'),

    path("fridgelist/", views.fridge, name = "fridgelist"),
    path("pantrylist/", views.pantry, name = "pantrylist"),
    # # path('inventory/', RecipeListView.as_view(), name='inventory'),

    # ###
    path('fridgecreate/', views.fridgeCreate, name= "fridgecreate"),
    path("fridgeupdate/<item_name>/", views.fridgeUpdate, name = "fridgeupdate"),
    path("fridgedelete/<item_name>/", views.fridgeDelete, name = "fridgedelete"),

    path("pantrycreate/", views.pantryCreate, name = "pantrycreate"),
    path("pantryupdate/<item_name>/", views.pantryUpdate, name = "pantryupdate"),
    path("pantrydelete/<item_name>/", views.pantryDelete, name = "pantrydelete"),
    ###
]