SELECT DISTINCT "teams"."name"
FROM "teams" INNER JOIN "performances"
ON "teams"."id" = "performances"."team_id"
INNER JOIN "players"
ON "performances"."player_id" = "players"."id"
WHERE "players"."first_name" = 'Satchel'
AND "players"."last_name" = 'Paige';
