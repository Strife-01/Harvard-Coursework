SELECT "teams"."name", ROUND(AVG("salaries"."salary"), 2) AS "average salary"
FROM "teams" INNER JOIN "salaries"
ON "teams"."id" = "salaries"."team_id"
INNER JOIN "players"
ON "players"."id" = "salaries"."player_id"
GROUP BY "teams"."name"
ORDER BY "average salary" ASC
LIMIT 5;
