# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Wrestler

# Create your views here.
def index(req):
    context = {
        "wrestlers": 
    }
    return render(req, 'wrestlers/index.html', context)

def create(req):
    name = req.POST['name']
    weight = req.POST['weight']
    nick_name = req.POST['nick_name']
    
    return redirect('/wrestlers')

def edit(req, wrestler_id):
    context = {
        "wrestler": 
    }
    return render(req, "wrestlers/edit.html", context)
def show(req, wrestler_id):
    context = {
        "wrestler": 
    }
    return render(req, "wrestlers/show.html", context)

def update(req, wrestler_id):
    wrestler = 
    wrestler.name =  req.POST['name']
    wrestler.weight = req.POST['weight']
    wrestler.nick_name = req.POST['nick_name']
    wrestler.save()
    return redirect('/wrestlers')
def new(req):
    return render(req, "wrestlers/new.html")
def destroy(req, wrestler_id):
    
    return redirect('/wrestlers')
