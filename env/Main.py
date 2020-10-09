import requests
import json
from Movie import Movies
search = input("Masukkan film yang anda cari:");
parameters = {
    "apikey": "b7286973",
    "s": search
}
response = requests.get("http://www.omdbapi.com/",params = parameters)
response.encoding = 'utf-8'
movies_data = response.json()['Search']
movies = []
i = 0
for i in range(len(movies_data)):
    movie = Movies(
        str(movies_data[i]['Title']),
        str(movies_data[i]['Year']),
        str(movies_data[i]['imdbID']),
        str(movies_data[i]['Type']),
        str(movies_data[i]['Poster'])
    )
    movies.append(movie)

for m in movies:
    print("Title:" + m.getTitle() + " Year:"+ m.getYear() + " imdbID:"+ m.getImdbID() +" Type:"+ m.getType() +" Poster:" + m.getPoster())