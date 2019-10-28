# impacct-campaign
Campaign builder for developed for IMPACCT Brooklyn

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://python.org)

## Getting Started for Windows

* Create and activate an environment
  * In Command Prompt, navigate to the flaskBackend folder
    ```
    ...
    cd impacct-campaign
    cd flaskBackend
    ```
  * Install virtualenv
    ```
    pip install virtualenv
    ```
  * Create an environment
    ```
    virtual env
    ```
  * Activate the environment
    ```
    .\env\Scripts\activate.bat
    ```

* Install the necessary modules
  * Install Flask
    ```
    pip install Flask
    ```
* Run the application
  ```
  set FLASK_APP=app.py
  python -m flask run
  ```
* Now head over to [http://127.0.0.1:5000/api/simplelist](http://127.0.0.1:5000/api/simplelist)
* Close the application
  ```
  Ctrl+c
  ```
* Close the virtual environment
  ```
  deactivate
  ```

## Getting Started for Mac and Linux

* Create and activate an environment
  * In Command Prompt, clone the repo and navigate to the folder
    ```
    ...
    git clone https://github.com/kkalucha/impacct-campaign.git
    cd impacct-campaign
    ```
  * Install virtualenv
    ```
    pip install venv
    ```
  * Create an environment
    ```
    venv env
    ```
  * Activate the environment
    ```
    source env/bin/activate
    ```

* Pull the database locally
  * Create the database
    ```
    createdb no_harassment
    ```
  * Migrate the tables
    ```
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    ```
  * Pull the database
    ```
    heroku pg:pull postgresql-silhouetted-52506 no_harassment
    ```

* Run the server locally
  ```
  python manage.py runserver
  ```
  
* Now head over to [http://127.0.0.1:5000/getall](http://127.0.0.1:5000/getall)
* Close the application
  ```
  Ctrl+c
  ```
* Close the virtual environment
  ```
  deactivate
  ```

## Authors

* **Angela Zhang**

* **Arya Zhao**

* **Justin Lee**

* **Kanav Kalucha**

* **Luvena Huo**

* **Mustafa Eyceoz**
