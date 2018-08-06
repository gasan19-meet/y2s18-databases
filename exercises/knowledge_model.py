from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__='info'
	student_id = Column(Integer, primary_key=True)
	fav_nickname = Column(String)
	fav_prehistoric_animal = Column(String)
	glove_size = Column(Integer)
	rating = Column(Integer)
	def __repr__(self):
		return ("students id: {}\n"
				"students favorite nikname: {}\n"
				"students favoite prehistoric animal: {}\n"
				"ideal glove size: {}\n"
				"rating:{}").format(
				self.student_id,self.fav_nickname,self.fav_prehistoric_animal,
				self.glove_size,self.rating)

	# Create a table with 4 columns
	# Thes first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

	pass