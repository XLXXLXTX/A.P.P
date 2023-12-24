# Advanced Python Programming - FP Project | Author: Javier Pardos | javier.pardos10@e-uvt.ro

"""
Assigment 3 - Create a program that manages a list of movies and implement the following functionality:

1. A movie is defined by a title and a rank (like the one defined in imdb.com)
2. Create the possibility to add a movie in the list of movies
3. Create the possibility to display all the movies existing at a certain moment in time
4. Implement the possibility to search the movies for a specific movie
5. Create the possibility of removing of a certain movie from the movies list

"""

from typing import List, Tuple

def addMovie(movies: List[ Tuple[str, float] ]) -> List[ Tuple[str, float] ]:
    
    """ Pure function () - Adds a movie to the list of movies """

    title = input(f'\tEnter the title of the movie: ')
    rank = float(input(f'\tEnter the rank of the movie: '))

    # return original list + new movie
    return movies + [(title, rank)]

def displayMovies(movies :List[ Tuple[str, float] ]) -> None:
    
    """ Pure function () - Displays all the movies existing at a certain moment in time """

    for title, rank in movies:
        print(f'\tTittle: {title} - Ranking: {rank}')

def findMovie(movies :List[ Tuple[str, float] ]) -> None:

    """ Pure function () - Search the movies for a specific movie """

    title = input('\tEnter the title of the movie: ')
    
    # 'filter()' iterates over the list of movies and applies 
    #            the lambda function to each element
    #
    # lambda function to check if title given is the same from any movie 
    movie = list( filter(lambda m: m[0] == title, movies) )

    # print the movie (tittle and rank) if exists,
    if movie: print(f'\t{movie[0][0]} -  {movie[0][1]}')
    # else print error msg
    else: print(f'\tMovie not found')

def removeMovie(movies :List[ Tuple[str, float] ]) -> List[ Tuple[str, float] ]:
    
    """ Removes a movie from the list of movies """
    
    title = input(f'\tEnter the title of the movie: ')
    
    # 'filter()' iterates over the list of movies and applies the filter 
    #            function to each element 
    #
    # lambda function to check if title given is not is the same from any movie
    return list( filter(lambda m: m[0] != title, movies) )

def exit_loop():
    exit(0)

def error_handler():
    print("This operation does not exist ...")

def main():

    # create an empty dict for the movies: tittle -> rating 
    movies = []

    menuList = [
        '1. Add a movie',
        '2. Display all movies',
        '3. Search for a movie',
        '4. Remove a movie',
        '5. Exit'
    ]

    operations = { 1 : addMovie, 2 : displayMovies, 
                   3 : findMovie, 4 : removeMovie,
                   5 : exit_loop}

    #Header 
    print(f'\n{"*" * 50}\n')

    while True:
        
        for menu in menuList:
            print(menu)
        
        print(f'\n{"*" * 50}\n')
        
        op = int( input("\nEnter your operation:") )
        func = operations.get(op, error_handler)
        
        # exit option was chosen
        if op == 5:
            func()

        # execute the function and save the result in a variable
        updated_list = func(movies)

        # if variable is not None, then the list of movies need to be updated
        if updated_list is not None:
            movies = updated_list
        
        print(f'\n{"*" * 50}\n')
        #Clear de console
        

if __name__ == '__main__':
    main()