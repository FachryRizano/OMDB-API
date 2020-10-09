import json
class Movies:
    def __init__(self, title, year, imdbID, type, poster):
        self.__title = str(title)
        self.__year = str(year)
        self.__imdbID = str(imdbID)
        self.__type = str(type)
        self.__poster = str(poster)

    def getTitle(self):
        return self.__title
    
    def getYear(self):
        return self.__year
    
    def getImdbID(self):
        return self.__imdbID

    def getType(self):
        return self.__type

    def getPoster(self):
        return self.__poster
    
    def setTitle(self,title):
        self.title = title
    
    def setYear(self,year):
        self.year = year

    def setImdbID(self,imdbID):
        self.imdbID = imdbID

    def setType(self,type):
        self.type = type

    def setPoster(self,poster):
        self.poster = poster
    