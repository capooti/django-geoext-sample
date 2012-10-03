How to setup the environment
============================

This code is intended to be an example prototype application using GeoDjango and GeoExt.

There are two entities:
    * Country 
    * Evaluation

One Country may have 0 to many evaluations. The application let the user to edit and query the entities using the Django admin interface, or to show the countries in a OpenLayers map, letting the user to display by selecting a country all of the related evaluations.

* Create a virtual environment and activate it::

    $ virtualenv prj-env --no-site-packages --python=python2.7
    $ . prj-env/bin/activate

* Install the needed python libraries::

    $ pip install -r requirements.txt
    
* Edit the settings.py file for using your database settings and syncronize the database::

    $ ./manage.py syncdb

* Import country data from shapefile and generate some random evaluations for testing::

    $ ./manage.py shell 
    >>> from evaluations.models import Country
    >>> from evaluations.utils import generate_data
    >>> generate_data.import_country()
    >>> generate_data.generate_random_test_data()
    
* for importing the shapefile you could use ogr2ogr as well::

    $ ogr2ogr -append -f PostgreSQL -sql "SELECT NAME AS name FROM 'countries'" -nlt MULTIPOLYGON PG:"dbname='evaluations' user='wfp' password='mypassword'" -nln evaluations_country evaluations/data/countries.sh

* Run the development server::

    $ ./manage runserver

* Add some evaluation entities via the admin interface: http://localhost:8000/admin/

* Now navigate to the front end and test the application: http://localhost:8000/evaluations/map
