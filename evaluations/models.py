#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Models for the application.
"""

from django.db import models
from django.contrib.gis.db import models as gismodels

class Country(gismodels.Model):
    """
    Spatial model for Country.
    """
    REGIONAL_BUREAU_CHOICES = (
        ('ODB', 'ODB'),
        ('ODC', 'ODC'),
        ('ODD', 'ODD'),
        ('ODJ', 'ODJ'),
        ('ODN', 'ODN'),
        ('ODP', 'ODP'),
        ('ODS', 'ODS'),
    )
    # attributes
    name = gismodels.CharField(max_length=255)
    regional_bureaux = gismodels.CharField(null=True, blank=True, max_length=3, choices=REGIONAL_BUREAU_CHOICES)
    desk_study = gismodels.NullBooleanField()
    country_visit = gismodels.NullBooleanField()
    planned = gismodels.NullBooleanField()
    planning_date = gismodels.DateField(null=True, blank=True)
    geometry = gismodels.MultiPolygonField(srid=4326)
    objects = gismodels.GeoManager()

    def __unicode__(self):
        return '%s' % (self.name)
        
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Countries"

class Evaluation(gismodels.Model):
    """
    Model for Evaluation.
    """
    EVALUTATION_TYPE_CHOICES = (
        ('EV1', 'Evaluation type 1'),
        ('EV2', 'Evaluation type 2'),
        ('OTH', 'Other evaluation type'),
    )
    # attributes
    title = models.CharField(max_length=255)
    date = models.DateField()
    evaluation_type = models.CharField(max_length=3, choices=EVALUTATION_TYPE_CHOICES)
    link = models.URLField(max_length=255)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return '%s' % (self.title)
