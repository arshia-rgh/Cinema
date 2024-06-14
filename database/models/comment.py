from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from database.base import Base


class Comment(Base):
    """
    A Comment entity representing a comment in the database.
    - Attributes:
        - id (int): The unique identifier of the comment.
        - user_id (int): FK(User.id) user of the comment.
        - movie_id (int): FK(Movie.id) movie of the comment.
        - parent_id (int): FK(Comment.id) the comment which this comment is repiled to.
        - text (Text): the text of the comment.
    - Relationships:
        - movie: the Movie which the comment belongs to
        - user: the User which the comment belongs to
        - parent: the parent Comment
    """

    __tablename__ = 'comments'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    movie_id = Column("movie_id", Integer, ForeignKey("movies.id", ondelete='CASCADE'))
    user_id = Column("user_id", Integer, ForeignKey("users.id", ondelete='CASCADE'))
    parent_id = Column("parent_id", Integer, ForeignKey('comments.id', ondelete='CASCADE'), default=None)
    text = Column("text", Text, default=None)

    movie = relationship("Movie", back_populates="comments")
    user = relationship("User", back_populates="comments")
    parent = relationship("Comment", backref="children", remote_side=[id])

    def __repr__(self):
        return f"<Comment(User= '{self.user_id}', movie= '{self.movie_id}', parent_comment='{self.parent_id}', text= '{self.text}'>"
