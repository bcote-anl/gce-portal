# gce-portal
An ACDC portal for the galactic chemical evolution (GCE) project. The search index points to datasets generated by the interactive astronomy data service prototype.

### Development

Clone repository

```
git clone https://github.com/bcote-anl/gce-portal.git
```

Create your environment and install packages:

```
cd gce-portal/
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Install ACDC tools to re-use existing javascript functions.

```
git clone https://github.com/globusonline/django-alcf-data-portal.git
cd django-alcf-data-portal/
python setup.py develop
```

Once you have the alcf-data-portal application installed, perform the Django migration.

```
cd ../
python manage.py migrate
```

Add your Globus client details in testing/settings.py.

```
SOCIAL_AUTH_GLOBUS_KEY = 'your_client_ID_here'
SOCIAL_AUTH_GLOBUS_SECRET = 'your_client_secret_here'
```

Run the portal with the following command. Make sure your localhost port matches the redirect URL of your Globus client (see instructions [here](https://django-globus-portal-framework.readthedocs.io/en/latest/tutorial/installation-and-setup.html#globus-auth)).



```
python manage.py runserver localhost:8000
```
