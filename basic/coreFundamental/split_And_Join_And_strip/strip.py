# strip use for removing caracter from string

s = " This String will be stripped\n"
print(len(s))
#remove space characters from the right end
print(s.rstrip())
print(len(s.rstrip()))

#remove space characters from the left end
print(s.lstrip())
print(len(s.lstrip()))


movie = 'This String will be stripped'
# Convert to lowercase and print the result
movie_lower = movie.lower()
print(movie_lower)

# Remove specified character and print the result
movie_no_space = movie_lower.strip("will")
print(movie_no_space)


