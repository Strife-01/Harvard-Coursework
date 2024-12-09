SELECT "salaries"."year", "salaries"."salary"
FROM "salaries"
WHERE "salaries"."player_id" IN (
    SELECT "players"."id"
    FROM "players"
    WHERE "players"."first_name" = 'Cal'
    AND "players"."last_name" = 'Ripken'
)
ORDER BY "salaries"."year" DESC;
