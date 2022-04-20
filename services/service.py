from config import CONNECTION_STRING
from data.entities import *

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import CONNECTION_STRING
from data.entities import *

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine(CONNECTION_STRING)

session = Session(bind=engine)

def addUser(chat_id):
    session.add(User(
        chat_id=chat_id,
    ))
    session.commit()

def userExists(chat_id):
    return session.query(User).filter(User.chat_id == chat_id).count() > 0