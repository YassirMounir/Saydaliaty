# from queue import Empty
from ast import Not
from collections import UserList
from genericpath import exists
from queue import Empty
from sqlite3 import Row
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django. shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Medicament, Commande, Clients
from urllib import request
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import ClientForm, ClientLogin
from django.contrib.sessions.models import Session
from django.db import connection


def home(request):
    User = get_user_model()
    costumers = User.objects.all()
    meds = Medicament.objects.raw(
        'select * from playgroubd_medicament ')
    return render(request, 'Templates/Home.html', {'medicament': meds})


def med_search(request):
    meds = ''
    if request.method == 'GET' and 'med_name' in request.GET:
        if request.GET.get('med_name') == '':
            #   redirect('/products')
            return home(request)
        else:
            meds = Medicament.objects.raw(
                'select * from playgroubd_medicament where UPPER(mdc_name) = UPPER(\''+request.GET.get('med_name')+'\')')
    return render(request, 'Templates/home.html', {'medicament': meds})


# def products(request):
    # meds = Medicament.objects.raw(
    # 'select * from playgroubd_medicament ')
    # meds =
    # meds.objects
    # costumers = Clients.objects.raw('select * from playgroubd_Clients where clt_login = \'Hamid@gmail.com\' and clt_mdp = \'123\'')
    # costumers = Clients.objects.filter(
    #     clt_login='Hamid@gmail.com', clt_mdp='13').values()
    # return render(request, 'Templates/products.html', {'medicament': meds})

def profile(request):

    form = ClientForm()
    if request.method == 'POST':
        user = request.user
        form = Clients.objects.filter(CU_id_id=user.id)
        if form.exists():

            Clients.objects.filter(CU_id_id=user.id).update(clt_lastname=request.POST.get('clt_lastname'), clt_firstname=request.POST.get('clt_firstname'), clt_tel=request.POST.get(
                'clt_tel'), clt_city=request.POST.get('clt_city'), clt_zip=request.POST.get('clt_zip'), clt_adresse=request.POST.get('clt_adresse'))

        else:

            Clients.objects.create(CU_id_id=user.id, clt_lastname=request.POST.get('clt_lastname'), clt_firstname=request.POST.get('clt_firstname'), clt_tel=request.POST.get(
                'clt_tel'), clt_city=request.POST.get('clt_city'), clt_zip=request.POST.get('clt_zip'), clt_adresse=request.POST.get('clt_adresse'))

        return redirect('/home')
    return render(request, 'Templates/profile.html', {'form': form})


def signin(request):
    if request.method == 'POST':

        User = authenticate(request)

        if User is not None:
            login(request, User)
            messages.success(request, 'User was Logged In Successfully')
            return redirect('')
        else:
            messages.info(request, 'Email Or Password Is Incorrect')
            return redirect('/signin')

    return render(request, 'Templates/signin.html')


# def signup(request):

#     form = ClientCreateAccount()
#     if request.method == 'POST':
#         pass1 = request.POST.get('clt_mdp')
#         pass2 = request.POST.get('confirmpass')
#         if pass1 == pass2:
#             form = ClientCreateAccount(request.POST)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'User was Created for ' +
#                                  form.cleaned_data.get('clt_login') + ' Successfully')
#                 return redirect('/signin')
#         else:
#             context = {'form': form,
#                        'err': 'Passwords Do Not Match ! Try Again .'}
#             return render(request, 'Templates/signup.html', context)

#     context = {'form': form}
#     return render(request, 'Templates/signup.html', context)


# def cart(request):
#     cmd = Commande.objects.all()
#     return render(request, 'Templates/cart.html', {'commands': cmd})


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'Templates/signin'
    success_url = reverse_lazy('signin/')
