<!-- TODO
 - screenshots
 - update requirements
 - image referencing -->


# CITS3403 Agile Web Development Project 2021
# Uni-Safe Online Formative Assessment
Building a web application that simulates a learning experience with learning assessments, results and feedback for users. 

## Our Team
- Joshua Cheng (22708023)
- Matthew Walsh (22734017)
- Shana Edwards (22479434)
- Tatum Botha (22976568)


## Purpose
The purpose of our webpage is to educate UWA students about university health and safety, providing handy tips, tricks, and resources to develop their skills when it comes to staying safe and healthy during the semester.

We teach this content through a selection of modules with attached multiple-choice quizzes assessing the user's learning as they progress through each module.

Immediate results are displayed after each multiple-coice quizz, as well as a final results page providing an summary of the user's results overall. Users will be able to compare their overall results to other users via the rankings page which presents a leaderboard with the current top users.


## Architecture
Our webpage uses a client-server architecture, with the one server and database responding to many clients.
HTML, CSS, and JavaScript were used to design the client-side of the web applciation, with Python, Flask, and SQAlchemy used for the server-side.


## Agile Development Approach
We used an agile approach to manage our project in the following ways: 
- broke the project up into smaller tasks with priorities and time targets. 
- assigned these smaller tasks to group members according to what we were each most comfortable with, eg: "This week one team member will work on the content for our learning module, another will focus on the styling, another works on the assessment design, and another creates a login page."
- had regular meetings in which we worked together on the project as well as presenting what we had been individually working on
- face-to-face conversation as much as Covid-19 would allow
- prioritised working software, continuously commiting and pushing it to GitHub


## Database Schema
<!-- user and score tables -->
![Schema](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/dbschema.png)


## Launching the Application
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


## Requirements
<!-- update the requirements last minute -->
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


## Unit Tests
<!-- Explain how to run these as well! -->
To run the unit tests, type the following command into the terminal:  ``` python tests.py ```

```Python
class UserModelCase(unittest.TestCase):

    setUp(self):
    - sets up a database for the testing

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
```

```Python
class GoogleTestCase(unittest.TestCase):

    setUp(self):

    tearDown(self):

    testPageTitle(self):
    - checks that page title is correct

    testRegister(self):
    - tests user registration to ensure it is working correctly

    test_quiz_marks(self):
    - testing for the quiz results
```


## Screenshots
<!-- of all pages and include images of all drafting - powerpoint and everything etc. -->


## Images Used
<!-- ieee referencing... -->
<!-- 
- home page:
- about page: 
- modules:
- log in and results etc.:
 -->

![Planning Powerpoint](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/pwrpoint.jpg)
![Planning page1](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/plan1.jpg)
![Planning page2](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/plan2.jpg)
![Planning page3](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/plan3.jpg)
![Home page](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/home.png)
![About page](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/about.png)
![Login page](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/login.png)
![Module home page](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/modulehome.png)
![Modules page](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/modules.png)
![Quiz page](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/Quiz.png)
![Results page](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/results.png)
![Ranking page](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/ranking.png)
 