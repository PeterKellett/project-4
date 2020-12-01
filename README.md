<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

# PeterKellett - Milestone Project 4

## User stories

### As a User

1. As a user I would like to view a nicely designed site with logical navigation applied.
2. As a user I would like to view sample designs done by the company previously.
3. As a user I would like to be able to see any testimonials left by previous users.
4. As a user I would like to be able to contact the company in a simple straightforward way.
5. As a user I would like to be able to order a particular graphic and spcify it's size.
6. As a user I would like to be assured that any contact information provided is dealt in a secure manner.

### As an Owner

1. As an owner I would like to be able to showcase a sample of my previous work.
2. As an owner I would like to be notified of any orders submitted and be able view them as a superuser and that they are not accessible to anybody else.
3. As an owner I would like to be able to contact the person who submitted the order.
4. As an owner I would like top be able to keep the final product secure until a verified payment is made whereby the final product is immediately released to the client.
5. As an owner I would like to be able to gather a testimonial from each client.
6. As an owner I would like the finished products and the client testimonial to be automatically added to the site showcase area.

## Project initial set up

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
   Ref: https://django-allauth.readthedocs.io/en/latest/faq.html?highlight=EMAIL_BACKEND#when-i-sign-up-i-run-into-connectivity-errors-connection-refused-et-al  
   Ref: https://docs.djangoproject.com/en/dev/ref/settings/#email-host - EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
2. Set up AUTHENTICATION methods  
   Ref: https://django-allauth.readthedocs.io/en/latest/configuration.html?highlight=ACCOUNT_AUTHENTICATION_METHOD#configuration - ACCOUNT_AUTHENTICATION_METHOD = 'username_email' - ACCOUNT_EMAIL_REQUIRED = True - ACCOUNT_EMAIL_VERIFICATION = 'mandatory' - ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True - ACCOUNT_USERNAME_MIN_LENGTH = 4 - LOGIN_URL = '/accounts/login/' - LOGIN_REDIRECT_URL = '/'
3. Manually set superuser email to both verified and primary via django site admim
4. Freeze all pip3 installs to requirements.txt
   - pip3 freeze > requirements.txt

## Templates

### Allauth templates

1. mkdir templates
2. mkdir templates/allauth
3. Copy over all allauth built in templates from root folder
   - CLI: cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/\* ./templates/allauth
4. Remove openid and tests folders as they are not required.

### Site base.html template

This holds the code for:

- {% load static %}
- The head tags
  - The meta tags
  - Links to 3rd party source libraries
  - The title tags
- The body tags
  - The header container
  - The messages container
    Content is divided into blocks so sections can be extended by other pages if required.

Block sections added are:

- block meta
- block extra_meta
- block corecss
- block extra_css
- block corejs
- block extra_js
- block extra_title
- block page_header
- block content
- block postloadjs

#### Source libraries

1. Bootstrap4 starter template with css and js option 2 chosen.

# Apps

## Home App
1. Create app
   - python3 manage.py startapp home
2. Add a templates/home folder inside this app folder
   - mkdir -p home/templates/home
3. Add an index.html file to this directory.
   - This is for all the home page content.
4. Add a view for this page in views.py
   - def index view and return the index.html page
5. In the home app create a new file urls.py and set the imports and url pattern to the home page
6. Return to root level urls.py file to include the home urls
7. Add the home app to our INSTALLED_APPS list in settings.py
8. Add the templates for the root level templates directory and the allauth directory to TEMPLATES DIRS settings
   - 'DIRS': [
      os.path.join(BASE_DIR, 'templates'),
      os.path.join(BASE_DIR, 'templates', 'allauth'),
      ],

### Home views  
- index  


## CSS stylesheet

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

## Crispy forms

1. pip3 install django-crispy-forms
2. Add this install to settings.py INSTALLED_APPS
3. CRISPY_TEMPLATE_PACK = 'bootstrap4'
4. Add to templates-builtins in settings.py

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

## Shopping Bag App  
- New file for context processor: shopping_bag/contexts.py  
- Add this to the list of context processors in settings.py TEMPLATES section

### Shopping Bag context processor  
- shopping_bag_contents  

