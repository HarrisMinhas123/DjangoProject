from adoptions.models import products
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import ProductModelForm
from .models import products


# Create your views here.
def products_view(request):
    # create a dictionary to pass
    # data to the template
    context ={
        "data":"Gfg is the best",
        "count" :products.objects.count(),
        "products" :products.objects.all()

    }
    print(context)
    # return response with template and context
    return render(request, "geeks.html", context)

def indexView(request):
    return render(request,'index.html')
@login_required()
def dashboardView(request):
    context ={
        "data":"Gfg is the best",
        "count" :products.objects.count(),
        "products" :products.objects.all()

    }
    return render(request,'dashboard.html', context)
def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})

def create_product(request):
    print("We here")
    return render(request,'create_product.html')