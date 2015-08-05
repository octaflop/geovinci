# geovinci
Demo app for Python, GeoDjango, and Elastic Search GIS

## [Presentation Slides](https://docs.google.com/presentation/d/1bRubWmkoJHbhcB5EI_wvSWjGWXKZq1MD6zhnZmBLeO4/edit?usp=sharing)

## Repo setup

1. Prereqs: Virtualenv, Python3.4, pip, git, postgresql-9.3, postgresql-server-dev-9.3

2. git clone

3. `mkvirtualenv --python=/usr/bin/python3.4 geovinci`

4. `pip install -r requirements`

5. Add the apps folder to the virtualenv:
  ```bash
  add2virtualenv `pwd`/apps
  ```

## Postgres

1. `sudo su postgres`

2. `createuser geovinci_user -P  # Enter a password when prompted`

3. Copy `local_settings.example.py` to `local_settings.py` and update the `DATABASES['default']['PASSWORD']` field to your new password.

4. `createdb geovinci -O "geovinci_user"`


## Other installation notes

1. [GeoDjango Installation Notes](https://docs.djangoproject.com/en/1.8/ref/contrib/gis/install/)

2. Install os modules (Ubuntu): `apt-get install postgresql-server-dev-9.3 postgresql-9.3 postgresql-9.3-postgis-2.1`

3. Install more os modules: `sudo apt-get install binutils libproj-dev gdal-bin libgeos-dev`


5. `world` is just the [geodjango tutorial](https://docs.djangoproject.com/en/1.8/ref/contrib/gis/tutorial/#introduction)


# External resources

* Django Leaflet

* https://www.mapbox.com/mapbox-studio/#linux

