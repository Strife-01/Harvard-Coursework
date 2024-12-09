SELECT "teams"."name", COUNT("performances"."H") AS "total hits"
FROM "players" INNER JOIN "performances"
ON "players"."id" = "performances"."player_id"
INNER JOIN "teams"
ON "performances"."team_id" = "teams"."id"
WHERE "performances"."year" = 2001
GROUP BY "teams"."name"
ORDER BY "total hits" DESC
LIMIT 5;
