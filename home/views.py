from django.shortcuts import render
from home.models import Contact
from django.contrib import messages

def index(request):
  
    return render(request,'index.html')
def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        contact = Contact(name=name , email = email)
        contact.save()
        messages.success(request,"Your form is submitted succesfully")
    return render(request,'contact.html')
def checkout(request):
    return render(request,'checkout.html')
def sale(request):
    return render(request,'sale.html')
def offers(request):
    return render(request,'offer.html')
def phone(request):
    return render(request,'phone.html')
def womenoffer(request):
    return render(request,'womenoffer.html')
def login(request):
    return render(request,'login.html')
