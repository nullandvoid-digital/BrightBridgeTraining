import datetime

from django.shortcuts import render, redirect
from django.template.defaultfilters import date
from django.views.generic import ListView
from django.forms import modelformset_factory
from django.db.models import Q

from .models import ReportCard, Trainee
from .forms import ReportCardForm, FilteredReportCardFormSet


# Create your views here.
def scoring_home(request):
    return render(request, "trainee_scoring/scoring-home.html")


def grading_sheet(request):
    trainees = Trainee.objects.filter(
        Q(day_one=datetime.date.today()) | Q(day_two=datetime.date.today())
    )
    reportcardformset = modelformset_factory(
        ReportCard,
        form=ReportCardForm,
        formset=FilteredReportCardFormSet,
        extra=len(trainees),
        exclude=("day",),
    )
    formset = reportcardformset(
        request.POST,
        trainees=trainees,
        queryset=ReportCard.objects.filter(trainee__in=trainees),
    )
    if request.method == "POST":
        day = request.POST.get("training_day")
        formset = reportcardformset(request.POST, queryset=ReportCard.objects.none())
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data.get("trainee"):
                    form.instance.day = datetime.date.today()
            formset.save()
        return redirect("scoring")
    else:
        formset = reportcardformset(
            queryset=ReportCard.objects.none(),
            initial=[{"trainee": trainee} for trainee in trainees],
        )
    return render(request, "trainee_scoring/grading-sheet.html", {"formset": formset})


class Trainees(ListView):
    model = Trainee


def report_card(request, trainee_id):
    pass
