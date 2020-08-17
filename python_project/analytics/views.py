from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse

import pandas as pd

def index(request):
    return render(request, 'analytics/index.html', {})

def upload(request):
    data = pd.read_csv(request.FILES['csv'].file, encoding="SHIFT-JIS")
    return render(request, 'analytics/index.html', {'data': data})
