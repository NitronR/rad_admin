from django.shortcuts import render


# Create your views here.
def home(req):
    return render(req, 'mainapp/index.html')


def submit_ra(req):
    pass


def get_ra(req):
    pass