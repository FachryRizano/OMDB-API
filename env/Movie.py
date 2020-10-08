class Movie:
    def __init__(self, title, year, imdbID, type, poster):
        self.__title = title
        self.__year = year
        self.__imdbID = imdbID
        self.__type = type
        self.__poster = poster

    def get__title(self):
        return self.__title
    
    def get__year(self):
        return self.__year
    
    def get__imdbID(self):
        return self.__year

    def get__type(self):
        return self.__type

    def get__poster(self):
        return self.__poster
    
    def set__title(self,title):
        self.__title = title
    
    def set__year(self,year):
        self.__year = year

    def set__imdbID(self,imdbID):
        self.__imdbID = imdbID

    def set__type(self,type):
        self.__type = type
        
    def set__poster(self,poster):
        self.__poster = poster
    