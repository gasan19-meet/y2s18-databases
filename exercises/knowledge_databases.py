from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_article(fav_nickname,fav_prehistoric_animal,glove_size,rating):
	Knowledge_object=Knowledge(
		fav_nickname= fav_nickname,
		fav_prehistoric_animal = fav_prehistoric_animal,
		glove_size = glove_size,
		rating= rating)
	session.add(Knowledge_object)
	session.commit()


add_article("ben", "T-Rex", 10, 4)

	

def query_all_articles():
	pass

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
