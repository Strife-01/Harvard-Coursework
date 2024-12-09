SELECT "salaries"."salary"
FROM "salaries" INNER JOIN "players"
ON "salaries"."player_id" = "players"."id"
INNER JOIN "performances"
ON "performances"."player_id" = "players"."id"
WHERE "performances"."year" = 2001
ORDER BY "performances"."H" DESC
LIMIT 1;
