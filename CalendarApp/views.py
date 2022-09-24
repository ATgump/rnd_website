from django.shortcuts import render, get_object_or_404
from .models import CalendarEvent
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
# Create your views here.


def single_event_view(request,somestringnamehere):
    event_obj = get_object_or_404(CalendarEvent,event_name=somestringnamehere)
    context = {
        "event_name":event_obj.event_name,
        "event_creator":event_obj.event_creator,
        "date":event_obj.date
    }
    return render(request,"CalendarApp/event_view.html",context)


class ClassBasedSingleEventView(DetailView):
    template_name: str = "CalendarApp/event_view.html"
    queryset = CalendarEvent.objects.all()

class ClassBasedListEventView(ListView):
    template_name: str = "CalendarApp/event_list_view.html"
    queryset = CalendarEvent.objects.all()
    # def get_queryset(self):
    #     return super().get_queryset().filter(hos)





def list_event_view(request):
    queryset = CalendarEvent.objects.all()
    context = {
        "queryset":queryset
    }
    return render(request,"CalendarApp/event_list_view.html",context)