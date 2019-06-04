from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('count/', views.count, name='count'),
    path('count/home/', views.home)
]
