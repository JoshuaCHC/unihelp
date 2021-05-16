<!-- 
- the purpose of the web application, explaining both the context and the assessment mechanism used.
- the architecture of the web application.
- describe how to launch the web application.
- describe some unit tests for the web application, and how to run them.
 -->

 <!-- TODO
 - architecture
 - describe the unit tests
 - agile
 - screenshots
 - database schema
 - update requirements
 - image referencing -->


# CITS3403 Agile Web Development Project 2021
# Uni-Safe Online Formative Assessment
Building a web application that simulates a learning experience with learning assessments, results and feedback for users. 

## Our team
- Joshua Cheng (22708023)
- Matthew Walsh (22734017)
- Shana Edwards (22479434)
- Tatum Botha (22976568)

## Purpose
<!-- explain both the context and the assessment mechanism used (multi-choice) -->
The purpose of our webpage is to educate UWA students about university health and safety, providing handy tips, tricks, and resources to develop their skills when it comes to staying safe and healthy during the semester.

We teach this content through a selection of modules with attached multiple-choice quizzes assessing the user's learning as they progress through each module.

Immediate results are displayed after each multiple-coice quizz, as well as a final results page providing an summary of the user's results overall. Users will be able to compare their overall results to other users via the rankings page which presents a leaderboard with the current top users.

## Architecture




## Agile



## Database schema
<!-- user and score tables -->

## Launching the application
To launch the application from local host:

Install all requirements for the web application using:

``` $ pip install -r requirements.txt ``` 

In the terminal at the root directory of the web page, tell flask where to find the application:

``` $ export FLASK_APP=web.py ```

Adding in the database:

``` $ flask db init ```

``` $ flask db migrate ```

``` $ flask db upgrade```

Now run the application:

``` $ flask run ```




## Dependencies and requirements
<!-- update the requirements last minute -->
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
To run the web application unit tests, run the following line in terminal:
``` pythontests.py ```

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
<!-- of all pages and include images of all drafting - powerpoint and everything etc. -->


## References - Images
<!-- ieee referencing... -->


