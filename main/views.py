from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView
from .models import Event

# Create your views here.
class TopView(TemplateView):
    template_name = "top.html"

class EventCreateView(CreateView):
    model = Event

class EventListView(ListView):
    model = Event
    
class EventDetailView(DetailView):
    model = Event