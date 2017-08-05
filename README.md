# Expense Tracker

Expense tracker is an app that allows you to track your expenses

#### Features

    * User sign up
    * User log in / log out
    * Expense exhibition
    * Expense creation
    * Expense edit
    * Expense deletion

# Running

#### Check out repository
    
    $ git clone https://github.com/luizpericolo/expense_tracker.git

#### Install requirements
Use a virtualenv with python3

    $ pip install -r requirements.txt

#### Export variables

    $ export MONGO_DB_USER=webapp_user
    $ export MONGO_DB_PASSWORD=9225zNLTZA3Y
    $ export SECRET_KEY=6WVXPhhjVTv06RY51KY0rlZsQrK2BJtJ


#### Run
    
    $ chmod a+x run.py
    $ ./run.py
    

# Next steps

    * Add more tracking features that were not added due to lack of time
    * Add request authentication via HTTP header
    * Turn into Single Page App and backend into Rest API