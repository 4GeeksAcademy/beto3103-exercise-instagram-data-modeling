import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
	__tablename__ = "user"
	id = Column(Integer(), primary_key = True)
	username = Column(String(40), nullable = False, unique = True)
	firstname = Column(String(80), nullable = False)
	lastname = Column(String(80), nullable = False)
	email = Column(String(80), nullable = False, unique = True)
#RELATIONSHIP
	follower = relationship ("Follower", uselist = True, backref = "user")
	follow = relationship ("Follower" , uselist = False)
	post = relationship ("Post", uselist = True, backref = "user")
	comment = relationship("Comment", uselist = True, backref = "user")
	

class Follower(Base):
	__tablename__ = "follower"
	id = Column(Integer(), primary_key = True)
#RELATIONSHIP
	idfollow = Column(Integer(), ForeignKey("user.id"))
	idfollower = Column(Integer(), ForeignKey("user.id"))


class Media(Base):
	__tablename__ = "media"
	id = Column(Integer(), primary_key = True)
	type = Column(String(80), nullable = False)
	url = Column(String(100), nullable = False, unique = True)
#RELATIONSHIP
	post_id = Column(Integer(), ForeignKey ("post.id"))


class Post(Base):
	__tablename__ = "post"
	id = Column(Integer(), primary_key = True)
#RELATIONSHIP
	user_id = Column(Integer(), ForeignKey("user.id"))
	media = relationship("Media", uselist = True, backref="post")
	comment = relationship("Comment", uselist = True, backref="post")


class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer(), primary_key = True)
    comment_text = Column(Text(), nullable= False)
#RELATIONSHIP   
    author_id = Column(Integer(), ForeignKey("user.id"))
    post_id = Column(Integer(), ForeignKey("post.id"))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
