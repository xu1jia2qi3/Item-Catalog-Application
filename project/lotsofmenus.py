from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User

# Create database and create a shortcut for easier to update database
engine = create_engine('sqlite:///catalogs.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="test", email="test@gmail.com")
session.add(User1)
session.commit()

# Create category of soccer
category1 = Categories(user_id=1, name="soccer")
session.add(category1)
session.commit()


# Create category of basketball
category2 = Categories(user_id=1, name="basketball")
session.add(category2)
session.commit()

# Create category of baseball
category3 = Categories(user_id=1, name="baseball")
session.add(category3)
session.commit()

# Create category of Crime & frisbee
category4 = Categories(user_id=1, name="frisbee")
session.add(category4)
session.commit()

# Create category of snowboarding
category5 = Categories(user_id=1, name="snowboarding")
session.add(category5)
session.commit()

# Create category of rock climbing
category6 = Categories(user_id=1, name="rock climbing")
session.add(category6)
session.commit()

# Create category of foosball
category7 = Categories(user_id=1, name="foosball")
session.add(category7)
session.commit()

# Create category of skating
category8 = Categories(user_id=1, name="skating")
session.add(category8)
session.commit()

# Create category of hockey
category9 = Categories(user_id=1, name="hockey")
session.add(category9)
session.commit()


# Add Items into categories
categoryItem1 = CategoryItem(user_id=1, name="soccer 1",
                             description="This is soccer 1 !!!",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="soccer 2",
                             description="This is soccer 2 !!!",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="basketball 1",
                             description="This is basketball 1 !!!",
                             categories=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="basketball 2",
                             description="This is basketball 2 !!!",
                             categories=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="baseball 1",
                             description="This is basketball 1 !!!",
                             categories=category3)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="baseball 2",
                             description="This is baseball 2 !!!",
                             categories=category3)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="frisbee 1",
                             description="This is frisbee 1 !!!",
                             categories=category4)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="frisbee 2",
                             description="This is frisbee 2 !!!",
                             categories=category4)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="snowboarding 1",
                             description="This is snowboarding 1 !!!",
                             categories=category5)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="snowboarding 2",
                             description="This is snowboarding 2 !!!",
                             categories=category5)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="rock climbing 1",
                             description="This is rock climbing 1 !!!",
                             categories=category6)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="rock climbing 2",
                             description="This is rock climbing 2 !!!",
                             categories=category6)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="foosball 1",
                             description="This is foosball 1 !!!",
                             categories=category7)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="foosball 2",
                             description="This is foosball 2 !!!",
                             categories=category7)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="skating 1",
                             description="This is skating 1 !!!",
                             categories=category8)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="skating 2",
                             description="This is skating 2 !!!",
                             categories=category8)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="hockey 1",
                             description="This is hockey 1 !!!",
                             categories=category9)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="hockey 2",
                             description="This is hockey 2 !!!",
                             categories=category9)
session.add(categoryItem1)
session.commit()
print ("added category items!")