from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume', views.resume, name='test'),
    path('code', views.code, name="code"),
]
