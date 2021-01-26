<img src="https://res.cloudinary.com/dfboxofas/image/upload/v1611675581/project-4/blackhillls_logo_qgtqtm.png" style="height: 100px"><img src="https://res.cloudinary.com/dfboxofas/image/upload/v1611676527/project-4/jerseys-transparent-bg_2_yi6org.png" style="height: 100px">

# PeterKellett - Milestone Project 4
## Introduction
This project forms the 4th milestone project of the Code Institute Full Stack Developer module and is to demonstrate my ability and knowledge of the Django framework.  
To do this I have developed an e-commerce store for sports jerseys with a user registration and checkout facilities.  

## User stories

### As a User
1. As a user I would like to view a nicely designed site with logical navigation applied.
2. As a user I would like to view products in a nice concise manner.
3. As a user I would like to be able to see any testimonials left by previous users.
4. As a user I would like to be able to contact the company in a simple straightforward way.
5. As a user I would like to be able to order a particular jersey and spcify it's size.
6. As a user I would like to be assured that any contact information provided is dealt in a secure manner.

### As an Owner
1. As an owner I would like to be able to showcase our products.
2. As an owner I would like to be notified of any orders submitted and be able view them as a superuser and that they are not accessible to anybody else.
3. As an owner I would like to be able to contact the person who submitted the order.
4. As an owner I would like top be able to keep the final product secure until a verified payment is made whereby the final product is immediately released to the client.
5. As an owner I would like to be able to gather a testimonial from each client.
6. As an owner I would like the finished products and the client testimonial to be automatically added to the site showcase area.  

