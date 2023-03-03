import jwt
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout as django_logout
from django.conf import settings

from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView

from .models import FridgeItem, PantryItem, Recipe
from .forms import FridgeItemForm, PantryItemForm, RecipeForm

# from django.contrib.auth import get_user_model

# from django.views.generic import View
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'home/base.html')


@login_required
def logout(request):
    django_logout(request)
    domain = settings.SOCIAL_AUTH_AUTH0_DOMAIN
    client_id = settings.SOCIAL_AUTH_AUTH0_KEY
    return_to = request.build_absolute_uri(reverse('index'))
    return redirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')


# def profile(request):
#     user = request.user

#     auth0_user = user.social_auth.get(provider='auth0')
    
#     user_data = {
#         'nickname': auth0_user.username,
#         'email': auth0_user.email,
#     }

#     context = {
#         'user_data':json.dumps(user_data, indent=4),
#         'auth0_user': auth0_user,
#     }

#     return render(request, 'profile.html')


# These are fast and flexible class-based views (refer to inventory.html to see how they're rendered) |-->

# class FridgeListView(View):

#     @method_decorator(login_required)

#     def dispatch(self, *args, **kwargs):
#         return super(FridgeListView, self).dispatch(*args, **kwargs)

#     def get(self, request):
#         items = FridgeItem.objects.all()
#         context = {
#             'f_items': items
#             }
#         return render(request, 'taproot/fridgeitem_list.html', context)

# class PantryListView(View):

#     @method_decorator(login_required)

#     def dispatch(self, *args, **kwargs):
#         return super(PantryListView, self).dispatch(*args, **kwargs)

#     def get(self, request):
#         items = PantryItem.objects.all()
#         context = {
#             'p_items': items
#         }
#         #return render(request, 'base.html', context)
#         return render(request, 'taproot/pantryitem_list.html', context)

# class RecipeListView(View):

#     @method_decorator(login_required)

#     def dispatch(self, *args, **kwargs):
#         return super(RecipeListView, self).dispatch(*args, **kwargs)

#     def get(self, request):
#         recipes = Recipe.objects.all()
#         context = {
#             'recipes': recipes
#         }
#         return render(request, 'taproot/inventory.html', context)
# 

@login_required
def fridge(request):
    fridge = FridgeItem.objects.filter(user=request.user)

    return render(request, 'home/fridge.html', {'fridge' : fridge})


@login_required
def fridgeCreate(request):
    form = FridgeItemForm()
    if request.method == 'POST':
        form = FridgeItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('/fridgelist')
        else:
            print(form.errors)
    else:
        form = FridgeItemForm()

    context={'form' : form}
    return render(request, 'components/fridgecreate_view.html', context)


@login_required
def fridgeUpdate(request, id):
    obj = get_object_or_404(FridgeItem, id = id)
    form = FridgeItemForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/fridgelist/')

    context={'form' : form}
    return render(request, 'components/fridgeupdate_view.html', context)


@login_required
def fridgeDelete(request, id):
    obj = get_object_or_404(FridgeItem, id = id)
    
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect('/fridgelist/')

    context={'item_name': obj.item_name}
    
    return render(request, 'components/fridgedelete_view.html', context)

@login_required
def fridgeDeleteAll(request):
    userFridge = FridgeItem.objects.filter(user=request.user)

    if request.method == 'POST':
        userFridge.delete()
        return HttpResponseRedirect('/fridgelist/')
    return render(request, 'components/fridgeDeleteAll_view.html')

# <----- Fridge views above / Pantry views below ----->


@login_required
def pantry(request):
    pantry = PantryItem.objects.filter(user=request.user)

    return render(request, 'home/pantry.html', {'pantry' : pantry})


@login_required
def pantryCreate(request):
    form = PantryItemForm()
    if request.method == 'POST':
        form = PantryItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('/pantrylist/')
        else:
            print(form.errors)
    else:
        form = PantryItemForm()

    context={'form' : form}
    return render(request, 'components/pantrycreate_view.html', context)


@login_required
def pantryUpdate(request, id):
    obj = get_object_or_404(PantryItem, id = id)
    form = PantryItemForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/pantrylist/')

    context={'form': form}
    return render(request, 'components/pantryupdate_view.html', context)


@login_required
def pantryDelete(request, id):
    obj = get_object_or_404(PantryItem, id = id)

    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect('/pantrylist/')

    context={'item_name': obj.item_name}
    
    return render(request, 'components/pantrydelete_view.html', context)

@login_required
def pantryDeleteAll(request):
    userPantry = PantryItem.objects.filter(user=request.user)

    if request.method == 'POST':
        userPantry.delete()
        return HttpResponseRedirect('/pantrylist/')
    return render(request, 'components/pantryDeleteAll_view.html')


##/FAQ/##
def faq(request):
    return render(request, 'home/faq.html')


def discover(request):
    form = RecipeForm()

    context={'form' : form}

    return render(request, 'home/discover.html', context)


# class BookView(CreateView):
#     model = Recipe
#     form_class = RecipeForm
#     template_name = 'home/book.html'

def recipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('/book/')
        else:
            print(form.errors)
    else:
        form = RecipeForm()

    context={'form' : form}
    return render(request, 'home/book.html', context)



# CANNY.IO WIDGET
# def create_canny_token(user):
#   private_key = settings.CANNYIO_PRIVATE_KEY
#   user_data = {
#     'email': user.email,
#     'id': user.id,
#     'username': user.username,
#   }
#   return jwt.encode(user_data, private_key, algorithm='HS256')

def feedback(request):
    # context = {'create_canny_token': create_canny_token(user=request.user)}
    return render(request, 'home/feedback.html')

###