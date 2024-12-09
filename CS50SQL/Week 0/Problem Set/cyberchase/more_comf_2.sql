SELECT strftime('%Y', air_date) AS year, strftime('%m %d', air_date) AS day FROM episodes GROUP BY strftime('%Y', air_date);
