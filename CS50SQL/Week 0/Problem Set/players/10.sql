SELECT first_name, last_name FROM players WHERE strftime('%Y', final_game) = '2023' AND first_name LIKE 'A%' ORDER BY first_name , last_name;
