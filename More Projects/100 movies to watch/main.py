import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
    )
text = response.text

soup = BeautifulSoup(text, "html.parser")
movie_titles = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]

movies = []
for el in reversed(movie_titles):
    movies.append(el)

print(*movies, sep="\n")