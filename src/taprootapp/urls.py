from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout, name='logout'),

    path('fridge/', views.fridge, name = 'fridge'),
    path('pantry/', views.pantry, name = 'pantry'),

    # ###
    path('fridgecreate/', views.fridgeCreate, name= 'fridgecreate'),
    path('fridgeupdate/<id>/', views.fridgeUpdate, name = 'fridgeupdate'),
    path('fridgedelete/<id>/', views.fridgeDelete, name = 'fridgedelete'),
    path('fridgedeleteall/', views.fridgeDeleteAll, name = 'fridgeDeleteAll'),

    path('pantrycreate/', views.pantryCreate, name = 'pantrycreate'),
    path('pantryupdate/<id>/', views.pantryUpdate, name = 'pantryupdate'),
    path('pantrydelete/<id>/', views.pantryDelete, name = 'pantrydelete'),
    path('pantrydeleteall/', views.pantryDeleteAll, name = 'pantryDeleteAll'),

    path('faq/', views.faq, name='faq'),
    path('discover/', views.discover, name='discover'),
    path('discover/<name>', views.discover, name='discoverview'),
    path('recipe/', views.recipeCreate, name='recipe'),
    path('feedback/', views.feedback, name='feedback'),


    # path('<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('book/', login_required(views.BookView.as_view()), name='book'),
    # path('<int:pk>/update/', views.RecipeUpdateView.as_view(), name='recipe_update'),
    # path('<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
    ###
]