SELECT "players"."first_name", "players"."last_name", "salaries"."salary" / "performances"."H" AS "dollars per hit"
FROM "salaries" INNER JOIN "players"
ON "salaries"."player_id" = "players"."id"
INNER JOIN "performances"
ON "performances"."player_id" = "players"."id"
WHERE "performances"."year" = "salaries"."year"
AND "performances"."year" = 2001
AND "performances"."H" > 0
ORDER BY "dollars per hit" ASC,
"players"."first_name" ASC,
"players"."last_name" ASC
LIMIT 10;
