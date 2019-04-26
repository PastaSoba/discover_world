from django.urls import path
from . import views

app_name = 'mainapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('exploreplan', views.exploreplan, name='exploreplan'),
    path('aboutus', views.aboutus, name='aboutus'),
]