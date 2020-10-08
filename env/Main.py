import requests

search = input("Masukkan film yang anda cari:");
parameters = {
    "apikey": "b7286973",
    "s": search
}
response = requests.get("http://www.omdbapi.com/",params = parameters)
data = response.json()['Search']
movie = []
for m in data:
    movieTitle = data["Title"]
    movieYear
    movie.append(movieTitle)