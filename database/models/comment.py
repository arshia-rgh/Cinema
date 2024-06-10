from database.base import Base
from sqlalchemy import (Column,Integer,ForeignKey,Text)
from sqlalchemy.orm import relationship

class Comment(Base):
    """
    subclasses Base class
    each object represents a row in comments table
    Columns:
        - id (PK)
        - user_id (FK to User) 
            - manager and customer both can comment on a movie
        - movie_id (FK to Movie)
        - parent_id (FK to Comment) :
            - Comment.id if its a reply to a comment
            - None if its directly written for a movie
        - text type(Text)
    relationships:
        - movie (one-to-many)
        - user (one-to-many)
        - parent (one-to-many)
    """

    __tablename__ = 'comments'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    movie_id = Column("movie_id", Integer, ForeignKey("movies.id"), ondelete='CASCADE')
    user_id = Column("user_id", Integer, ForeignKey("users.id"), ondelete='CASCADE')
    parent_id = Column("name", Integer, ForeignKey('comments.id') ,default=None, ondelete='CASCADE')
    text = Column("text", Text, default=None)

    movie = relationship("Movie", back_populates="comments")
    user = relationship("User", back_populates="comments")
    parent = relationship("Comment", back_populates="comments")

    def __repr__(self): 
        return f"<Comment(User= '{self.user_id}', movie= '{self.movie_id}', parent_comment=
        '{self.parent_id}', text= '{self.text}'>"
    