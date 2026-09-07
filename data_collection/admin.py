from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Behavior)
class BehaviorAdmin(admin.ModelAdmin):
    list_display = ("name", "opdef")
    list_select_related = ["examples"]
    search_fields = ("slug", "name")
    prepopulated_fields = {"slug": ["name"]}


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "behavior",
        "event",
        "explanation",
        "meetsdef",
        "example",
    )
    list_filter = ("behavior", "meetsdef", "example")


@admin.register(EventSet)
class EventSetAdmin(admin.ModelAdmin):
    list_display = ("id", "set_id", "events", "ordered", "index")
    list_filter = ("events", "ordered")


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("id", "behavior", "type", "events")
    list_filter = ("behavior", "events")


@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "timestamp", "program", "results")
    list_filter = ("user", "timestamp", "program")
