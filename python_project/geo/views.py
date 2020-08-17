from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
import requests
import io
import pandas as pd
import geopandas as gpd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import urllib
import json
from . import forms

def index(request):
    form = forms.SampleForm(request.POST)
    context = {
        'form': form
    }
    return render(request, 'geo/index.html', context)

def prefecture(request, pid):
    context = {
        'pk': pid
    }
    return render(request, 'geo/prefecture.html', context)

def setPlt(pid):
    print(pid)
    file_path = f'./geo/geojson/prefectures/{pid}.json' if pid != '0' else './geo/assets/prefectures.geojson'
    df = gpd.read_file(file_path, encoding='SHIFT-JIS')
    df.plot(figsize=[10,10])


# svgへの変換
def pltToSvg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

def get_svg(request, pid):
    setPlt(pid)     # create the plot
    svg = pltToSvg() # convert plot to SVG
    plt.cla()        # clean up plt so it can be re-used
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response


def set_prefecture(request):
    pid = request.GET.get('prefectures')
    print(pid)
    context = {
        'pid': pid
    }
    return render(request, 'geo/prefecture.html', context)