<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

# PeterKellett - Milestone Project 4

## Project initial set up
1. Install Django 
    - pip3 install django (v20.2.4 installed)
2. Create the project root files
    - django-admin startproject project_4 .
3. Create a .gitignore file
    - touch .gitignore
    - Add *.sqlite, *.pyc, __pycache__ to .gitignore file
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
Ref: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
    - EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
2. Set up AUTHENTICATION methods
Ref: https://django-allauth.readthedocs.io/en/latest/configuration.html?highlight=ACCOUNT_AUTHENTICATION_METHOD#configuration
    - ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
    - ACCOUNT_EMAIL_REQUIRED = True
    - ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
    - ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
    - ACCOUNT_USERNAME_MIN_LENGTH = 4
    - LOGIN_URL = '/accounts/login/'
    - LOGIN_REDIRECT_URL = '/'
3. MAnually set superuser email to both verified and primary via django site admim
4. 



## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

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

--------

Happy coding!
