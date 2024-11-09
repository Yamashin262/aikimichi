from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView
from .models import Event
from .models import EventJoin
from django.urls import reverse_lazy

# Create your views here.
class TopView(TemplateView):
    template_name = "top.html"
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        events = Event.objects.all()
        context["events"] = events
        
        return context

class EventCreateView(CreateView):
    model = Event
    fields = "__all__"

class EventListView(ListView):
    model = Event
    paginate_by = 10
    
class EventDetailView(DetailView):
    model = Event

class EventUpdateView(UpdateView):
    model = Event
    fields = '__all__'
    template_name_suffix = '_edit'

class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy('list')

class EventJoinCreateView(CreateView):
    model = EventJoin
    fields = "__all__"

class EventJoinListView(ListView):
    model = EventJoin
    paginate_by = 10
    
class EventJoinDetailView(DetailView):
    model = EventJoin

class EventJoinUpdateView(UpdateView):
    model = EventJoin
    fields = '__all__'
    template_name_suffix = '_edit'

class EventJoinDeleteView(DeleteView):
    model = EventJoin
    success_url = reverse_lazy('list')