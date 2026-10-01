from django import forms

from .models import ReportCard


class ReportCardForm(forms.ModelForm):
    # template_name = "trainee_scoring/form_rows.html"
    model = ReportCard
    exclude = ("day_one", "day_two")
    widgets = {
        "trainee": forms.HiddenInput(),
    }


class FilteredReportCardFormSet(forms.BaseModelFormSet):
    """Custom formset that filters queryset based on trainees with training today"""
    def __init__(self, *args, trainees=None, **kwargs):
        super().__init__(*args, **kwargs)
        if trainees:
            self.queryset = ReportCard.objects.filter(trainee__in=trainees)
