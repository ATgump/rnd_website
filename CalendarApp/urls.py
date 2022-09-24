"""rnd_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path



### will import views later 
from .views import single_event_view,list_event_view,ClassBasedListEventView,ClassBasedSingleEventView,event_creation_view,event_home_view



app_name = 'CalendarApp'
urlpatterns = [
#path("event/<slug:somestringnamehere>/",ClassBasedSingleEventView.as_view(),name='single-event-view'),
path("",event_home_view,name="home-view"),
path("event-list/",ClassBasedListEventView.as_view(),name="list-event-view"),
path("event/<str:somestringnamehere>/",single_event_view,name='single-event-view'),
path("eventcreate/",event_creation_view,name="create-event-view"),
# path("event-list/",list_event_view,name="list-event-view"),
]
