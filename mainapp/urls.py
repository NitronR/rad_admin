from django.urls.conf import path
from mainapp import views

urlpatterns = [
    path('', views.home),
    path('submit_ra', views.submit_ra),
    path('get_ra', views.get_ra)
]