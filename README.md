<img src="https://res.cloudinary.com/dfboxofas/image/upload/v1611675581/project-4/blackhillls_logo_qgtqtm.png" style="height: 50px">
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
5. As a user I would like to be able to order a particular jersey and specify it's size.
6. As a user I would like to be assured that any contact and billing information is dealt with in a secure manner.

### As an Owner
1. As an owner I would like to be able to showcase our products to our customers.
2. As an owner I would like to be notified of any orders submitted and be able view them as a superuser and that they are not accessible to anybody else.
3. As an owner I would like to be able to contact the person who submitted the order.
4. As an owner I would like top be able to keep the final product secure until a verified payment is made whereby the final product is immediately released to the client.
5. As an owner I would like to be able to gather a testimonials from our clients.
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
The main fonts used are Bangers and Roboto from Google Fonts. Bangers is the style of the brand logo so it is continued in a descrete fashion throughout the site on the buttons which bring the user through the full visit and checkout experience. It was chosen as it reflects a casual yet sharp style. Roboto is used for all other text as it is a clean well spaced font and easy on the eye.

### Source libraries  
1. Django framework
2. Bootstrap4 
3. Fontawesome  
4. Stripe javascript  
5. jQuery  

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


## Project level base templates  
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

## Project Apps  
### Allauth  
Django Allauth is used for controlling user registration, login verification, and password encryption.   
- pip3 install django-allauth  
- Set up reference guide https://django-allauth.readthedocs.io/en/latest/installation.html  
### Home App  
This app holds the files for any static pages on the site such as the home page and any other generic pages such as Terms and Conditions, Privacy Policy if applicable. In this project the only Home page is held in this app folder.   

Home app views:
- index  

Home app url's:
- path('', views.index, name='home')
- path('home2/', views.home2, name='home2')  

### Products App  
This app holds the files for all the product applications such as the Products page and Product Details page. It also contains the files for the Admin Product Management for adding, editing, deleting Products from the site.  

Products app views:
- all_products  
- product_detail  
- add_product  
- edit_product  
- delete_product    

Products app url's:
- path('', views.all_products, name='products')
- path('<int:product_id>/', views.product_detail, name='product_detail')
- path('add/', views.add_product, name='add_product')
- path('edit/<int:product_id>/', views.edit_product, name='edit_product')
- path('delete/<product_id>/', views.delete_product, name='delete_product')

### Shopping Bag App 
The shopping bag app holds all the files for configuring, and totalling the products a user has added, edited, deleted in their shopping bag.

Shopping Bag app views:
- view_shopping_bag  
- add_to_shopping_bag  
- edit_shopping_bag  
- remove_from_shopping_bag  

Shopping Bag app url's:  
- path('', views.view_shopping_bag, name='view_shopping_bag')
- path('add/<item_id>/', views.add_to_shopping_bag, name='add_to_shopping_bag')
- path('edit/<item_id>/', views.edit_shopping_bag, name='edit_shopping_bag')
- path('remove/<item_id>/', views.remove_from_shopping_bag, name='remove_from_shopping_bag')

Shopping Bag context_processor:  
A context processor is used for storing the users shopping bag contents so it is available for accessing site wide.  

### Checkout App  
This checkout app holds all the files and functionality for a user to purchase a product securely and it contains the payment gateway to Stripe.  

Checkout app views:
- checkout  
- checkout_success  
- cache_checkout_data  

Checkout app url's:  
- path('', views.checkout, name='checkout')
- path('checkout_success/<order_number>', views.checkout_success, name='checkout_success')
- path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data')
- path('WH/', webhook, name='webhook')

## Checkout App order number generator (uuid)  
To generate a unique order number for each order Django uuid is used. This will give a random string of 32 characters as a unique identifier to each order submitted.  

### Stripe checkput
1. The checkout view creates a Stripe paymentIntent  
2. Stripe returns the client_secret, which is returned to the template  
3. Using JavaScript on the client side, call the confirm card payment method from stripe js useing the client_secret in the template to call confirmCardPayment() and verify the card.  

### Stripe webhook  
1. Create a new file checkout/webhook_handler.py
2. Add webhook methods for:
    - Unhandled webhooks
    - Payment succeeded
    - Payment failed/declined
