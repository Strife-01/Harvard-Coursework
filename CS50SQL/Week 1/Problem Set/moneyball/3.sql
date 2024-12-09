SELECT "performances"."year", "performances"."HR"
FROM "performances"
WHERE "performances"."player_id" IN (
    SELECT "players"."id"
    FROM "players"
    WHERE "players"."first_name" = 'Ken'
    AND "players"."last_name" = 'Griffey'
    AND "players"."birth_year" = 1969
)
ORDER BY "performances"."year" DESC;
