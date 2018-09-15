from django.shortcuts import render
from .models import Question


# Create your views here.
def index_view(request):
    qs = Question.objects.all()
    return render(request, 'encyclopedia/index.html', {'qs': qs})