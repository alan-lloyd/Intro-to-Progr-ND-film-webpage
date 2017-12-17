import webbrowser

class Movie():

#constructor for object instances of class Movie
 def __init__(self, movie_title, movie_storyline, release_date, poster_image, trailer_youtube):

        self.title=movie_title
        self.storyline=movie_storyline
        self.releasedate=release_date
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
