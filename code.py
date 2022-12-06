import requests,webbrowser

from tkinter import *
struct=Tk()
struct.geometry("600x400") #Defining Size of GUI box
struct.title("Youtube Search Classifier")
label=Label(struct,text="Youtube Search Classifier",bg="grey",fg="white",font=("Times",20,"bold"))
label.pack(side=TOP)
struct.config(background="grey")
text=StringVar()
def search():
    pass
label=Label(struct,text="Enter here to search",bg="grey",fg="white",font=("Times",15,"bold"))
label.place(x=50,y=100)
enter=Entry(struct,font=("Times",10,"bold"),textvar=text,width=30,bd=2,bg="white")
enter.place(x=50,y=130)
button=Button(struct,text="Search",font=("Times",10,"bold"),width=30,bd=2,command=search)
button.place(x=50,y=170)
struct.mainloop()
