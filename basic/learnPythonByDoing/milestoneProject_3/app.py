"""
- Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:
    
- Add movies
- See movies
- Find a movie
- stop running the program

Task:
    []: Decide where to store movies
    []: What is the format of a movie?
    []: Show the user the main interface and get their input
    []: Allow users to add movies
    []: Show all their movies
    []: Find a movie
    []: Stop running the program when they type 'q'
    
    
"""



movies = []
"""
our movie can be store as dictionary
movie = {
        'name' : ........(str),
        'director' : ....(str),
        'year' : .......(int)
}
"""





def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")
    
    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        
        elif user_input == 'l':
            show_movie()
            
        elif user_input == 'f':
            find_movie()
            
        else:
            print("unknown command....try again.........")
            
        user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")



def add_movie():
    name = input('Enter the movie\'s name: ')
    director = input('Enter the movie\'s director: ')
    year = input("Enter the movie's release year: ")
    
    # constract movies value with needed key
    movies.append({
            'name': name,
            'director': director,
            'year': year
            })
    

def show_movie():
    for movie in movies:
        show_movies_details(movie)
    
def show_movies_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Realeas Year: {movie['year']}")
    print(f'\n')
    
    
    
    

def find_movie():
    find_by = input("What property of the movie are you looking for? write any of 3 \n name or director or year: ") # one of 'year','name','director'
    looking_for = input("what are you searching for? ")
    
    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])
    
    show_movie(found_movies)

def find_by_attribute(items, expected, finder):
    found = []
    
    for i in items:
        if finder(i) == expected:
            found.append(i)
            
    return found

menu()

#print(movies)

