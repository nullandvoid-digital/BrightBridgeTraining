from django.urls import path, register_converter
from . import views

urlpatterns = [
    path("", views.scoring_home, name="scoring"),
    path("grading/", views.grading_sheet, name="grading_sheet"),
    path("reportcards/", views.Trainees.as_view(), name="report_cards"),
    path(
        "reportcards/<int:pk>",
        views.TraineeReportCard.as_view(),
        name="report_card",
    ),
]
