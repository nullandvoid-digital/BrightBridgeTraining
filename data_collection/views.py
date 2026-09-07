from django.shortcuts import render
from django.template.response import TemplateResponse

from .models import Program


# Create your views here.
def display_program(request, pk):
    prog = Program.objects.select_related().get(pk=pk)

    response = TemplateResponse(
        request,
        "program_display.html",
        {
            "program": prog,
        },
    )
    return response
