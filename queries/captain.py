from data import db_session
from data.user import User

db_session.global_init("db/mars_explorer.db")
session = db_session.create_session()

captain = User(
    surname="Scott",
    name="Ridley",
    age="21",
    position="captain",
    speciality="research engineer",
    address="module_1",
    email="scott_chief@mars.org"
)

session.add(captain)

engineer = User(
    surname="Rex",
    name="Bexc",
    age="24",
    position="engineer",
    speciality="ok",
    address="module_2",
    email="rex_bexc@mars.org"
)

session.add(engineer)

ktoto = User(
    surname="Can't",
    name="Even",
    age="23",
    position="ktoto",
    speciality="okey",
    address="module_3",
    email="cant_even@mars.org"
)

session.add(ktoto)

ktoto2 = User(
    surname="Msushi",
    name="SpeedRuner",
    age="22",
    position="ktoto2",
    speciality="okeey",
    address="module_4",
    email="cant_even@mars.org"
)

session.add(ktoto2)
session.commit()