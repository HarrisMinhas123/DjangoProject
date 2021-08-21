from adoptions.models import Projects
from django.shortcuts import render

# Create your views here.
def geeks_view(request):
    # create a dictionary to pass
    # data to the template
    context ={
        "data":"Gfg is the best",
        "count" :Projects.objects.count(),
        "projects" :Projects.objects.all()

    }
    
    # return response with template and context
    return render(request, "geeks.html", context)
