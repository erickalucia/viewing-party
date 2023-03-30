# ------------- WAVE 1 --------------------
#---Wave_1_function_1---
def create_movie(title, genre, rating):
# take three parameters: title, genre, rating
# If those three attributes are truthy, then return a dictionary. This dictionary should...
# Have three key-value pairs, with specific keys
# The three keys should be "title", "genre", and "rating"
# The values of these key-value pairs should be appropriate values
# If title is falsy, genre is falsy, or rating is falsy, this function should return None

# create empty dictionary
    movie_dict = {}
# if any arguments are falsy, return None
    if not title:
        return None
    elif not genre:
        return None
    elif not rating:
        return None
# else: add arguments to empty dictionary with key value pairs
    else: 
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating

# return the dictionary
    return movie_dict

create_movie("Title", "Genre", "Rating")


# #---Wave_1_function_2---
def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data
# #  we need to add movie to the list that is the value dictionary user_data 
#     return (user_data)

add_to_watched({"watched": []}, {
        "title": "MOVIE_TITLE_1",
        "genre": "GENRE_1",
        "rating": "RATING_1"})


# #---Wave_1_function_3---
def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)
    return user_data

# janes_data = {
#             "watchlist": [{
#                 "title": "MOVIE_TITLE_1",
#                 "genre": "GENRE_1",
#                 "rating": "RATING_1"
#             }],
#             "watched": []
#         }
# print (janes_data["watchlist"][0]["title"])


#---Wave_1_function_4---
def watch_movie(user_data, title):

    # if title not in user_data["watchlist"]["title"]:
    #     return user_data
    for movie in user_data["watchlist"]:
        if title != (movie["title"]):
            return user_data
        elif title in (movie["title"]):
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            print (user_data)
            return user_data


# ------------- WAVE 2 --------------------
# ---Wave_2_function_1---

janes_data = {
            "watchlist": [{
                "title": "mean girls",
                "genre": "comedy",
                "rating": 10
            }, {
                "title": "iron man",
                "genre": "action",
                "rating": 6
            }],
            "watched": [{"title": "black panther",
                "genre": "action",
                "rating": 9},{"title": "john tucker must die",
                "genre": "comedy",
                "rating": 5}, {"title": "john wick",
                "genre": "action",
                "rating": 9}, {"title": "spider man",
                "genre": "action",
                "rating": 8}]
        }
title = "iron man"


def get_watched_avg_rating(user_data):
# - navigate to janes_data rating (watchlist -> dictionaries, rating)
# - new list of ratings
# - find function to calculate average get_watched_avg_rating
# - return 0.0 for empty list


    ratings = []
    
    if len(user_data["watched"]) == 0:
        return 0.0
    
    for movie in user_data["watched"]:
        ratings.append((movie["rating"]))
    
    ratings_sum = sum(ratings)
    ratings_average = (ratings_sum) / len(ratings)

    return ratings_average


        

# ---Wave_2_function_2---
def get_most_watched_genre(user_data):

    movie_genre_dict = {}

    if len(user_data["watched"]) == 0:
        return None
    
    for movie in user_data["watched"]:
        
        # movie_genre_dict[(movie["genre"])].update(movie)
        title = movie["title"]
        genre = movie["genre"]
        if genre not in movie_genre_dict:
            movie_genre_dict[genre] = []
        movie_genre_dict[genre].append(title)
   
        # append new value to existing key 
    print(movie_genre_dict)

    # figure out max count
    max_genre = None
    max_count = 0

    

    return max(movie_genre_dict)

# movie_genre_dict.update({(movie["genre"]): movie})


print (get_most_watched_genre(janes_data))




# ------------- WAVE 3 --------------------

#---Wave_3_function_1---
# def get_unique_watched(user_data):

#---Wave_3_function_2---
# def get_friends_unique_watched(user_data):

# ------------- WAVE 4 --------------------
#---Wave_4_function_1---
# def get_available_recs(user_data):


# ------------- WAVE 5 --------------------
# ---Wave_5_function_1---
# def get_new_rec_by_genre(user_data):

# ---Wave_5_function_2---
# def get_rec_from_favorites(user_data):


