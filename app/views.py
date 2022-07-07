from asyncio.windows_events import NULL
from itertools import product
from pickle import NONE
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail, BadHeaderError, EmailMessage, get_connection
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from pathlib import Path
from .functions import *
from .models import *
from .forms import *


def homeView(request):
    if request.method == "POST":
        name = request.POST['message-name']
        email = request.POST['message-email']
        phone = request.POST['message-phone']
        message = request.POST['message']
        send_mail(
            'Message from ' + name +
            '(nr.tel.: ' + phone + '| email: ' + email + ')',  # subiect
            message,  # mesaj
            email,  # from email
            ['suport.marut@gmail.com', 'gabrieldan2399@gmail.com',
                'razvan_felecan@yahoo.com'],  # to email
        )
        return render(request, "base.html", {})
    else:
        return render(request, "base.html", {})


def aboutView(request):
    return render(request, "about.html", {})


def servicesView(request):
    return render(request, "services.html", {})


def productsView(request):
    return render(request, "products.html", {})


def termsView(request):
    return render(request, "terms.html", {})


def aluplast70View(request):
    return render(request, "aluplast70.html")


def rehau70View(request):
    return render(request, "rehau70.html")


def synegoView(request):
    return render(request, "synego.html")


def geneophzView(request):
    return render(request, "geneophz.html")


def usiView(request):
    return render(request, "usi.html")


def rulouriView(request):
    return render(request, "rulouri.html")


def cookiesView(request):
    return render(request, "cookies.html")


