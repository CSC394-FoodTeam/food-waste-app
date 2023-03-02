from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout, name='logout'),

    path('fridgelist/', views.fridge, name = 'fridgelist'),
    path('pantrylist/', views.pantry, name = 'pantrylist'),

    # ###
    path('fridgecreate/', views.fridgeCreate, name= 'fridgecreate'),
    path('fridgeupdate/<id>/', views.fridgeUpdate, name = 'fridgeupdate'),
    path('fridgedelete/<id>/', views.fridgeDelete, name = 'fridgedelete'),

    path('pantrycreate/', views.pantryCreate, name = 'pantrycreate'),
    path('pantryupdate/<id>/', views.pantryUpdate, name = 'pantryupdate'),
    path('pantrydelete/<id>/', views.pantryDelete, name = 'pantrydelete'),
    path('faq/', views.faq, name='faq'),
    path('discover/', views.discover, name='discover'),
    path('book/', views.BookView.as_view(), name='book'),
    path('recipe/<name>/', views.recipe, name='recipe'),
    path('feedback/', views.feedback, name='feedback'),


    # path('<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    # path('book/', views.RecipeCreateView.as_view(), name='book'),
    # path('<int:pk>/update/', views.RecipeUpdateView.as_view(), name='recipe_update'),
    # path('<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
    ###
]