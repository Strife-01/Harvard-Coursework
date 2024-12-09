SELECT movies.title FROM ratings JOIN movies ON movies.id = ratings.movie_id JOIN stars on movies.id = stars.movie_id JOIN people ON stars.person_id = people.id WHERE people.name = 'Chadwick Boseman' ORDER BY ratings.rating DESC LIMIT 5;
