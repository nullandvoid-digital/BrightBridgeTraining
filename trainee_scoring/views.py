import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import date
from django.views.generic import ListView
from django.forms import modelformset_factory
from django.db.models import Q
from django.views.generic.detail import DetailView

from .models import ReportCard, Trainee
from .forms import ReportCardForm, FilteredReportCardFormSet
from .rubric import Rubric as r


# Create your views here.
def scoring_home(request):
    return render(request, "trainee_scoring/scoring_home.html")


def grading_sheet(request):
    trainees = Trainee.objects.filter(
        Q(day_one=datetime.date.today()) | Q(day_two=datetime.date.today())
    )
    reportcardformset = modelformset_factory(
        ReportCard,
        form=ReportCardForm,
        formset=FilteredReportCardFormSet,
        extra=len(trainees) if trainees else 5,
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
        )
    return render(request, "trainee_scoring/grading_sheet.html", {"formset": formset})


class Trainees(ListView):
    model = Trainee
    context_object_name = "trainees"


class TraineeReportCard(ListView):
    template_name = "trainee_scoring/report_card.html"
    context_object_name = "reportcards"

    def get_queryset(self):
        self.trainee = get_object_or_404(Trainee, pk=self.kwargs["pk"])
        return ReportCard.objects.filter(trainee=self.trainee)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trainee"] = self.trainee

        attrs = [attr for attr in dir(r) if not attr.startswith("__")]
        total = 0
        for attr in attrs:
            if attr.isupper() and attr != "DAYS":
                attr_value = getattr(r, attr)
                if isinstance(attr_value, dict) and attr_value:
                    total += r.max_value(attr)
        total = (total * 2) - 2
        context["total"] = total

        reportcards = ReportCard.objects.filter(trainee=self.trainee)
        actual = 0
        for card in reportcards:
            actual += card.on_time
            actual += card.answers
            actual += card.focus
            actual += card.dress
            actual += card.duration
        context["actual"] = actual

        context["percent"] = round((actual / total) * 100, 2)
        return context
