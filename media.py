import webbrowser
#Array that will be used with open_movies_page function called in entertainment_center.py
movie_list = []

class Movie():
    """This class provides a way to store movie related information"""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    #Class constructor
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        #Add Movie instance to movies array
        movie_list.append(self)        
    
