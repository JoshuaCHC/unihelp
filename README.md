<!-- 
- the purpose of the web application, explaining both the context and the assessment mechanism used.
- the architecture of the web application.
- describe how to launch the web application.
- describe some unit tests for the web application, and how to run them.
- Include commit logs, showing contributions and review from both contributing students 
-->




# CITS3403 Agile Web Development Project 2021
# Uni-Safe Online Formative Assessment
Building a web application that simulates a learning experience with learning assessments, results and feedback for users. 

## Our team
- [Joshua Cheng (22708023)](https://github.com/JoshCUni)
- [Matthew Walsh (22734017)](https://www.example.com)
- [Shana Edwards (22479434)](https://github.com/shana-edwards)
- [Tatum Botha (22976568)](https://github.com/tatum-botha)

## Purpose of the web application
<!-- explain both the context and the assessment mechanism used (multi-choice) -->
Our team created a webpage aimed at UWA students, to educate them about university health and safety, providing handy tips, tricks, and resources to develop their skills when it comes to 
staying safe and healthy during the semester.

## Architecture


## Database schema
<!-- user and score tables -->

## Launching the application
To launch the application from local host:

Install all requirements for the web application using:

``` $ pip install -r requirements.txt ``` 

In the terminal at the root directory of the web page, tell flask where to find the application:

``` $ export FLASK_APP=web.py ```

Now run the application:

``` $ flask run ```


## Dependencies and requirements
Requirements:
- click==7.1.2
- Flask==1.1.2
- itsdangerous==1.1.0
- Jinja2==2.11.3
- MarkupSafe==1.1.1
- Werkzeug==1.0.1
- alembic==1.6.2
- Flask-Login==0.5.0
- Flask-Migrate==2.7.0
- Flask-SQLAlchemy==2.5.1
- greenlet==1.1.0
- Mako==1.1.4
- python-dateutil==2.8.1
- python-dotenv==0.17.1
- python-editor==1.0.4
- six==1.16.0
- SQLAlchemy==1.4.14
- WTForms==2.3.3


## Unit tests
<!-- Explain how to run these as well! -->

```Python
class UserModelCase(unittest.TestCase):

    setUp(self):

    tearDown(self):
    - resets the database, removing any existing content

    test_password_hash(self):
    - checks that the password hashing is working correctly
    - does this using the check_password method

    test_top_players(self):
    - tests that the ranking of the top players is done correctly

    test_avg_mark(self):
    - tests average mark is correct
    - compares mark to manual avg calculation of the three scores

    test_add_marks(self):
    - 


```

```Python
class GoogleTestCase(unittest.TestCase):

    setUp(self):

    tearDown(self):

    testPageTitle(self):

    testRegister(self):

    test_quiz_marks(self):




```


## Screenshots


## References - Images
<!-- ieee referencing... -->


