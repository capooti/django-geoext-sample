#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Classes for Django admin.
"""

from django.contrib import admin
from models import Country, Evaluation
from django.contrib.gis.admin import OSMGeoAdmin

class CountryAdmin(OSMGeoAdmin):
    """
    Admin model for Country.
    """
    model = Country
    list_per_page = 20
    list_display = ['name', 'regional_bureaux', 'desk_study', 'country_visit', 'planned', 'planning_date',]
    search_fields = ['name', 'regional_bureaux', 'desk_study', 'country_visit', 'planned']
    list_filter = ['regional_bureaux', 'desk_study', 'country_visit', 'planned', ]
    date_hierarchy = 'planning_date'
    # Openlayers settings
    map_width = 500
    map_height = 500
    #openlayers_url = '/static/openlayers/lib/OpenLayers.js'
    default_zoom = 18

class EvaluationAdmin(admin.ModelAdmin):
    """
    Admin model for Evaluation.
    """
    model = Evaluation
    list_per_page = 20
    list_display = ['title', 'evaluation_type', 'date', 'link', 'country',]
    search_fields = ['title', 'country']
    list_filter = ['evaluation_type', 'country', ]
    date_hierarchy = 'date'
    
admin.site.register(Country, CountryAdmin)
admin.site.register(Evaluation, EvaluationAdmin)

