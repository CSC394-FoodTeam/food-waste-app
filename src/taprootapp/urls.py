from django.urls import path
from . import views
from django.views.generic import CreateView

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout, name='logout'),

    path('fridgelist/', views.fridge, name = 'fridgelist'),
    path('pantrylist/', views.pantry, name = 'pantrylist'),

    # ###
    path('fridgecreate/', views.fridgeCreate, name= 'fridgecreate'),
    path('fridgeupdate/<item_name>/', views.fridgeUpdate, name = 'fridgeupdate'),
    path('fridgedelete/<item_name>/', views.fridgeDelete, name = 'fridgedelete'),
    path('fridgedeleteall/', views.fridgeDeleteAll, name = 'fridgeDeleteAll'),

    path('pantrycreate/', views.pantryCreate, name = 'pantrycreate'),
    path('pantryupdate/<item_name>/', views.pantryUpdate, name = 'pantryupdate'),
    path('pantrydelete/<item_name>/', views.pantryDelete, name = 'pantrydelete'),
    path('pantrydeleteall/', views.pantryDeleteAll, name = 'pantryDeleteAll'),
    path('faq/', views.faq, name='faq'),
    path('discover/', views.discover, name='discover'),
    path('book/', views.BookView.as_view(), name='book'),
    path('recipe/<name>/', views.recipe, name='recipe')
    ###
]