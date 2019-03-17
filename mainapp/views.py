from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from mainapp.forms import AlertForm
from mainapp.models import AccidentAlert
from django_common.http import JsonResponse


# Create your views here.
def home(req):
    return render(req, 'mainapp/index.html')


@csrf_exempt
def submit_ra(req):
    form = AlertForm(req.POST, req.FILES)
    if(form.is_valid()):
        form.save()
    return HttpResponse("Hello")


@csrf_exempt
def get_ra(req):
    objs = list(AccidentAlert.objects.all().values())

    alerts = list(map(lambda x: {'cam': x['camera_num'], 'img': '/media/' + x['image']}, objs))

    return JsonResponse({'alerts': alerts})
