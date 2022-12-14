
import json
import csv
# from beautifulsoup4 import BeautifulSoup
# import re
# import pandas as pd

#from movie import  *
from tkinter import *
from video import SearchMovie




def search():


      struct=Tk()
      struct.geometry("600x400") #Defining Size of GUI box
      struct.title("Youtube Search Classifier")
      label=Label(struct,text="Youtube Search Classifier",bg="grey",fg="white",font=("Times",20,"bold"))
      label.pack(side=TOP)
      struct.config(background="grey")
      text=StringVar()

      c = Canvas(struct, bg="White",  width="500")
      c.place(x=80, y=130)
      c.pack()




      label=Label(struct,text="Enter here to search",bg="grey",fg="white",font=("Times",15,"bold"))
      label.place(x=50,y=100)
      #inputing values
      enterInput=Entry(struct,font=("Times",10,"bold"),textvar=text,width=30,bd=2,bg="white")
      enterInput.place(x=50,y=130)
      #submit button
      enterButton=Button(struct,text="Search",font=("Times",10,"bold"),width=30,bd=2, command=get_text())
      enterButton.place(x=50,y=170)


      struct.mainloop()
search()


def get_text():
      searchKeyword = enterInput.get()
      search()

# def search ():
#
# def display_text():
#    global entry
#    SearchMovie()
#    string= entry.get(x)
#    label.configure(text=string)





def enter_details():
      Enter