## Wireframes  
![home page large and up](https://res.cloudinary.com/dfboxofas/image/upload/v1611686272/project-4/readme/Home-large-and-up_hltnla.jpg)  
![Products page large and up](https://res.cloudinary.com/dfboxofas/image/upload/v1611686272/project-4/readme/Products-large-and-up_osxxsr.jpg)  
![Products card](https://res.cloudinary.com/dfboxofas/image/upload/v1611686272/project-4/readme/Products-card_vg18up.jpg)  
![Products details page](https://res.cloudinary.com/dfboxofas/image/upload/v1611686272/project-4/readme/product-detail-large-and-up_eblblf.jpg)  
![Shopping bag page large and up](https://res.cloudinary.com/dfboxofas/image/upload/v1611686272/project-4/readme/shopping-basket-large-and-up_vjbyhb.jpg)  

## Design
### Colour Scheme
The two main colours used on this site #d0b3b7 and #985d65.  

### Typography
The main fonts used are Bangers and Roboto from Google Fonts. Bangers is the style of the brand logo so it is continued in a descrete fashion throughout the site on the buttons which bring the user through the full visit and checkout experience. It was chosen as it reflects a casual yet sharp style. Roboto is used for all other text as it is a clean font well spaced font and easy on the eye.


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

## Crispy form  
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
- 
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

## Checkout  
1. Checkout view creates a Stripe paymentIntent  
2. Stripe returns the client_secret, which is returned to the template  
3. Using JavaScript on the client side, call the confirm card payment method from stripe js useing the client_secret in the template to call confirmCardPayment() and verify the card.  

### Django Countries for use with Stripe
- pip3 install django-Countries
- pip3 freeze > requirements.txt

## Stripe webhook  
1. Create a new file checkout/webhook_handler.py
2. Add webhook methods for:
    - Unhandled webhooks
    - Payment succeeded
    - Payment failed/declined
3. Add a URL path to this file in checkout/urls.py and import the webhooks function from .webhooks  
4. Create a new file checkout/webhooks.py to listen for Stripe Webhooks
https://stripe.com/docs/payments/handling-payment-events  
5. In settings.py set the stripe webhook secret key from the environment variables  
6. Add a webhook endpoint in Stripe dashboard/Developers/webhooks/add endpoint 
    - endpoint url: https://8000-c613707c-ac21-4c3b-9ef3-d0af7fd6591c.ws-eu03.gitpod.io/checkout/WH/  
    - Select 'Receive all events'
    - Click 'Add endpoint'
7. Copy the signing secret key and export it to the project using the terminal.
    - export STRIPE_WH_SECRET='webhhok secret key'
8. Use the wehooks listener to map the webhook and event type and pass it to the webhook handler  
9. Create the necessary database objects in the webhook handler
    - In stripe_elements.js add the billing details and shipping details from the form to the Stripe.confirmCardPayment method 
    so they can be passed to Stripe to be included in the webhook response  
10. Cache checkout data if user checks save info box  
    - Create a new view cache_checkout_data in order to modify the payment intent and add some metadata to it.
    - Pass the client_secret from the payment intent  
    - Extract the payment intent id from the client secret key  
    - Call the paymentIntent.modify method from Stripe passing in the clientid and the extra data to be added.
    - Add a url to the cache_checkout_data view  
11. In stripe_elements.js add the save-info data to the form.addEventListener

## UserProfileModel

## Django email  
### Set up  
1. Create new text files for the email subject and body content in the apps static folder  
2. In the Stripe webhook handler define a new class _send_confirmation_email  
3. Imports  
    - from django.core.mail import send_mail  
    - from django.core.mail import send_mail
    - from django.template.loader import render_to_string  
    
## Securing the views (Restricting edit and delete functionality to superusers)  
- Use the decorator @login_required from django.contrib.auth.decorators  

## Customising the product image input (django widgets)
- https://github.com/django/django/tree/master/django/forms/templates/django/forms/widgets  
- Create a new file products/widgets.py  
- 
 

## Checkout App
- uuid  

### Checkout models  
- Order  
- OrderLineItem  
(At time of initiation could not run migrations - Console output: No changes detected)  

### Checkout admin models  
- OrderLineItemAdminInline  
- OrderAdmin  

### Checkout Signals checkout/signals.py
- post save
- post delete

### Checkout forms checkout/forms.py
- OrderForm  

### Checkout URL's checkout.urls.py  
Add path in root level urls.py file  
- checkout

### Checkout templates  
- checkout/templates/checkout/checkout.html
(note: Extra css block example in tutorials)  


# Deployment  
- Using AWS s3 
1. Create an Heroku App  
    - project-4-blackhills-jerseys  
2. Initiate a Postgres database in the heroku app Resources tab  
    - add-ons postgres and use the free plan  
3. Install dj_database_url and psycopg2-binary with pip3 installs
4. Freeze these installs to requirements.txt
5. In settings.py import dj_database_url and change the default DATABASE to the Heroku Postgres database url found in Heroku app settings tab Config Vars.
6. Migrate this new database python3 manage.py migrate
7. Set a superuser  
    - python3 manage.py createsuperuser
8. Install gunicorn to act as the webserver
    - pip3 install gunicorn
9. Create a Procfile to initiate a web dyno
10. Add the hostname of the Heroku app to the allowed host setting in settings.py
11. Deploy to Heroku

## Django secret key generator.  
- https://miniwebtool.com/django-secret-key-generator/  
1. Generate a random secret key and add this to Heroku Config Vars SECRET_KEY =  
2. Change the SECRET_KEY setting in setting.py to read it from the os environment Config Vars  
3. Set the DEBUG flag to True only if DEVELOPMENT is in the environment  


# AWS
1. Create a new AWS s3 bucket  

## Configure bucket settings  
1. In Properties, turn on Static website hosting. 
    - Set Index document to index.html (Unused but are required fields)
    - Set Error document to error.html (Unused but are required fields)
2. In Permissions set up the cross-origin resource sharing (CORS) 
3. In Permissions generate a new bucket policy number  
    - Set Policy type = s3 bucket policy  
    - Add Statements Principle = *  
    - Add Statements Actions = get object  
    - Copy ARN number from AWS Management Console and paste to ARN fields
    - Click Add Statement 
    - Click Generate Policy  
    - Copy this policy to the Edit bucket policy and add /* to end of resource key  
4. In Permissions go to Access control list and set the list objects permission to Everyone  

## Setting up Aws bucket user rights  
1. Go to AWS Services menu and select IAM (Identity and Access Management)
2. Create a group for the user 
    - Enter a group name (manage-project-4) and skip to end
3. Create an access policy to give the group access rights to the project bucket  
    - Click Policies and Create New Policy
    - On JSON tab click Import managed policy 
    - Search for s3 and import the AmazonS3FullAccess policy
    - Enter the ARN number to Resources key list twice  
        - arn:aws:s3:::project-4-blackhills-jerseys (to allow access to the bucket)
        - arn:aws:s3:::project-4-blackhills-jerseys/* (To allow access to the bucket contents)
    - Click Create Policy, enter a name and description and Create.
4. Assign a user to the group
    - Go to Groups
    - Select the manage-project-4 group, click attach a policy and search for the policy just generated and attach.  
    - Go to Users and click Add User  
    - Create a user called project-4-staticfiles-user
    - Assign Programmatic access to this user
    - Select the group to assign this user and click through to the end to create this user.
    - On Success page download and save the CSV file. This is required in order to authenticate the Django app secret access keys.

## Connecting Django to AWS bucket  
1. Install boto3 and django-storages  
    - pip3 install boto3  
    - pip3 install django-storages  
2. Add storages to list of INSTALLED_APPS in settings.py  
3. Declare AWS secret keys and config as environment variables.
4. Set these Config Vars in Heroku
    - AWS_ACCESS_KEY_ID (Values obtained in downloaded AWS CSV file)
    - AWS_SECRET_ACCESS_KEY (Values obtained in downloaded AWS CSV file)
    - USE_AWS = True  
5. Set the AWS custom domain in settings.py  
    - AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'  

## Creating Custom storages  
Create a new file custom_storages.py  
This tells the environment where to store static and media files using S3Boto£Storages

## Cache control
Create a folder 'media' in the project AWS bucket.
Add the required project images to this folder and grand public read permissions  

## Adding Stripe secret keys  
Set the Stripe secret keys to Heroku Config Vars  
- STRIPE_PUBLIC_KEY
- STRIPE_SECRET_KEY  

# Email setup  




## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

