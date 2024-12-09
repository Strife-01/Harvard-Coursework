SELECT title, air_date FROM episodes WHERE strftime('%m', air_date) = '12';
