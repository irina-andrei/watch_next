# A program that will tell you what to watch next based on the word vector 
# similarity of the description of movies.


import spacy
nlp = spacy.load('en_core_web_md')

#=====Formatting Options=====
GREEN = '\033[92m'
BLUE = '\033[94m'
PINK = '\033[95m'
CYAN = '\033[96m'
RED = '\033[31m'
ENDC = '\033[0m' # Removes all formatting applied.

movie_dict = {}
# A dictionary that will save the movie title as the key and the values will
# be the descriptions of each movie.


def watch_next(description):
    """ Function goes through the movie dictionary and finds the movie with
    the highest similarity based on the movie description. 
    Parameters: description (str)
    Returns: found_movie (str) """
    
    highest = 0
    # The variable will save the highest occurence of similarity. 
    
    model_sentence = nlp(description)
    # Parsing the text.
    
    for movie_name, movie_desc in movie_dict.items():
        similarity = nlp(movie_desc).similarity(model_sentence)
        
        print(f"\n{PINK}{movie_name}{ENDC}\n{CYAN}{movie_desc}{ENDC}")
        print(f"Similarity: {GREEN}{similarity}{ENDC}")
        
        if highest < similarity:
            highest = similarity
            found_movie = movie_name
    # The for loop goes though the dictionary and finds the similarity between
    # the description of the movie and the rest of the movie descriptions,
    # saving the one with the highest similarity.
    
    return found_movie


# Accessing the movie list file.
with open('movies.txt', 'r', encoding='utf-8') as movies_list:
    for line in movies_list:
        line_data = line.strip().split(" :")
        movie_dict[line_data[0]] = line_data[1]
        # Saving each movie and its description in our dictionary.

movie_name = "Planet Hulk"
movie_description = """Will he save their world or destroy it? When the Hulk 
becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle 
and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery 
and trained as a gladiator."""
# The preset movie information to compare to.

most_similar = watch_next(movie_description)
# Calling the function that will return the movie with the highest similarity.

print(f"{RED}\n{'═'*80}{ENDC}")
print(f"After watching {BLUE}'{movie_name}'{ENDC}, the closest movie is",
    f"{PINK}'{most_similar}'{ENDC}.")
print(f"{GREEN}Description:{ENDC} {movie_dict[most_similar]}")
print(f"{RED}{'═'*80}{ENDC}")