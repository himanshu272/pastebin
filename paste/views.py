from django.shortcuts import render
from .models import textpaste
from .forms import data
from django.http import HttpResponse
# Create your views here.
def intro(request):
    return render(request, "paste/intro.html")

def public(request):
    dict = {"input":textpaste.objects.all()}
    return render(request, "paste/publicpaste.html", context = dict)

def Data(request):
    form = data()
    if (request.method == 'POST'):
        form = data(request.POST)
        if form.is_valid():
            form.save(commit= True)
            return intro(request)
        else:
            return HttpResponse("<h1> Invalid Data <h1>")

    return render(request, "paste/forms.html",{'form':form})