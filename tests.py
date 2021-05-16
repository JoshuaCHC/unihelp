import unittest
from app import app, db
from app.models import User, Marks
from app.routes import add_marks
import random as rand
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

#TEST PASSWORDS
#CAN WRITE TEST FIRST THEN WRITE THE CODE TO MEET THE TEST REQUIREMENTS
class UserModelCase(unittest.TestCase):
    def setUp(self):
        #MEMORY DB
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hash(self):
        #MAKE USER HERE FROM USER MODEL
        u = User(username = 'admin')
        u.set_password('admin')

        self.assertFalse(u.check_password('admin1'))
        self.assertTrue(u.check_password('admin'))

    def test_top_players(self):
        plist = []
        for i in range(15):
            u = User(username = 'g{}'.format(i), email = 'e{}@gmail.com'.format(i))
            if(i < 5):
                m1 = 5
                m2 = 5
                m3 = 5-i
            elif(i < 10):
                m1=5
                m2=10-i
                m3=0
            elif(i<15):
                m1=15-i
                m2=0
                m3=0
            m = Marks(mod1=m1, mod2 = m2, mod3 = m3, user = u)
            m.update_avg_mark()
            self.assertEqual(m.avg_mark, '{:.2f}'.format((m1+m2+m3)/3))
            plist.append([u,m])
            db.session.add(u)
            db.session.add(m)
            print(u.username)
            db.session.commit()
        t1 = User.query.join(Marks).filter(User.id == Marks.user_id).order_by(Marks.avg_mark.desc()).with_entities(User.username, Marks.avg_mark, User.email).limit(10).all()
        for i in range(10):
            self.assertEqual(t1[i],(plist[i][0].username, plist[i][1].avg_mark, plist[i][0].email))
        
    def test_avg_mark(self):
        u = User(username = 'new_user', email = 'new_user@g.com')
        mod1 = rand.randint(0,5)
        mod2 = rand.randint(0,5)
        mod3 = rand.randint(0,5)
        m = Marks(mod1 = mod1, mod2= mod2, mod3=mod3, user=u)
        m.update_avg_mark()
        self.assertEqual(m.avg_mark, '{:.2f}'.format((mod1+mod2+mod3)/3))
        
    def test_add_marks(self):
        u = User(username='new_user', email = 'new_user@b.com')
        
    # def test_follow(self):
    #     u1 = User(username = 'g1', email = 'e1')
    #     u2 = User(username = 'g2', email = 'e2')

    #     db.session.add(u1)
    #     db.session.add(u2)

    #     db.session.commit()
    #     #USERS HAVE A FOLLOWED PROPERTY, SO ALL GETS ALL OF THE VALUES IN THAT
    #     self.assertEqual(u1.followed.all(),[])
    #     self.assertEqual(u2.followed.all(),[])

    #     u1.follow(u2)
    #     #We can write this function

    #     db.session.commit()

    #     self.assertTrue(u1.is_following(u2))
    #     self.assertEqual(u1.followed.count(),1)
    #     self.assertEqual(u1.followed.first().username, 'g2')
    #     #Check the other way as well.

    #     # Then do the same thing for unfollow.
    #     #I'll need to do this for adding marks etc


class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        # self.addCleanup(self.driver.close())

    def testPageTitle(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.assertIn('Unihelp', self.driver.title)

    def testRegister(self):
        self.driver.get('http://127.0.0.1:5000/register')
        user = self.driver.find_element_by_id('uname')
        email = self.driver.find_element_by_id('email')
        pwd = self.driver.find_element_by_id('pswd')
        cpwd = self.driver.find_element_by_id('cpswd')
        reg = self.driver.find_element_by_id('register')
        user.send_keys('user1')
        email.send_keys('gg@gmail.com')
        pwd.send_keys('1234')
        cpwd.send_keys('1234')
        ActionChains(self.driver).click(reg).perform()
        q = User.query.filter_by(username = 'user1')
        self.assertEqual(q.username, 'user1')
        self.assertEqual(q.email, 'gg@gmail.com')
        m = Marks.query.filter_by(user = q).first()
        self.assertEqual(m.mod1, 0)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)




