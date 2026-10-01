from django.contrib import admin

from .models import Trainee, ReportCard


@admin.register(Trainee)
class TraineeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "day_one", "day_two")
    list_filter = ("day_one",)
    search_fields = ("name",)


@admin.register(ReportCard)
class ReportCardAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "trainee",
        "on_time",
        "dress",
        "duration",
        "answers",
        "focus",
        "roleplay",
        "accepts",
        "implements",
    )
    list_filter = ("trainee",)
