import requests,webbrowser
import json
import csv
from bs4 import BeautifulSoup
import re
import pandas as pd

import PyMovieDb
from PyMovieDb import IMDB
from tkinter import *




def search():
    pass

struct=Tk()
struct.geometry("600x400") #Defining Size of GUI box
struct.title("Youtube Search Classifier")
label=Label(struct,text="Youtube Search Classifier",bg="grey",fg="white",font=("Times",20,"bold"))
label.pack(side=TOP)
struct.config(background="grey")
text=StringVar()



label=Label(struct,text="Enter here to search",bg="grey",fg="white",font=("Times",15,"bold"))
label.place(x=50,y=100)
#inputing values
enter=Entry(struct,font=("Times",10,"bold"),textvar=text,width=30,bd=2,bg="white")
enter.place(x=50,y=130)

#submit button
button=Button(struct,text="Search",font=("Times",10,"bold"),width=30,bd=2, command=search)
button.place(x=50,y=170)
print("Submitted")
struct.mainloop()


# def Youtube():
#
#
#     # Downloading imdb top 250 movie's data
#     url = 'http://www.imdb.com/chart/top'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     movies = soup.select('td.titleColumn')
#     crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
#     ratings = [b.attrs.get('data-value')
#                for b in soup.select('td.posterColumn span[name=ir]')]
#
#     # create a empty list for storing
#     # movie information
#     list = []
#
#     # Iterating over movies to extract
#     # each movie's details
#     for index in range(0, len(movies)):
#         # Separating movie into: 'place',
#         # 'title', 'year'
#         movie_string = movies[index].ent
#         movie = (' '.join(movie_string.split()).replace('.', ''))
#         movie_title = movie[len(str(index)) + 1:-7]
#         year = re.search('\((.*?)\)', movie_string).group(1)
#         place = movie[:len(str(index)) - (len(movie))]
#         data = {"place": place,
#                 "movie_title": movie_title,
#                 "rating": ratings[index],
#                 "year": year,
#                 "star_cast": crew[index],
#                 }
#         list.append(data)
#
#     # printing movie details with its rating.
#     for movie in list:
#         print(movie['place'], '-', movie['movie_title'], '(' + movie['year'] +
#               ') -', 'Starring:', movie['star_cast'], movie['rating'])
#
#     ##.......##
#     df = pd.DataFrame(list)
#     df.to_csv('movies.csv', index=False)
#
#     # imdb = IMDB()
#     # # getting user input
#     # var  = "House Of The Dragon", ""
#     # movie = imdb.get_by_name()
#     #
#     # # convert into a dictionary
#     # result = json.loads(movie)
#     # name = result["name"]
#     # genre = result["genre"]
#     # print(name)
#     # print(genre)
#










