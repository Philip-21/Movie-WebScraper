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

struct.mainloop()




#
# imdb = IMDB()
# # getting user input
# var  = "House Of The Dragon"
# movie = imdb.get_by_name(var)
#
#
#
# # convert into a dictionary
# result = json.loads(movie)
# # name = result["name"]
# # genre = result["genre"]
# # print(name)
# # print(genre)
#
# for movie in result :
#     print(movie["name"],movie["genre"] )
# df = pd.DataFrame(result)
# df.to_csv('movies.csv', index=False)







