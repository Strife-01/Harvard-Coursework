SELECT "players"."first_name", "players"."last_name", "salaries"."salary"
FROM "players" INNER JOIN "salaries"
ON "players"."id" = "salaries"."player_id"
WHERE "salaries"."year" = 2001
ORDER BY "salaries"."salary" ASC,
"players"."first_name" ASC,
"players"."last_name" ASC,
"players"."id" ASC
LIMIT 50;
