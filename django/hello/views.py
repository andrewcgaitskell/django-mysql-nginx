from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
