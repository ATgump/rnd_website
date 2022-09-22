from django.shortcuts import render,get_object_or_404
from .models import Presentation
# Create your views here.

def presentations_home_view(request):
    return render(request,"Presentations/home_view.html",{})

def individual_presentation_view(request,user):
    obj = get_object_or_404(Presentation,username=user)
    context = {
        "obj":obj
    }
    return render(request, "Profiles/UserProfile.html", context) ### directory in templates/htmldoc (or more directories presumably)


def make_presentation_view(request):
    return render(request,"Presentations/make_presentation_view.html",{})
