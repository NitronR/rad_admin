from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from mainapp.forms import AlertForm


# Create your views here.
def home(req):
    return render(req, 'mainapp/index.html')


@csrf_exempt
def submit_ra(req):
    form = AlertForm(req.POST, req.FILES)
    if(form.is_valid()):
        form.save()
    return HttpResponse("Hello")


def get_ra(req):
    pass