### Shopping Bag views  
- view_shopping_bag  
- add_to_shopping_bag  
- 

### shopping bag urls  
- path('', views.view_shopping_bag, name='view_shopping_bag'),
- path('add/<item_id>/', views.add_to_shopping_bag, name='add_to_shopping_bag'),  



## Models  
![home page wireframe](https://res.cloudinary.com/dfboxofas/image/upload/v1606741313/project-4/readme/project-4_models-v2_xqh5jg.png)  

### Products model   
Fields | Type | Max Length | Null | Blank |  
-------|------|------|----------|------|  
Primary_key | Int | Auto increment | False | False 
Category | Foreign_key Category |  | True | True 
name | Char| 254 | False | False |
description | Text | 254 | True | True  
price | Decimal | 6 (2 decimal places) | False | False | 
image_url | URL | 1024 | False | False 
image | Image |  | False | False  
sku | Char | 254 | False | False 
rating | Int | 2 | True | True  
size_s | Boolean | | True | True  
size_m | Boolean | | True | True  
size_lg | Boolean | | True | True  
size_xl | Boolean | | True | True  


### Category model
Fields | Type | Max Length | Null | Blank |  
-------|------|------|----------|------|  
Primary_key | Int | Auto increment | False | False
name | CharField | 254 | False | False
friendly_name | CharField | 254 | True | True


### OrderLineItem  
Fields | Type | Max Length | Null | Blank | Other
-------|------|------|----------|------|------
Primary_key | Int | Auto increment | False | False
order | ForeignKey(Order) |  | False | False | related_name='lineitems' ??  
product | ForeignKey(Product) | | False | False | related_name='lineitems' ??  
product_size | Char | 2 | True | True  
quantity | Int | | False | False | default=0 ??  
lineitem_total | Decimal | 6 | False | False | decimal_places=2  


### Order model  
Fields | Type | Max Length | Null | Blank | Other
-------|------|------|----------|------|------
Primary_key | Int | Auto increment | False | False
order_number | uuid | 32 | False | False 
user_profile | ForeignKey(UserProfile) | | True | True | related_name='order' ??  
full_name | Char | 50 | False | False
email | Email | 254 | False | False  
phone_number | Char | 30 | False | False
country | Country |  | False | False | blank_label='Country *'
postcode | Char | 20 | True | True 
town_or_city | Char | 40 | False | False 
street_address1 | Char | 80 | False | False 
street_address2 | Char | 80 | True | True 
county | Char | 80 | True | True 
date | DateTime |  | False | False | auto_now_add=True
delivery_cost | Decimal | 6 | False | False | decimal_places=2
order_total | Decimal | 10 | False | False | decimal_places=2
grand_total | Decimal | 10 | False | False | decimal_places=2
original_bag | Text | | False | False | default=''
stripe_pid | Char | 254 | False | False | default=''  


### UserProfile  
Fields | Type | Max Length | Null | Blank | Other
-------|------|------|----------|------|------
Primary_key | Int | Auto increment | False | False
user | OneToOne | | False | False
default_phone_number | Char | 30 | True | True 
default_street_address1 | Char | 80 | True | True 
default_street_address2 | Char | 80 | True | True 
default_town_or_city | Char | 40 | True | True 
default_county | Char | 80 | True | True 
default_postcode | Char | 20 | True | True 
default_country | Char | 30 | True | True  

### Subscription model  
Fields | Type | max Length | Null | Blank |  
-------|------|------|----------|------| 
Primary_key | Int | Auto increment | False | False  
name | Char | 254 | False | False 

### EmailSubscriptions model  
Fields | Type | Max Length | Null | Blank | Other
-------|------|------|----------|------|------
Primary_key | Int | Auto increment | False | False  
user_id | ForeignKey(UserProfile) |  | False | False 

### ProductComment model  
Fields | Type | Max Length | Null | Blank | Other
-------|------|------|----------|------|------
Primary_key | Int | Auto increment | False | False  
user_id | ForeignKey(UserProfile) |  | False | False  
product_id | ForeignKey(Products) | | False | False 
comment | Text | 254 | False | False  




## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

---

Happy coding!
