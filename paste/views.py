from django.shortcuts import render
from .models import textpaste
from .forms import data
from django.http import HttpResponse
# Create your views here.
def intro(request):
    dict = {"input":textpaste.objects.order_by('-id')}
    return render(request, "paste/intro.html", context = dict)

def Complete(request):
    return render(request, "paste/complete.html")

def Data(request):
    form = data()
    if (request.method == 'POST'):
        form = data(request.POST)
        if form.is_valid():
            form.save(commit= True)
            return Complete(request)
        else:
            return HttpResponse("<h1> Invalid Data <h1>")
    return render(request, "paste/forms.html",{'form':form})

def detailed(request, str):
    obj = textpaste.objects.get(Username=str)
    return render(request,"paste/detailed.html",{'paste':obj})