def registerView(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Account was succesfully created!')
            return redirect("login")

    context = {'form': form}
    return render(request, "register.html", context)


def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['profile.id'] = user.id
            return redirect("profile")
        else:
            messages.info(request, 'Username sau parola incorecte!')
            return render(request, "login.html", {})

    context = {}
    return render(request, "login.html", {})


@login_required(login_url='login')
def logoutView(request):
    if 'product_id' in request.session:
        del request.session['product_id']
    if 'quote_id' in request.session:
        del request.session['quote_id']
    if 'delete_id' in request.session:
        del request.session['delete_id']
    if 'profile.id' in request.session:
        del request.session['profile.id']
    logout(request)
    return redirect("login")


@login_required(login_url='login')
def profileView(request):
    if 'product_id' in request.session:
        del request.session['product_id']
    if 'quote_id' in request.session:
        del request.session['quote_id']
    quotes = Quote.objects.all()
    products = Product.objects.all()
    pqs = Product_in_Quote.objects.all()
    for quote in quotes:
        ok = False
        for pq in pqs:
            if quote.id == pq.quote.id:
                ok = True
        if not ok:
            Quote.objects.filter(id=quote.id).delete()
            quotes = Quote.objects.all()
    context = {'pqs': pqs, 'quotes': quotes}
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            request.user.first_name = form.cleaned_data['prenume']
            request.user.last_name = form.cleaned_data['nume']
            request.user.save()
            return HttpResponseRedirect('/profile/', context)
    else:
        form = ProfileForm(instance=profile)
        return render(request, "profile.html", context)


def quoteView(request):
    context = {}
    if 'product_id' in request.session:
        quote_id = request.session['quote_id']
        pq = Product_in_Quote.objects.all()
        quote = get_object_or_404(Quote, id=quote_id)
        context = {'pq': pq, 'quote': quote_id,
                   'suma': quote.suma+((quote.suma*30)/100)}
    else:
        if 'quote_id' not in request.session:
            if request.user.username != '':
                quote = Quote.objects.create(nume=request.user.last_name, prenume=request.user.first_name,
                                             email=request.user.email, telefon=request.user.profile.telefon, adresa=request.user.profile.adresa)
            else:
                quote = Quote.objects.create(
                    nume='a', prenume='a', email='a@yahoo.com', telefon='a', adresa='a')
            request.session['quote_id'] = quote.id
            pq = Product_in_Quote.objects.all()
            context = {'pq': pq, 'quote': quote.id, 'suma': quote.suma}

    return render(request, "quote.html", context)


def cancelquoteView(request):
    if 'product_id' in request.session:
        del request.session['product_id']
    if 'quote_id' in request.session:
        del request.session['quote_id']
    if 'delete_id' in request.session:
        del request.session['delete_id']
    return HttpResponseRedirect('/')


def addproductView(request):
    products = Product.objects.all()
    if request.method == "POST":
        nume = request.POST.get('nume')
        dimensiune = request.POST.get('dimensiune')
        dim = dimensiune.split('x')
        lungime = int(dim[0])
        inaltime = int(dim[1])
        deschidere = request.POST.get('deschidere')
        profil = request.POST.get('profil')
        culoare = request.POST.get('culoare')
        sticla = request.POST.get('sticla')
        for product in products:
            if findProduct(product, nume, profil, deschidere, lungime, inaltime, culoare, sticla):
                request.session['product_id'] = product.id
                product_id = request.session['product_id']
                product = Product.objects.get(id=product_id)
                quote_id = request.session['quote_id']
                quote = Quote.objects.get(id=quote_id)
                quote.suma += int(product.pret)
                quote.save()
                request.session['delete_id'] = quote_id
                Product_in_Quote.objects.create(product=product, quote=quote)
                return HttpResponseRedirect('/quote/')

    return render(request, "addproduct.html", {})


def deleteproductView(request, pk):
    product = get_object_or_404(Product_in_Quote, pk=pk)
    quote = get_object_or_404(Quote, id=product.quote.id)
    if request.method == "POST":
        product.delete()
        quote.suma -= product.product.pret
        quote.save()
        return redirect('/quote/')
    return render(request, "quote.html", {})


def submitquoteView(request):
    if 'product_id' in request.session:
        del request.session['product_id']
    if 'quote_id' in request.session:
        del request.session['quote_id']
    if 'delete_id' in request.session:
        del request.session['delete_id']
    if request.user.is_authenticated:
        return render(request, "submitquote.html", {'user': request.user})
    else:
        return render(request, "submitquote.html", {'user': ''})


def customquoteView(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.user.username
            email = request.user.email
            phone = request.user.profile.telefon
            message = request.POST['message']
            send_mail(
                'Message from ' + name +
                '(nr.tel.: ' + phone + '| email: ' + email + ')',  # subiect
                message,  # mesaj
                email,  # fom email
                ['suport.marut@gmail.com', 'gabrieldan2399@gmail.com',
                 'razvan_felecan@yahoo.com'],  # to email
                fail_silently=False
            )
            return HttpResponseRedirect("/submitquote/")
    else:
        if request.method == "POST":
            name = request.POST['message-name']
            email = request.POST['message-email']
            phone = request.POST['message-phone']
            message = request.POST['message']
            print(name)
            print(message)
            send_mail(
                'Message from ' + name +
                '(nr.tel.: ' + phone + '| email: ' + email + ')',  # subiect
                message,  # mesaj
                email,  # fom email
                ['suport.marut@gmail.com', 'gabrieldan2399@gmail.com',
                 'razvan_felecan@yahoo.com'],  # to email
                fail_silently=False
            )
            request.session['nume'] = name
            return HttpResponseRedirect("/submitquote/")

    return render(request, "customquote.html", {})


@login_required(login_url='login')
def deletequoteView(request, pk):
    quote = get_object_or_404(Quote, id=pk)
    if request.method == "POST":
        quote.delete()
        return redirect('/profile/')
    return render(request, "profile.html", {})


def answerquoteView(request, pk):
    connection = get_connection()
    connection.open()
    quote = get_object_or_404(Quote, id=pk)
    if request.method == 'POST':
        relative = Path("marut/pdf/" + request.POST.get('file'))
        abs = relative.absolute()
        msg = EmailMessage('Oferta MARUT', 'Aici ti-am atasat oferta solicitata!', request.user.email,
                           [quote.email], [request.user.email], connection=connection)
        msg.attach_file(path=abs)
        msg.send()
        quote.responded = True
        quote.save()
        return redirect('profile')
