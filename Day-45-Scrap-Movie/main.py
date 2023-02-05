import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

movie_tags = soup.find_all(name="h3", class_="title")
movies = [movie.getText() for movie in movie_tags]
movies.reverse()

with open("movies.txt", 'w') as file:
    for movie in movies:
        file.write(f"{movie}\n")
        
# Print a random movie from top 100 movie list:
with open("movies.txt") as file:
    movies = file.readlines()

movie_titles = [movie.strip() for movie in movies]

print(random.choice(movie_titles))

