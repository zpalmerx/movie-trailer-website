
import media
import fresh_tomatoes
excalibur = media.Movie('Excalibur','One Sword One Land One King','http://upload.wikimedia.org/wikipedia/en/6/60/Excalibur_movie_poster.jpg','http://youtu.be/emF-m9qnF5o')
meaningoflife = media.Movie('Meaning_of_Life','Everything you always wanted to know about life but were afraid to ask','https://upload.wikimedia.org/wikipedia/en/thumb/9/91/Meaningoflife.jpg/220px-Meaningoflife.jpg','https://www.youtube.com/watch?v=LH8aTeouR4Y')
mars_attacks = media.Movie('Mars_Attacks','One Small Step For Martian, One Giant issue for Man','https://upload.wikimedia.org/wikipedia/en/thumb/b/bd/Mars_attacks_ver1.jpg/220px-Mars_attacks_ver1.jpg','https://youtu.be/VYHeZCEFwhI')
ghostbusters = media.Movie('Ghostbusters','Who ya gonna call?','https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/Ghostbusters_cover.png/220px-Ghostbusters_cover.png','https://youtu.be/vntAEVjPBzQ')
movies = [excalibur,meaningoflife,mars_attacks,ghostbusters]
fresh_tomatoes.open_movies_page(movies)

