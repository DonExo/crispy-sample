# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .forms import MessageForm

# Create your views here.

def index(request):
    form = MessageForm()
    print(form)

    return render(request, 'app/template.html', {
        'form': form,
    })
    # return HttpResponse("Hello world")