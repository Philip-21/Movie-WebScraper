
from matplotlib import pyplot as plt

import numpy as np
from tmdbv3api import TMDb, Movie
tmdb = TMDb()
tmdb.api_key = '056e8c6cdd9f7aae4cc11feadce7922c'

# Creating dictionary of movieids and their names
genres = {
    28: 'Action',
    12: 'Adventure',
    16: 'Animation',
    35: 'Comedy',
    80: 'Crime',
    99: 'Documentary',
    18: 'Drama',
    10751: 'Family',
    14: 'Fantasy',
    36: 'History',
    27: 'Horror',
    10402:  'Music',
    9648: 'Mystery',
    10749: 'Romance',
    878: 'Science Fiction',
    10770: 'TV Movie',
    53: 'Thriller',
    10752: 'War',
    37: 'Western',
}


# function to convert list of genre ids to their names
def convert(arr: list):
    newarr = []  # creating an empty array
    for i in arr:  # looping through the array
        if i in genres:  # if an id in the array matches an id in the dictionary,
            i = genres[i]  # change the genre number to the name of the genre
            newarr.append(i)  # add it to the new list
    return (newarr)  # return the new list


# function to count number of times movies have a specific genre name
def counter(arr: list):
    occurence = []  # create an empty array
    # check the number of times each genres appear in the list and add it to the new empty list
    occurence.append(arr.count('Action'))
    occurence.append(arr.count('Adventure'))
    occurence.append(arr.count('Animation'))
    occurence.append(arr.count('Comedy'))
    occurence.append(arr.count('Crime'))
    occurence.append(arr.count('Documentary'))
    occurence.append(arr.count('Drama'))
    occurence.append(arr.count('Family'))
    occurence.append(arr.count('Fantasy'))
    occurence.append(arr.count('History'))
    occurence.append(arr.count('Horror'))
    occurence.append(arr.count('Music'))
    occurence.append(arr.count('Mystery'))
    occurence.append(arr.count('Romance'))
    occurence.append(arr.count('Science Fiction'))
    occurence.append(arr.count('TV Movie'))
    occurence.append(arr.count('Thriller'))
    occurence.append(arr.count('War'))
    occurence.append(arr.count('Western'))
    return occurence  # return the new list with each counts


# a list of all genre names
genreNames = [
    'Action',
    'Adventure',
    'Animation',
    'Comedy',
    'Crime',
    'Documentary',
    'Drama',
    'Family',
    'Fantasy',
    'History',
    'Horror',
    'Music',
    'Mystery',
    'Romance',
    'Science Fiction',
    'TV Movie',
    'Thriller',
    'War',
    'Western',
]


# colors for the piechart
colors = ['yellowgreen', 'red', '#009B77', 'lightskyblue', 'white', 'lightcoral',
          'blue', 'pink', 'darkgreen', 'yellow', 'grey', 'violet', 'magenta', 'cyan', '#F2827F',
          '#D5A372', '#08FF08', 'orange', '#8BD3E6']

# create an instance of Movie pulling from the api
movie = Movie()
# pull popular movies
popular = movie.popular()


# function to get the movie data from the api and add them to a list
def getMovies():
    allGenres = []  # empty list to get the genres ids of each movie

    # loop through data of all popular movies
    for p in popular:
        allGenres.append(p.genre_ids)  # add movie genres to list
    return allGenres  # return a list of genres ids


allGenres = getMovies()

# function to convert genre ids to genre names


def convertIdtoName():
    genre_ids = []  # empty list
    superGenrelist = []  # empty list
    for i in allGenres:  # loop through list of all genre ids gotten from the api
        genre_ids.append(convert(i))  # add the name of the genre id to a list
    for i in genre_ids:  # loop through the list above
        for j in i:  # get each item from the nested list
            superGenrelist.append(j)  # add them to a list
    return superGenrelist  # return the list


# run the counter on the list of genres to get the count of each genres in the list
count = counter(convertIdtoName())


fig = plt.figure(figsize=(10, 7))  # initial figure size for the pie chart
plt.title("GENRES OF CURRENTLY TRENDING MOVIES")  # pie chart title


# initialize a pie chart
patches, texts = plt.pie(count, colors=colors, startangle=90, radius=1.2)

y = np.array(count)  # convert the list of the genres count to a numpy array
x = np.array(genreNames)  # convert the list of genre names to a numpy array
porcent = 100.*y/y.sum()

labels = ['{0} - {1:1.2f} %'.format(i, j) for i, j in zip(x, porcent)]

sort_legend = True
if sort_legend:
    patches, labels, dummy = zip(*sorted(zip(patches, labels, y),
                                         key=lambda x: x[2],
                                         reverse=True))

plt.legend(patches, labels, loc='best', bbox_to_anchor=(-0.1, 1.),
           fontsize=8)  # create sorted legend
# show plot
plt.show()