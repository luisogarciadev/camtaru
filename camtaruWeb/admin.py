from django.contrib import admin
from camtaruWeb.models import Route, Vehicle


class RouteInline(admin.StackedInline):
    model = Route


class TaxiAdmin(admin.ModelAdmin):
    inlines = [RouteInline]

admin.site.register(Vehicle, TaxiAdmin)
