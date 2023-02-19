import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
###
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.shortcuts import (get_object_or_404,render, HttpResponseRedirect)
###
from .models import *
from .forms import *

from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

oauth = OAuth()

oauth.register(
    'auth0',
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        'scope': 'openid profile email',
    },
    server_metadata_url=f'https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration',
)

def index(request):
    return render(
        request,
        'base.html',
        context={
            'session': request.session.get('user'),
        },
    )


# def index(request):
#     if request.method == 'FRIDGEITEM':
#         form = FridgeItemForm(request.FRIDGEITEM)

#         if form.is_valid():
#             fridge_item = form.save(commit=False)
#             fridge_item.user = request.user
#             fridge_item.save()
#             return redirect('base')
#         else:
#             form =  FridgeItemForm()

#         context = {'form': form}

#         return render(request, 'taproot/base.html', context)

def profile(request):
    return render(
        request,
        'profile.html',
        context={
            'pretty': json.dumps(request.session.get('user'), indent=4),
        },
    )


def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session['user'] = token
    return redirect(request.build_absolute_uri(reverse('index')))


def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse('callback'))
    )


def logout(request):
    request.session.clear()

    return redirect(
        f'https://{settings.AUTH0_DOMAIN}/v2/logout?'
        + urlencode(
            {
                'returnTo': request.build_absolute_uri(reverse('index')),
                'client_id': settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

# These are fast and flexible class-based views (refer to inventory.html to see how they're rendered) |-->

class FridgeListView(View):

    @method_decorator(login_required)

    def dispatch(self, *args, **kwargs):
        return super(FridgeListView, self).dispatch(*args, **kwargs)

    def get(self, request):
        items = FridgeItem.objects.all()
        context = {
            'f_items': items
            }
        return render(request, 'taproot/fridgeitem_list.html', context)

class PantryListView(View):

    @method_decorator(login_required)

    def dispatch(self, *args, **kwargs):
        return super(PantryListView, self).dispatch(*args, **kwargs)

    def get(self, request):
        items = PantryItem.objects.all()
        context = {
            'p_items': items
        }
        #return render(request, 'base.html', context)
        return render(request, 'taproot/pantryitem_list.html', context)

class RecipeListView(View):

    @method_decorator(login_required)

    def dispatch(self, *args, **kwargs):
        return super(RecipeListView, self).dispatch(*args, **kwargs)

    def get(self, request):
        recipes = Recipe.objects.all()
        context = {
            'recipes': recipes
        }
        return render(request, 'inventory.html', context)

###
##/Fridge/##
#@method_decorator(login_required)
def fridgeCreate(request):
    form = FridgeTestForm()
    if request.method == 'POST':
        form = FridgeTestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/fridgelist")
    context={'form' : form}
    return render(request, 'fridge_item_creation.html', context)

#@method_decorator(login_required)
def updateFridge(request, item_name):
    context = {}
    obj = get_object_or_404(FridgeItem, item_name = item_name)
    form = FridgeTestForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        #return HttpResponseRedirect("/" + item_name)
        return HttpResponseRedirect("/fridgelist/")

    context['form'] = form
    return render(request, 'fridgeupdate_view.html', context)

#@method_decorator(login_required)
def fridgeDelete(request, item_name):
    context = {}
    obj = get_object_or_404(FridgeItem, item_name = item_name)
    
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/fridgelist/")
    
    return render(request, "fridgedelete_view.html", context)

#@method_decorator(login_required)
def fridge(request):
    fridge = FridgeItem.objects.all()

    return render(request, 'fridgeitem_list.html', {'fridge' : fridge})
##/Fridge/##
##/Pantry/##

#@method_decorator(login_required)
def pantryCreate(request):
    form = PantryTestForm()
    if request.method == 'POST':
        form = PantryTestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/pantrylist/")
    context={'form' : form}
    return render(request, 'pantry_item_creation.html', context)

#@method_decorator(login_required)
def updatePantry(request, item_name):
    context = {}
    obj = get_object_or_404(PantryItem, item_name = item_name)
    form = PantryTestForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        #return HttpResponseRedirect("/" + item_name)
        return HttpResponseRedirect("/pantrylist/")

    context['form'] = form
    return render(request, 'pantryupdate_view.html', context)

#@method_decorator(login_required)
def pantryDelete(request, item_name):
    context = {}
    obj = get_object_or_404(PantryItem, item_name = item_name)
    
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/pantrylist/")
    
    return render(request, "pantrydelete_view.html", context)

#@method_decorator(login_required)
def pantry(request):
    pantry = PantryItem.objects.all()

    return render(request, 'pantryitem_list.html', {'pantry' : pantry})
##/Pantry/##

##/FAQ/##
def faq(request):
    return render(request, 'faq.html')
##/FAQ/##
#class FridgeTestCreate(CreateView):
   # model = FridgeItem
   # template_name = 'fridge_item_creation.html'
   # form_class = FridgeTestForm

class PantryCreate(CreateView):
    model = PantryItem
    template_name = "pantry_item_create.html"
    form_class = PantryTestForm

class FridgeList(ListView):
    model = FridgeItem

class PantryList(ListView):
    model = PantryItem

###