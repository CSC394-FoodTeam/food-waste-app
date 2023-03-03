from django.urls import path
from . import views

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
    path('discover/<id>', views.discover, name='discoverview'),
    path('book/', views.recipe, name='book'),
    path('recipe/<name>/', views.recipe, name='recipe'),
    path('feedback/', views.feedback, name='feedback'),


    # path('<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    # path('book/', views.RecipeCreateView.as_view(), name='book'),
    # path('<int:pk>/update/', views.RecipeUpdateView.as_view(), name='recipe_update'),
    # path('<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
    ###
]