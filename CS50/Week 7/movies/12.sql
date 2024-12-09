SELECT mv_title_1 FROM (SELECT title AS mv_title_1, movie_id AS mv_1 FROM movies JOIN stars ON movies.id = stars.movie_id JOIN people ON people.id = stars.person_id WHERE people.name = 'Jennifer Lawrence'
) JOIN (SELECT title AS mv_title_2, movie_id AS mv_2 FROM movies JOIN stars ON movies.id = stars.movie_id JOIN people ON people.id = stars.person_id WHERE people.name = 'Bradley Cooper'
) ON mv_1 = mv_2;
