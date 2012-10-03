#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Utilities functions for the application.
"""

from django.contrib.gis.utils import LayerMapping
from evaluations.models import Country, Evaluation
from random import randint
import random
from datetime import date

def import_country(shp='evaluations/data/countries.shp'):
    """
    Import the countries from a shapefile.
    """
    # first delete all features (if any)
    Country.objects.all().delete()
    # mapping model-shp
    country_mapping = {
        'name' : 'NAME',
        'geometry' : 'MULTIPOLYGON',
    }
    # import features from shapefile to model
    countries = LayerMapping(Country, shp, country_mapping, transform=False, 
        encoding='iso-8859-1')
    countries.save(verbose=True, progress=True)
    print 'Import completed.'

def generate_random_test_data():
    """
    Generate some random test data.
    """
    # create the evaluations
    i = 0
    Evaluation.objects.all().delete()
    for country in Country.objects.all():
        # generate 0 to 5 evals
        for eva in range(0, randint(0,5)):
            i = i + 1
            print 'Generating eva %s for %s' % (i, country.name)
            e = Evaluation()
            e.title = 'Eval %s' % i
            e.country = country
            start_date = date.today().replace(day=1, month=1).toordinal()
            end_date = date.today().toordinal()
            random_date = date.fromordinal(random.randint(start_date, end_date))
            print random_date
            e.date = random_date
            e.link = 'http://example.com/%s/%s' % (country.name, i)
            e.evaluation_type = random.choice(Evaluation.EVALUTATION_TYPE_CHOICES)[0]
            e.save()
            # update country with random
            country.desk_study = random.choice([True, False])
            country.save()



