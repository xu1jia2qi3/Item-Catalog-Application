from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from database_setup import *

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Delete Category if exisitng.
session.query(Category).delete()
# Delete Items if exisitng.
session.query(Items).delete()
# Delete Users if exisitng.
session.query(User).delete()

# Create fake users
User1 = User(
    name="test",
    email="test@gmail.com",
    picture='http://dummyimage.com/200x200.png/ff4444/ffffff')
session.add(User1)
session.commit()

# Create category of soccer
Category1 = Category(name="soccer", user_id=1)
session.add(Category1)
session.commit()

# Create category of basketball
Category2 = Category(name="basketball", user_id=1)
session.add(Category2)
session.commit()

# Create category of baseball
Category3 = Category(name="baseball", user_id=1)
session.add(Category3)
session.commit()

# Create category of Crime & frisbee
Category4 = Category(name="frisbee", user_id=1)
session.add(Category4)
session.commit()

# Create category of snowboarding
Category5 = Category(name="snowboarding", user_id=1)
session.add(Category5)
session.commit()

# Create category of rock climbing
Category6 = Category(name="rock climbing", user_id=1)
session.add(Category6)
session.commit()

# Create category of foosball
Category7 = Category(name="foosball", user_id=1)
session.add(Category7)
session.commit()

# Create category of skating
Category8 = Category(name="skating", user_id=1)
session.add(Category8)
session.commit()

# Create category of hockey
Category9 = Category(name="hockey", user_id=1)
session.add(Category9)
session.commit()

# Add Items into Category
Item1 = Items(
    name="soccer 1",
    date=datetime.datetime.now(),
    description="This is soccer 1 !!!",
    picture="a",
    category_id=1,
    user_id=1)
session.add(Item1)
session.commit()

Item2 = Items(
    name="basketball 1",
    date=datetime.datetime.now(),
    description="This is basketball 1 !!!",
    picture="",
    category_id=2,
    user_id=1)
session.add(Item2)
session.commit()

Category1 = Category(name="Football", user_id=1)
session.add(Category1)
session.commit()

print("added category items!")
