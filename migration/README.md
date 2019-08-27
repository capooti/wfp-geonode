# WFP GeoNode 2.4 -> 2.10 migration

## PostgreSQL

Create a role and a database for Django:

```
create role wfp with superuser login with password 'wfp';
create database wfp_24 with owner wfp;
\c wfp_24
create extension postgis;
```

Restore backup:

```
psql wfp_24 < sdi_django.sql
```

## Run GeoNode migrations

Activate virtualenv and set the env vars:

```
. env/bin/Activate
export vars_210
```

Downgrade psycopg2:

```
pip install psycopg2==2.7.7
```

Apply migrations:

```
cd wfp-geonode
./manage.py migrate --fake-initial
```

Upgrade psycopg2:

```
pip install -r requirements.txt
```

## Create superuser

To create a superuser I had to drop the following constraints (we can re-enable if needed):

```
alter table people_profile alter column last_login drop not null;
```

./manage createsuperuser
