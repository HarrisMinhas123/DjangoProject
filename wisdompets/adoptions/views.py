from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import ProductModelForm, Add_Product
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
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Add_Product(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            product_name = form.cleaned_data['product_name']
            category_name = form.cleaned_data['category_name']
            description = form.cleaned_data['description']
            products.objects.create(product_name=product_name, category_name = category_name, description=description,)
            return redirect('dashboard')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Add_Product()

    return render(request, 'create_product.html', {'form': form})

def delete_product(request, product_name):
    print("Its working!")
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        # process the data in form.cleaned_data as required
        print("Inside delete")
        product = products.objects.get(product_name=product_name)
        product.delete()
        context ={
        "data":"Gfg is the best",
        "count" :products.objects.count(),
        "products" :products.objects.all()

        }
        # if a GET (or any other method) we'll create a blank form
    else:
        return True

    return render(request, 'dashboard.html', context)