import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from urllib.parse import quote_plus, urlencode

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
            'pretty': json.dumps(request.session.get('user'), indent=4),
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
        return render(request, 'base.html', context)

class PantryListView(View):

    @method_decorator(login_required)

    def dispatch(self, *args, **kwargs):
        return super(PantryListView, self).dispatch(*args, **kwargs)

    def get(self, request):
        items = PantryItem.objects.all()
        context = {
            'p_items': items
        }
        return render(request, 'base.html', context)

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