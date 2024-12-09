SELECT "first_name", "last_name" FROM (
SELECT "first_name", "last_name", "id" FROM (
SELECT "first_name", "last_name", "players"."id" AS "id"
FROM "salaries" INNER JOIN "players"
ON "salaries"."player_id" = "players"."id"
INNER JOIN "performances"
ON "performances"."player_id" = "players"."id"
WHERE "performances"."H" > 0-- OR "performances"."RBI" > 0)
AND "performances"."year" = "salaries"."year"
AND "performances"."year" = 2001
ORDER BY
"salaries"."salary" / "performances"."H"
--"salaries"."salary" / (("performances"."H" + "performances"."RBI") / 2),
--"players"."id",
--"players"."last_name",
--"players"."first_name"
LIMIT 10)

-- You can use intersect

INTERSECT

SELECT "first_name", "last_name", "id" FROM (
SELECT "first_name", "last_name", "players"."id" AS "id"
FROM "salaries" INNER JOIN "players"
ON "salaries"."player_id" = "players"."id"
INNER JOIN "performances"
ON "performances"."player_id" = "players"."id"
WHERE "performances"."RBI" > 0-- OR "performances"."RBI" > 0)
AND "performances"."year" = "salaries"."year"
AND "performances"."year" = 2001
ORDER BY
"salaries"."salary" / "performances"."RBI"
LIMIT 10))
ORDER BY "id";
