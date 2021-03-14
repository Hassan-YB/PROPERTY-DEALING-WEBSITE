from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect
from .models import Citie,Categorie,Area,Offer,Bathroom,Bedroom,Property,Mail
from .forms import SearchForm , ContactForm ,SubscribeForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


def properties(request):
    properties=Property.objects.all
    a=""
    b=""
    c=0
    d=0
    e=""
    context={'properties':properties}
    if request.method=='POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            a=str(form.cleaned_data['City'])
            b=str(form.cleaned_data['Categorie'])
            c=str(form.cleaned_data['Bathrooms'])
            d=str(form.cleaned_data['Bedrooms'])
            e=str(form.cleaned_data['Area'])
            context={'properties':properties,'form':form,'a':a,'b':b,'c':c,'d':d,'e':e}
    else:
        form=SearchForm()
    return render(request,'dealer/properties.html',context)        
    
def home(request):
    properties=Property.objects.all
    return render(request,'dealer/index.html',{'properties':properties})

def gallery(request):
   photos = Photo.objects.all()
   return render(request, 'gallery.html', {'photos': photos})

def contact(request):
    properties=Property.objects.all
    context={'properties':properties}
    subject="Hello"
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = 'hassanbaras5@gmail.com'
            recipients = [form.cleaned_data['sender']]
            fail_silently=False
            send_mail(subject, message, sender, recipients, fail_silently)
            context={'properties':properties,'form':form,'subject':subject}
    else:
        form=ContactForm()
    return render(request,'dealer/contact.html',context)



def aboutus(request):
    properties=Property.objects.all
    return render(request,'dealer/about.html',{'properties':properties})

def news(request):
    properties=Property.objects.all
    return render(request,'dealer/news.html',{'properties':properties})

def lahore(request):
    properties=Property.objects.all
    return render(request,'dealer/lahore.html',{'properties':properties})

def karachi(request):
    properties=Property.objects.all
    return render(request,'dealer/karachi.html',{'properties':properties})

def islamabad(request):
    properties=Property.objects.all
    return render(request,'dealer/islamabad.html',{'properties':properties})

def detail(request,property_id):
    property_detail=get_object_or_404(Property,pk=property_id)
    return render(request,'dealer/property.html',{'property_detail':property_detail})

def cart(request):
    properties=Property.objects.all
    return render(request,'dealer/cart.html',{'properties':properties})

def login(request):
    properties=Property.objects.all
    return render(request,'dealer/login.html',{'properties':properties})

@login_required(login_url="/accounts/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Property.objects.get(id=id)
    cart.add(product=product)
    return HttpResponseRedirect("/")


@login_required(login_url="/accounts/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Property.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required(login_url="/accounts/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Property.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="/accounts/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Property.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


@login_required(login_url="/accounts/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


@login_required(login_url="/accounts/login")
def cart(request):
    properties=Property.objects.all
    return render(request, 'dealer/cart.html',{'properties':properties})