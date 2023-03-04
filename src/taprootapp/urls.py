from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    #path('login/auth0/', None, name = 'login'),

    path('fridgelist/', views.fridge, name = 'fridgelist'),
    path('fridgecreate/', views.fridgeCreate, name= 'fridgecreate'),
    path('fridgeupdate/<id>/', views.fridgeUpdate, name = 'fridgeupdate'),
    path('fridgedelete/<id>/', views.fridgeDelete, name = 'fridgedelete'),
    path('fridgedeleteall/', views.fridgeDeleteAll, name = 'fridgeDeleteAll'),

    path('pantrylist/', views.pantry, name = 'pantrylist'),
    path('pantrycreate/', views.pantryCreate, name = 'pantrycreate'),
    path('pantryupdate/<id>/', views.pantryUpdate, name = 'pantryupdate'),
    path('pantrydelete/<id>/', views.pantryDelete, name = 'pantrydelete'),
    path('pantrydeleteall/', views.pantryDeleteAll, name = 'pantryDeleteAll'),

    path('faq/', views.faq, name='faq'),
    #path('discover/', views.discover, name='discover'),
    #path('discover/<id>/', views.discoverInstance, name='discoverview'),
    path('book/', views.recipe, name='book'),
    path('recipe/<name>/', views.recipe, name='recipe'),
    path('feedback/', views.feedback, name='feedback'),
    
    # path('<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    # path('book/', views.RecipeCreateView.as_view(), name='book'),
    # path('<int:pk>/update/', views.RecipeUpdateView.as_view(), name='recipe_update'),
    # path('<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
    ###
]
urlpatterns2 = [
    path('discover/', views.discover, name='discover'),
    path('discover/<id>', views.discoverInstance, name='discoverview'),
]


#urlpatterns2 += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
for i in urlpatterns2:
    urlpatterns.append(i)
