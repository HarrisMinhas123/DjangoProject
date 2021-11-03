from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import Add_Product, Update_Product
from .models import products
from django.contrib.auth.hashers import make_password
import json
from django.views.decorators.csrf import csrf_exempt


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
    hashed_pass = make_password("~]p`Xq7K5)d(Y#5J")
    print(hashed_pass)
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

def search_product(request):
    try:
        if request.method == 'GET':
            category_name = request.GET['category_name']
            print(category_name)
            products_list = products.objects.filter(category_name=category_name).all()
            return render(request, 'dashboard.html', {'products': products_list})
    
    except:
        return False

def update_product(request, product_name):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(products, product_name=product_name)
    # pass the object as instance in form
    form = Update_Product(instance=obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    print(form)
    # add form dictionary to context
    context["form"] = form
    context['product_name'] = product_name
 
    return render(request, "update_product.html", context)

def add_product(request, product_id): 
    try:
        if request.method == 'POST':
            form = Update_Product(request.POST)
            if form.is_valid():
                product_name = form.cleaned_data["product_name"]
                category_name = form.cleaned_data['category_name']
                description = form.cleaned_data['description']
                django_admin_side = form.cleaned_data['django_admin_side']

            products_update = products.objects.filter(product_name=product_id).update(product_name=product_name, category_name=category_name, description=description, django_admin_side=django_admin_side)
            products_list = products.objects.all()
            return render(request, 'dashboard.html', {'products': products_list})
    
    except:
        return False



@csrf_exempt
def create_products(request): 
    holder = []
    if request.method == 'POST':
        
        my_json = request.body.decode('utf8').replace("'", '"')
        print(my_json)
        print('- ' * 20)

        # Load the JSON to a Python list & dump it back out as formatted JSON
        data = json.loads(my_json)
        s = json.dumps(data, indent=4, sort_keys=True)
        print(s)
        holder.append(s)
        print(type(s))    
        return HttpResponse(status=200)
    

@csrf_exempt
def create_order(request): 
    holder = []
    if request.method == 'POST':
        
        my_json = request.body.decode('utf8').replace("'", '"')
        print(my_json)
        print('- ' * 20)

        # Load the JSON to a Python list & dump it back out as formatted JSON
        data = json.loads(my_json)
        s = json.dumps(data, indent=4, sort_keys=True)
        print(s)
        holder.append(s)
        print(type(s))
        return HttpResponse(status=200)

@csrf_exempt
def create_stores(request): 
    holder = []
    if request.method == 'POST':
        
        my_json = request.body.decode('utf8').replace("'", '"')
        # print(my_json)
        header = request.header
        print(header)
        # print('- ' * 20)

        # Load the JSON to a Python list & dump it back out as formatted JSON
        data = json.loads(my_json)
        s = json.dumps(data, indent=4, sort_keys=True)
        # print(s)
        # holder.append(s)
        print(type(s))
        return HttpResponse(status=200)