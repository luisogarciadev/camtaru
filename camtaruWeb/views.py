# Create your views here.
from django.shortcuts import render_to_response
from django.utils import timezone
from camtaruWeb.models import Route


def colors(request):
    route_colors = Route.objects.all().order_by('id')
    return render_to_response('colors.html', {'route_colors', route_colors})

# def add(request):
