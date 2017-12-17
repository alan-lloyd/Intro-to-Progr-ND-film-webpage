import fresh_tomatoes
import media

#declaration and initialisation of 9 instances of class Movie
terminator_1 = media.Movie("Terminator","Brilliantly original sci-fi night-chase movie", "1984", "https://images-na.ssl-images-amazon.com/images/M/MV5BNjg3MTIwNTI0OV5BMl5BanBnXkFtZTYwODk4NDc5._V1_.jpg","https://www.youtube.com/watch?v=x_-JB8Uut6c")

terminator_2 = media.Movie("Terminator 2","Sequel many say is better than its awesome original", "1991", "https://upload.wikimedia.org/wikipedia/en/8/85/Terminator2poster.jpg","https://www.youtube.com/watch?v=-W8CegO_Ixw")

alien = media.Movie("Alien","a very original classic sci-fi film", "1979", "https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg","https://www.youtube.com/watch?v=LjLamj-b0I8")

aliens = media.Movie("Aliens","The Corporation & The Aliens vs. Ripley & The Marines",  "1986", "https://upload.wikimedia.org/wikipedia/en/f/fb/Aliens_poster.jpg","https://www.youtube.com/watch?v=XKSQmYUaIyE")

forbin_project = media.Movie("The Forbin Project","computer takes over world..", "1970", "https://upload.wikimedia.org/wikipedia/en/c/c4/Colossus_the_forbin_project_movie_poster.jpg","https://www.youtube.com/watch?v=cG7ij1Ft6lw")

the_matrix = media.Movie("The Matrix","people, software, machines fight for survival", "1999", "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg","https://www.youtube.com/watch?v=tGgCqGm_6Hs")

solaris = media.Movie("Solaris","Mystery on planet Solaris", "1972", "https://upload.wikimedia.org/wikipedia/en/5/54/Solyaris_ussr_poster.jpg","https://www.youtube.com/watch?v=HEOfJQX2qdQ")

ex_machina = media.Movie("Ex-Machina","an AI with a body wants freedom..", "2015", "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg","https://www.youtube.com/watch?v=gwFg8ilABps")

day_the_world_stood_still = media.Movie("Day the world stood still","Aliens come to clean the earth", "2008", "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Day_the_Earth_Stood_Still.jpg","https://www.youtube.com/watch?v=6QFcZohER3s")



#list used by open_movies_page() to load up dynamically film web page and contents
movies=[terminator_1, terminator_2, alien, aliens, forbin_project, the_matrix, solaris, ex_machina, day_the_world_stood_still]


#main calling method
fresh_tomatoes.open_movies_page(movies)  


 

