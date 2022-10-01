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

from .views import (
    presentations_home_view,
    individual_presentation_view,
    make_presentation_view,
)

app_name = "Presentations"
urlpatterns = [
    #    path("css/",cssUploadView,name="css-upload"),
    #    path("uploadsuccess/",uploadSuccessView,name="success")
    path("", presentations_home_view, name="presentations-home"),
    path("create/", make_presentation_view, name="make-presentation"),
    path(
        "<presentation_name>/", individual_presentation_view, name="presentation-single"
    ),
]
