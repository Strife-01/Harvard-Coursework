SELECT "players"."first_name", "players"."last_name",
"salaries"."salary", "performances"."HR",
"performances"."year"
FROM "salaries" INNER JOIN "players"
ON "players"."id" = "salaries"."player_id"
INNER JOIN "performances"
ON "performances"."player_id" = "players"."id"
WHERE "performances"."year" = "salaries"."year"
ORDER BY "players"."id" ASC,
"performances"."year" DESC,
"performances"."H" DESC,
"salaries"."salary" DESC;
