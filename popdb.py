from app import app, db
from app.models import User, Marks
import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
f = Marks.query.all()
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
    db.session.add(u)
    db.session.add(m)
db.session.commit()
for i in f:
    i.update_avg_mark()
    db.session.commit()
