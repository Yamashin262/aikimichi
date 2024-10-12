from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView
from .models import Event
from .models import Event_list
from .models import Event_detail

# Create your views here.
class TopView(TemplateView):
    template_name = "top.html"

class EvetCreateView(CreateView):
    model = Event

class EvetListView(ListView):
    model = Event
    
class EvetDetailView(DetailView):
    model = Event