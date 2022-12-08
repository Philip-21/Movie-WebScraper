
import requests,webbrowser
import json
import csv
from bs4 import BeautifulSoup
import re
import pandas as pd

import PyMovieDb
from PyMovieDb import IMDB





# Downloading imdb top 250 movie's data
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#gettig the movie and genre
movies = soup.select('td.titleColumn')
genre = soup.find("a", href="search/title?genres")

# create a empty list for storing
# movie information
list = []

# Iterating over movies to extract
# each movie's details
for index in range(0, len(movies)):
    # Separating movie into: 'place',
    movie_string = movies[index].ent
    movie = (' '.join(movie_string.split(",")).replace('.', ''))
    movie_title = movie[len(str(index)) + 1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index)) - (len(movie))]
    data = {"place": place,
            "genre": genre,
            }
    list.append(data)

# printing movie details with its rating.
for movie in list:
    print(movie['place'], '-', movie['movie_title'], '(' + movie['genre'] +
          ') -')

#saving the list as dataframe
#then converting into .csv file
df = pd.DataFrame(list)
df.to_csv('movies.csv', index=False)


# imdb = IMDB()
# #getting user input
# var = "House Of The Dragon"
# movie= imdb.get_by_name(var)
#
# #convert into a dictionary
# result= json.loads(movie)
# name= result["name"]
# genre = result["genre"]
# print(name)
# print(genre)
# #putting inputs in a csv file
#
# with open("movies.csv", "w",newline='')as f :
#       field_names =  ["Movie_Name", "Genre"]
#       writer = csv.DictWriter(file, filednames=field_names)
#
#       writer.writerows()
#
#       for items in  f:
#             value_name = []
#             value_name.append(name)
#             value_name.append(genre)
#
#
#
# # with open("movies.csv", "w")as f :
# #       writer = csv.writer(f)
# #       field_movie= ["Movie Name", "Genre"]
# #       writer.writerows([name])
# #
# #
# #       for items in f:
# #             value_name = []
# #             value_name.append(fieldname["Movie Name"])
# #             value_name.append(fieldname["Genre"])
#
#
#

      




























