#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Views for the application.
"""
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.gis.shortcuts import render_to_kml
from models import Country, Evaluation
from django.utils import simplejson
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
import json

def map_view(request):
    """
    Map view for evaluations.
    """
    return render_to_response('evaluations/map.html', 
        {
        },
        context_instance=RequestContext(request))
        
def get_kml_countries(request):
    """
    View for generating kml for countries.
    """
    countries = Country.objects.kml()
    return render_to_kml("gis/kml/countries.kml", {'countries' : countries})

def get_evaluations_json(request, country_id):
    """
    View for generating json for evaluation for a given country.
    """
    eva_list = []
    try:
        country = Country.objects.get(pk=country_id)
        rs = country.evaluation_set.all()
        for eva in rs:
            eva_dict = {
                'id': eva.id,
                'title': eva.title,
                'date': eva.date.isoformat(),
                'country': eva.country.name,
                'evaluation_type': eva.evaluation_type,
                'link': eva.link,
            }
            eva_list.append(eva_dict)
    except ObjectDoesNotExist:
        print 'There is not such a country'
    eva_json = json.dumps(eva_list)
    print eva_json
    return HttpResponse(eva_json, mimetype='application/json')

