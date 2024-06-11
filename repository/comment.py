from typing import Type

from sqlalchemy.orm import Session

from database.base import session
from database.models.comment import Comment
from repository.base import BaseRepository


class CommentRepository(BaseRepository):
    """
        All queries needed on comments are here. methods:
        - get_all           ( returns all comments )
        - get_by_id         ( returns a single comment )
        - get_by_user_id    ( returns a list of all user's comments )
        - get_by_movie_id   ( returns a list of all comments on a movie )
        - get_by_parent_id  ( returns a list of replies to the parent comment )
        - get_parent        ( returns the parent comment)
        - create
        - update
        - delete
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Type[Comment]] | None:
        comments : list[Type[Comment]] = self.db.query(Comment).all()
        return comments

    def get_by_id(self, id: int) -> Type[Comment] | None:
        comment = self.db.query(Comment).filter(Comment.id == id).first()
        if comment:
            return comment
        return None

    def get_by_user_id(self, id: int) -> list[Type[Comment]] | None:
        comments = self.db.query(Comment).filter(Comment.user_id==id).all()
        if comments:
            return comments
        return None
    
    def get_by_movie_id(self, id: int) -> list[Type[Comment]] | None:
        comments = self.db.query(Comment).filter(Comment.movie_id==id).all()
        if comments:
            return comments
        return None
    
    def get_by_parent_id(self, id: int) -> list[Type[Comment]] | None:
        comments = self.db.query(Comment).filter(Comment.parent_id==id).all()
        if comments:
            return comments
        return None
    
    def get_parent(self, id: int) -> Type[Comment] | None:
        parent_comment = self.db.query(Comment).filter(Comment.parent_id==id).first()
        if parent_comment:
            return parent_comment
        return None
            
    def create(self, item: Comment) -> Comment:
        try:
            self.db.add(item)
            self.db.commit()
            self.db.refresh(item)
            return item
        except Exception as e :
            self.db.rollback()
            # TODO: handle exceptions for invalid parameters (movie,user,parent id)
            pass

    def update(self, item: Type[Comment]) -> Type[Comment]:
        Comment = self.db.query(Comment).filter(Comment.id == item.id).first()
        if Comment:
            try:
                Comment = item
                self.db.commit()
                self.db.refresh(Comment)
                return Comment
            except Exception as e:
                self.db.rollback()
                # TODO: handle exceptions for invalid parameters (movie,user,parent id)
                pass

        else:
            # TODO: raise appropriate exception, Not found Comment
            pass

    def delete(self, id: int) -> bool:
        Comment = self.db.query(Comment).filter(Comment.id == id).first()
        if Comment:
            self.db.delete(Comment)
            self.db.commit()
            return True
        return False

Comment_repository = CommentRepository(session)
