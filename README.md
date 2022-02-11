Yihui Fang
011679103
Fiance/Computer Sience 

    * app
            * __init__.py            Python script that initializes the `app` module. 
            * Controller
                * __init__.py            Python script that initializes the `Controller` module. 
                * auth_forms.py          Flask-WTF forms for authentication use cases, i.e., "registering a new user" and "login". 
                * forms.py               Flask-WTF forms for "creating a post" and "sorting all posts". 
                * errors.py              Error handlers for 404 and 505 errors
                * auth_routes.py         Routes handling authetication, i.e., "registering a new user" and "login". 
                * routes.py              Other routes
            * Model
                * __init__.py            Python script that initializes the `Model` module. 
                * models.py              Database models
            * View
                * static
                    * css
                        * main.css
                    * img 
                        * happiness-level-1.png  image for happiness-level-1
                        * happiness-level-2.png  image for happiness-level-1
                        * happiness-level-3.png  image for happiness-level-1
                        * like.png, like_hover.png      icons for like button
                * templates
                    * 404error.html      HTML template page for displaying 404 errors
                    * 500error.html      HTML template page for displaying 500 errors
                    * _post.html         HTML sub-template for displaying a smile post
                    * base.html          Base “skeleton” template that contains all the common elements of HTML pages.  
                    * create.html        HTML template for create post page
                    * index.html         HTML template for the main page 
                    * login.html         HTML template for the login page 
                    * register.html      HTML template for the user sign-up page 
    * tests
            * __init__.py            Python script that initializes the `tests` module. 
            * test_models.py         Tests for the `model` ; uses `unittest` framework
            * test_routes.py         Tests for the rotes ; uses `pytest` framework 
    * requirements.txt             Lists all the dependencies (required packages), along with their versions.
    * .flaskenv                    
    * config.py                    Python script that defines app's configuration variables 
    * smile.py                     Main application file
