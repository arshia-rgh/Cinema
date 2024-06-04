#import Users 

class Movie ():
    """
    Movie class 
    Attributes:
        -name
        -ageLimit
        -rate
    Methods:

    """

    def __init__(self, ageLimit= 0, name= "title" ):
        self._name = name
        self._ageLimit = ageLimit
        self._rate = -1
        
    
    #   GETTERs and SETTERs
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        # Verify name
        self._name = name
        
    @property
    def ageLimit(self):
        return self._ageLimit
    
    @ageLimit.setter
    def ageLimit(self,ageLimit:int):
        #   Verify ageLimit
        self._ageLimit = ageLimit
    
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self,rate):
        self._rate = rate
    
class MovieRate():
    """
        Attributes :
            -User
            -Movie
            -Stars = {0,5}
        Functions:
            -update_rate : calculates rate and updates Movie.rate
    """

    def __init__(self, user , movie:Movie , stars):
        self.user = user
        self.movie = movie
        self.stars = stars
        self.update_rate(movie)


    def update_rate(self, movie):
        #self.movie.rate = avg of rates
        pass

class Comment():
    """
        Attributes:
            -ID
            -User
            -Movie
            -Parent : parent Comment ID
            -Text
        Functions:
            - get_comments_by_movie
            - get_comments_by_parent
    """
    
    def __init__(self, user, movie:Movie, text:str ,parent=None):
        self.user = user
        self.movie = movie
        self.text = text
        self.parent = parent
    
    #   GETTERS
    @property
    def user(self):
        return self.user
    @property
    def movie(self):
        return self.movie
    @property
    def text(self):
        return self.text
    @property
    def parent(self):
        return self.parent
    
    def get_comments_by_movie(self) -> list:
        #   show all comments on a movie
        pass
    
    def get_comments_by_parent(self) -> list:
        #   show all subcomments 
        pass

    