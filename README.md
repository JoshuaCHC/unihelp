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
HTML, CSS, and JavaScript were used to design the client-side of the web application, with Python, Flask, and SQAlchemy used for the server-side.


## Agile Development Approach
We used an agile approach to manage our project in the following ways: 
- broke the project up into smaller tasks with priorities and time targets. 
- assigned these smaller tasks to group members according to what we were each most comfortable with, eg: "This week one team member will work on the content for our learning module, another will focus on the styling, another works on the assessment design, and another creates a login page."
- had regular meetings in which we worked together on the project as well as presenting what we had been individually working on
- face-to-face conversation as much as Covid-19 would allow
- prioritised working software, continuously commiting and pushing it to GitHub


## Database Schema
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
- alembic==1.6.2
- click==7.1.2
- Flask==1.1.2
- Flask-Login==0.5.0
- Flask-Migrate==2.7.0
- Flask-SQLAlchemy==2.5.1
- Flask-WTF==0.14.3
- greenlet==1.1.0
- itsdangerous==1.1.0
- Jinja2==2.11.3
- Mako==1.1.4
- MarkupSafe==1.1.1
- python-dateutil==2.8.1
- python-dotenv==0.17.1
- python-editor==1.0.4
- selenium==3.141.0
- six==1.16.0
- SQLAlchemy==1.4.14
- urllib3==1.26.4
- Werkzeug==1.0.1
- WTForms==2.3.3


## Unit Tests
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
    - sets up browser testing, checking that the webpage is running correctly on the browser
    - does this with chrome driver

    tearDown(self):
    - closes the browser window that the driver is currently on

    testPageTitle(self):
    - checks that page title is correct

    testRegister(self):
    - tests user registration to ensure it is working correctly

    test_quiz_marks(self):
    - testing for the quiz results
```


## Screenshots

The planning process begun with drawing out ideas and creating a powerpoint to play with different layouts.

![Planning Powerpoint](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/pwrpoint.jpg)

![Planning page1](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/plan1.jpg)

![Planning page2](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/plan2.jpg)

![Planning page3](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/plan3.jpg)

Starting at the home page, you can navigate through the webpage, accessing an about page or heading to the login page. 
The login page allows returning users to login and new users to register a new account. 
After logging in, a user can access the three learning modules, take quizzes, see their results, and then view their ranking compared with other users.

Home page:

![Home page](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/home.png)

About page:

![About page](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/about.png)

Login page:

![Login page](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/login.png)

Home page for the modules:

![Module home page](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/modulehome.png)

Module pages:

![Modules page](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/modules.png)

Results page:

![Results page](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/results.png)

Ranking page:

![Ranking page](https://github.com/JoshCUni/unihelp/blob/main/app/static/images/ranking.png)


## Images Used
Home_Page


Perkinsbuilders.com.au, 2019. [Online]. Available: https://www.perkinsbuilders.com.au/wp-content/uploads/2020/05/UWA_EZONE275_001_small-Copy.jpg. [Accessed: 1-May-2021]

Login:

Bellvuestudents.co.uk, 2021. [Online]. Available: https://www.bellvuestudents.co.uk/wp-content/uploads/2016/11/shutterstock_276679427.jpg. [Accessed: 2-May-2021]

Results:

GIPHY, “Excited Season 2 GIF by The Office - Find & Share on GIPHY,” GIPHY, 2020. https://media.giphy.com/media/IwAZ6dvvvaTtdI8SD5/giphy.gif (accessed April 15, 2021).


Shopify.com, 2021. [Online]. Available: https://cdn.shopify.com/s/files/1/1061/1924/products/Sad_Face_Emoji_1024x1024.png?v=1571606037. [Accessed: 16-May-2021]

About:

Cloudfront.net, 2021. [Online]. Available: https://dm0qx8t0i9gc9.cloudfront.net/watermarks/image/rDtN98Qoishumwih/graphicstock-young-smiling-man-sitting-at-the-table-with-glass-and-bottle-of-wine-happy-man-drinking-wine-at-restaurant-cheerful-man-enjoying-a-drink-at-wine-bar-vector-flat-design-illustration-square-layout_SX6BAcIIb_SB_PM.jpg. [Accessed: 1-May-2021]


Istockphoto.com, 2021. [Online]. Available: https://media.istockphoto.com/vectors/students-on-a-book-pile-vector-id951047480?k=6&m=951047480&s=612x612&w=0&h=wCWzjKLuQMbIR1KvnqjzX8uJzxGIM9bMk6TXkqvgi4w=. [Accessed: 2-May-2021]


Calmedtrainingcenter.com, 2021. [Online]. Available: https://calmedtrainingcenter.com/wp-content/uploads/2017/12/CPR_BLS.png. [Accessed: 15-April-2021]

Home Module:

Healthyactivebydesign.com.au, 2021. [Online]. Available: https://www.healthyactivebydesign.com.au/images/uploads/Case_Studies/WA/UWA4_Cropped.jpg. [Accessed: 6-May-2021]

Module 1

Cloudfront.net, 2019. [Online]. Available: https://d2ebzu6go672f3.cloudfront.net/media/content/images/H0819b_costo(1).jpg. [Accessed: 5-May-2021]

Researchgate.net, 2021. [Online]. Available: https://www.researchgate.net/profile/Pantelis-Nikolaidis/publication/332621009/figure/fig3/AS:751207572312077@1556113250973/Location-of-chest-compression.ppm. [Accessed: 10-May-2021]

Module 2

S. Irl et al., “”, [Online]. Available: https://www.cm.uwa.edu.au/__data/assets/pdf_file/0006/3377976/UWA-Help-points-and-walksafe-routes-09-2018.pdf. [Accessed: 3-May-2021]

transport.uwa.edu.au, “Crawley Campus Parking Map.” Accessed: Apr. 20, 2021. [Online]. Available: https://www.transport.uwa.edu.au/__data/assets/pdf_file/0007/148948/UWA-Parking-map-2020.pdf

References for module 1:
“How to perform CPR,” Healthdirect.gov.au, May 06, 2021. https://www.healthdirect.gov.au/how-to-perform-cpr (accessed May 1, 2021).

“First aid fact sheet,.” [Online]. Available: https://stjohn.org.au/assets/uploads/fact%20sheets/english/Fact%20sheets_recovery%20position.pdf.
