SELECT "salaries"."year", ROUND(AVG("salaries"."salary"), 2) AS "average salary"
FROM "salaries"
GROUP BY "salaries"."year"
ORDER BY "salaries"."year" DESC;
