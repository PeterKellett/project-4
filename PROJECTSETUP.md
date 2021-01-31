# Project set up  
This document outlines the various steps taken during the development of this project.  

### Pypi installs required  
The following pip3 installs are required:  
- django  
- django-allauth  
- django-crispy-forms  
- dj-database-url
- django-countries
- django-crispy-forms
- django-jsonify
- django-storages
- gunicorn
- Pillow
- psycopg2-binary
- boto3
- stripe==2.55.1

## Initial set up 
1. Install Django
   - pip3 install django (v20.2.4 installed)
2. Create the project root files
   - django-admin startproject project_4 .
3. Create a .gitignore file
   - touch .gitignore
   - Add _.sqlite, _.pyc, **pycache** to .gitignore file
4. Run migrations
   - python3 manage.py migrate
5. Create superuser
   - python3 manage.py createsuperuser
   - Provide username
   - Provide an email address
   - Provide a password

## Allauth
### Allauth set up 1
1. Install django-allauth
   - pip3 install django-allauth
2. Set up reference guide https://django-allauth.readthedocs.io/en/latest/installation.html
3. Add the AUTHENTICATION_BACKENDS from reference guide
4. Add in the following INSTALLED_APPS from reference guide
   - 'django.contrib.sites',
   - 'allauth',
   - 'allauth.account',
   - 'allauth.socialaccount',
5. Add SITE_ID = 1 to settings.py file
6. Add a path to allauth accounts in urls.py file
   - path('accounts', include('allauth.urls')),
7. Run new migrations
   python3 manage.py migrate
8. Open the site and log in to django admin and go to 'sites'
9. Update the domain of the default site to blackhills.graphics.example.com
10. Update the display name to Blackhills graphics

### Allauth set up 2
1. To enable emails be printed to the console without an smtp server for emails add following code to settings.py:  
   Ref: https://docs.djangoproject.com/en/dev/ref/settings/#email-host  
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
2. Set up AUTHENTICATION methods  
   Ref: https://django-allauth.readthedocs.io/en/latest/configuration.html?highlight=ACCOUNT_AUTHENTICATION_METHOD#configuration ACCOUNT_AUTHENTICATION_METHOD = 'username_email' - ACCOUNT_EMAIL_REQUIRED = True - ACCOUNT_EMAIL_VERIFICATION = 'mandatory' - ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True - ACCOUNT_USERNAME_MIN_LENGTH = 4 - LOGIN_URL = '/accounts/login/' - LOGIN_REDIRECT_URL = '/'
3. Manually set superuser email to both verified and primary via django site admim
4. Freeze all pip3 installs to requirements.txt
   - pip3 freeze > requirements.txt  

### Allauth templates
1. mkdir templates
2. mkdir templates/allauth
3. Copy over all allauth built in templates from root folder
   - CLI: cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/\* ./templates/allauth
4. Remove openid and tests folders as they are not required.

## Django email  
### Set up  
1. Create new text files for the email subject and body content in the apps static folder  
2. In the Stripe webhook handler define a new class _send_confirmation_email  
3. Imports  
    - from django.core.mail import send_mail  
    - from django.core.mail import send_mail
    - from django.template.loader import render_to_string  
 
## Creating Apps
1. Initiate the app
   - python3 manage.py startapp appname
2. Add a templates/appname folder inside this app folder
   - mkdir -p appname/templates/appname
3. Add html files related to this app in this directory.
4. Add a view for these pages in views.py
5. Write the controller logic for each of these views in views.py file. 
6. In the app create a new file urls.py and set the imports and url pattern for each file path required
7. Return to root level urls.py file to include the root path to the app urls
7. Add the appname to the list INSTALLED_APPS in settings.py

## Adding Categories
1. Create a new app Products
2. Add a new folder fixtures
3. Add a json file to fixtures file
4. Add a model for the categories database table
5. Make migrations
   - python3 manage.py makemigrations --dry-run
   - python3 manage.py makemigrations
   - python3 manage.py migrate --plan
   - python3 manage.py migrate
6. Register this model in products/admin.py
7. Load the data
   - python3 manage.py loaddata categories
8. Customise the admin of the categories model in products/admin.py  

## Adding Products  
1. Create a new app Products
2. Add a new folder fixtures
3. Add a json file to fixtures file 
4. Add a model for the products database table
5. Make migrations
   - python3 manage.py makemigrations --dry-run
   - python3 manage.py makemigrations
   - python3 manage.py migrate --plan
   - python3 manage.py migrate
6. Register this model in products/admin.py
7. Load the data
   - python3 manage.py loaddata products
8. Customise the admin of the categories model in products/admin.py  

## CSS stylesheets
1. mkdir static
2. mkdir static/css
3. Connect these new folders in settings.py
   - STATIC_URL = '/static/'
   - STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)  

## Media files
1. mkdir media
2. Connect the media folder in settings.py
   - MEDIA_URL = '/media/'
   - MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
3. Add the following to the root urls.py file
   - from django.conf import settings
   - from django.conf.urls.static import static
   - '+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'

## Crispy form  
1. pip3 install django-crispy-forms
2. Add this install to settings.py INSTALLED_APPS
3. CRISPY_TEMPLATE_PACK = 'bootstrap4'
4. Add to templates-builtins in settings.py  
