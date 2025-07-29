from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from listings.models import Band, Article
from listings.forms import ListingForm, BandForm, ContactUsForm

def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)

        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    
    return render(request,
                  'listings/band_create.html',
                  {'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request,
                  'listings/band-update.html',
                  {'form': form, 'band': band})

def about(request):
    return render(request, 'listings/about.html')

def listings_list(request):
    articles = Article.objects.all()
    return render(request, 'listings/listings_list.html',
                  {'articles': articles})

def listings_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request,
                  'listings/listings_detail.html',
                  {'article': article})

def listings_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)

        if form.is_valid():
            article = form.save()
            return redirect(request, 'listings-list', article.id)
    else:
        form = ListingForm()

    return render(request,
                  'listings/listings_create.html',
                  {'form': form})

def listings_update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect('listings-detail', article.id)
    else:
        form = ListingForm(instance=article)
    
    return render(request,
                  'listings/listings_update.html',
                  {'form': form, 'article': article})

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data['name'] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchx.xyz'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()

    return render(request,
                  'listings/contact.html',
                  {'form': form})

def email_sent(request):
    return render(request,
                  'listings/email_sent.html')