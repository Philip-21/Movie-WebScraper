import requests,webbrowser
import json
import csv
from csv import writer, DictWriter
from bs4 import BeautifulSoup
import re
import pandas as pd

import PyMovieDb
from PyMovieDb import IMDB


def SearchMovie():


    imdb = IMDB()
    #getting user input
    var = input("Enter Value ")
    movie= imdb.get_by_name(var)

    #convert into a dictionary
    result= json.loads(movie)
    name= result["name"]
    genre = result["genre"]
    #total = [([name]),([genre])]
    print(name)
    print(genre)

    #putting inputs in a csv file

    with open("movies.csv", 'a',newline='') as f_object :
        field_names = ["Movie_Name", "Genre"]

        dict = {"Movie_Name":name, "Genre":genre}
        dictwriter_object = DictWriter(f_object, fieldnames=field_names)

        # Pass the dictionary as an argument to the Writerow()
        dictwriter_object.writerow(dict)

        f_object.close()



        # for items in  f:
        #       value_name = []
        #       value_name.append(name)
        #       value_name.append(genre)
SearchMovie()




      




























