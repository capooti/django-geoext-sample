#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
URLs for the application.
"""
from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    url(r'^map$', views.map_view, name='evaluations-map-view'),
    url(r'^countries/kml$', views.get_kml_countries,
        name='evaluations-countries-kml'),
    url(r'^per-country/(?P<country_id>\d+)/json$', views.get_evaluations_json, 
        name='evaluations-per-country-json'),
)