3. Add a URL path to this file in checkout/urls.py and import the webhooks function from .webhooks  
4. Create a new file checkout/webhooks.py to listen for Stripe Webhooks
    [Stripe docs - Payment intents](https://stripe.com/docs/payments/handling-payment-events)  
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

### Django Countries for use with Stripe  
The Stripe payment gateway requires a 2 character abbreviation for the country field. In order to prevent user error and to ensure the country field return a 2 character string Django Countries is used. This gives us the ability to load the country field with the labels set as the full country name but the value will be the 2 character string of the country selected.
- pip3 install django-Countries
- pip3 freeze > requirements.txt

### Profiles App  
The profiles app contains the files for storing users personal credentials.  

Profiles app views:
- profile  
- order_history
- add_review  
- edit_review 
- delete_review  

Profiles app url's:  
- path('', views.profile, name='profile'),
- path('order_history/<order_number>',  views.order_history, name='order_history')
- path('add_review/<product_id>/', views.add_review, name='add_review')
- path('edit_review/<review_id>/', views.edit_review, name='edit_review')
- path('delete_review/<review_id>/', views.delete_review, name='delete_review')

## CSS stylesheets  
In development environment: 
CSS stylesheets can be kept locally or globally. Global CSS stylesheets are held in the root level static folder. Local CSS stylesheets can be held in the App static folders.  
In production environment: 
All stylesheet files are held in the AWS project bucket/static.

## Media files  
In development environment: 
Media files are held in the root level media folder.  
In production environment: 
All media files are held in the AWS project bucket/media. 

## Testing  
### Testing the templates  
Go to each page in turn and verify the page and contents display correctly.
1. / - Verify the home page is displayed  
2. /products - Verify the products page is displayed  
3. /product/<productid> - Verify the product details page is displayed  
4. /bag - Verify the Shopping bag page is displayed  
5. /profile - Verify the profile page is displayed  
6. /checkout - Verify the checkout page is displayed. 
7. /login - Verify the login page is displayed  
8. /Register - Verify the register page is displayed  

### Testing functionality  
#### allAuth Registration test 
1. Go to registration page and submit login form.
2. Verify email verification page is displayed.
3. Verify verification email is received.
4. Verify visiting the link in the email completes the registration process.  

#### allAuth Login/logout test
1. Go to login in page and submit the form.
2. Verify user is logged in correctly.  
3. Click logout link in navbar and verify user is logged out correctly.

#### Sidebar filter tests
1. Go to products page and verify sidebar triggers correctly.  
2. Verify all checkboxes are ticked by default and all products are displayed.
3. Uncheck some of the checkboxes and verify the products are filtered out correctly.  
4. Verify the All checkbox checks and unchecks all other checkboxes in the sidebar menu.  

#### Product details test  
1. Go to product details of a product.  
2. Verify a user can select quantities and size of a particular product.  

#### Reviews  
1. Verify the reviews modal on a product with reviews opens and closes.
2. Verify all reviews for that product are listed on the modal.  

#### Add/Edit/Delete reviews test  
1. Verify a user must be logged in to be able to add a review.
2. Log in and add a review to a product.  
3. Go to profile page, edit and verify the review can be edited and deleted.  
4. Add another review and log out.
5. Verify the review added cannot be edited by entering /edit_review/<review_id> in the url.  
6. Verify the review added cannot be deleted by entering /delete_review/<review_id> in the url.  

#### Shopping bag test
1. Add several items of various sizes and quantities of each.
2. Click on the shopping bag icon in the navbar to go to the shopping bag page.  
3. Verify size, quantities and subtotals are correct for each item added.
4. Verify total, delivery, and grand totals are correct.  
5. Verify a user can edit and delete any item in their shopping bag. 

#### Checkout test  
1. Go to checkout page and submit the form using a Stripe test card number.  
    - [Stripe docs - Testing](https://stripe.com/docs/testing)
2. Verify the user is brought to the checkout success page with the order details displayed.  
3. Go to Stripe dashboard > Developers > logs and verify a payment intent was created, the payment was charged, and the payment was successful.  

#### Checkout Stripe webhook test  
In case there is a problem with the connection between the server and the user and a Stripe callback cannot be made at the time of payment execution a Stripe webhook is used to complete the payment and safely store the order to the database.  
The Stripe webhook endpoint can be tested in 2 ways:  
1. By ommitting the form.send() command on the checkout page. This will force the server to initiate the callback using the webhook endpoint.  
2. Webhook endpoints can be manually triggered from the Stripe dashboard > webhooks. This will trigger a generic callback response to the endpoint provided.  

#### Securing the views test (Restricting certain functionality to registered users only)  
@login_required from django.contrib.auth.decorators  
Restricted content and functionality includes:  
- Functionality of adding, editing, or deleting a review.  
- Access to the Profile page.  
- Access to order_history content.  
- Access to Product Management pages. 
1. Log out and manually force a url to restricted content.  
2. Verify the content access is denied and the user is brought to the home page with an error message displayed. 
3. Verify that only the superuser has access to the Product Management page. 

## Deployment  
This projects repository is held in GitHub and is hosted with Heroku Apps. Deployment to Heroku Apps is done from the GitHub master branch.

GitHub repository: https://github.com/PeterKellett/project-3
Deployment procedure to implement new functionality
Go to project repository above and create a new upstream branch or raise an issue, this will also create an upstream branch.
Open this branch or issue in code editor. For this project GitPod was used.
Add and commit code to this branch until satisfied code can be merged with the main branch.
Send a pull request to GitHub requesting the branch can be merged.
If there are no conflicts raised this branch or issue can then be closed by performing a merge onto the main branch. A merge can also be performed from GitPod.
This GitHub repository master branch is automatically connected to Heroku through Heroku settings so any merges to the GitHub master branch are automatically deployed and built in Heroku.
Deployment procedure to clone this project
Go to project repository above and click 'Code' button

Copy the url (see image below and for full instructions see https://docs.github.com/en/enterprise/2.13/user/articles/cloning-a-repository) Screenshot  


### Using AWS s3 
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

A full project set up procedure can be seen here:  
[Full project set up procedure](https://github.com/PeterKellett/project-4/blob/master/PROJECTSETUP.md)  

--------------------------------------------------------------------------------------------

   

## Customising the product image input (django widgets)
- [Django docs - widgets](https://github.com/django/django/tree/master/django/forms/templates/django/forms/widgets) 
- Create a new file products/widgets.py  


### Checkout Signals checkout/signals.py
- post save
- post delete

### Checkout forms checkout/forms.py
- OrderForm  



# Email setup  
