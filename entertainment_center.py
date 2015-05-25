import fresh_tomatoes
import media
import webbrowser

#All movies to be displayed on the webpage are below

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

empire_strikes_back = media.Movie("The Empire Strikes Back",
                                  "Episode V of Original Star Wars Trilogy",
                                  "http://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                                  "https://www.youtube.com/watch?v=0KphGm3_P90")

pitch_perfect = media.Movie("Pitch Perfect",
                             "A college acapella group has success despite differences",
                             "http://upload.wikimedia.org/wikipedia/en/b/b9/Pitch_Perfect_movie_poster.jpg",
                             "https://www.youtube.com/watch?v=axlppY_0l90")

dumb_and_dumber = media.Movie("Dumb and Dumber",
                               "Two stupid friends have a crazy roadtrip",
                               "http://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg",
                               "https://www.youtube.com/watch?v=l13yPhimE3o")

prestige = media.Movie("The Prestige",
                        "Two magicians have a personal and professional competition",
                        "http://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
                        "https://www.youtube.com/watch?v=o4gHCmTQDVI&spfreload=10")

new_hope = media.Movie("A New Hope",
                       "Episode IV of Original Star Wars Trilogy",
                       "http://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                       "https://www.youtube.com/watch?v=1g3_CFmnU7k")

jedi = media.Movie("Return of The Jedi",
                   "Episode VI of Original Star Wars Trilogy",
                   "http://upload.wikimedia.org/wikipedia/en/b/b2/ReturnOfTheJediPoster1983.jpg",
                   "https://www.youtube.com/watch?v=5UfA_aKBGMc")

last_crusade = media.Movie("Indiana Jones and the Last Crusade",
                           "Rockstar Archaeologist/Professor searches for the Holy Grail with his father",
                           "http://upload.wikimedia.org/wikipedia/en/f/fc/Indiana_Jones_and_the_Last_Crusade_A.jpg",
                           "https://www.youtube.com/watch?v=WGpq-LDV6jU")

                        


#Calling the function from fresh_tomatoes that opens the webpage. Array found in media.py
fresh_tomatoes.open_movies_page(media.movie_list)


