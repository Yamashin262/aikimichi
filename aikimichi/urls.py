"""
URL configuration for aikimichi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TopView.as_view(), name="top"),
    path('main/', views.EventListView.as_view(), name="list"),
    path('main/new', views.EventCreateView.as_view(), name="new"),
    path('main/detail/<int:pk>', views.EventDetailView.as_view(), name="detail"),
    path('main/edit/<int:pk>', views.EventUpdateView.as_view(), name="edit"),
    path('main/delete/<int:pk>', views.EventDeleteView.as_view(), name="delete"),
    
    path('eventjoin/', views.EventListView.as_view(), name="joinlist"),
    path('eventjoin/new', views.EventCreateView.as_view(), name="joinnew"),
    path('eventjoin/detail/<int:pk>', views.EventDetailView.as_view(), name="joindetail"),
    path('eventjoin/edit/<int:pk>', views.EventUpdateView.as_view(), name="joinedit"),
    path('eventjoin/delete/<int:pk>', views.EventDeleteView.as_view(), name="joindelete"),
]
