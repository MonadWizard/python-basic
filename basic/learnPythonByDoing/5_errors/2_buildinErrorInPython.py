# some Error which are happend by our poor knowledge in python code...
"""
* IndexError    *KeyError   *NameError  *AttributeError     *NotImplementedError
* RuntimeError  *SyntaxError    *IndentationError   *TabError   *TypeError
* ValueError    *ImportError    *DeprecationWarning
"""

"""
# index Error:
friends = ['Rakib','Hasan']
friends[2] # index much than list
"""


# Type Error:
movies = {
        'name' : 'Matrix',
        'director' : 'unknown to me',
        'relese' : '1998'
        }

def show_movie_details(movie):
    print(f'Name: {movie["name"]}')
    print(f'Director: {movie["director"]}')
    print(f'Name: {movie["release"]}')
    
#show_movie_details()    


#key Error happend on dictionarry

movies = {'name':'Matrix','director':'unknown to me'}

def show_movie(movie):
    print(f'Name: {movie["release"]}')

show_movie()










