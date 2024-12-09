SELECT DISTINCT p_n FROM (SELECT people.name AS p_n, movie_id AS mv_1 FROM movies JOIN stars ON movies.id = stars.movie_id JOIN people ON people.id = stars.person_id
) JOIN (SELECT movie_id AS mv_2 FROM movies JOIN stars ON movies.id = stars.movie_id JOIN people ON people.id = stars.person_id WHERE people.name = 'Kevin Bacon'
) ON mv_1 = mv_2;
