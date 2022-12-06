# from bs4 import BeautifulSoup as bs
# import html as html 
# import re 
# import requests
# from requests_html import HTMLSession 
import json 
import csv 
 
import PyMovieDb
from PyMovieDb import IMDB
import json
import csv

import PyMovieDb
from PyMovieDb import IMDB

imdb = IMDB()
#getting user input
var = "House Of The Dragon"
movie= imdb.get_by_name(var)

#convert into a dictionary
result= json.loads(movie)
name= result["name"]
genre = result["genre"]
print(name)
print(genre)
#putting inputs in a csv file

with open("movies.csv", "w",newline='')as f :
      field_names =  ["Movie_Name", "Genre"]
      writer = csv.DictWriter(file, filednames=field_names)

      writer.writerows()

      for items in  f:
            value_name = []
            value_name.append(name)
            value_name.append(genre)



# with open("movies.csv", "w")as f :
#       writer = csv.writer(f)
#       field_movie= ["Movie Name", "Genre"]
#       writer.writerows([name])
#
#
#       for items in f:
#             value_name = []
#             value_name.append(fieldname["Movie Name"])
#             value_name.append(fieldname["Genre"])


      

      




























