SELECT "city", "nr_schools" FROM (
    SELECT "city", COUNT("id") AS "nr_schools" FROM "schools"
    GROUP BY "city"
) WHERE "nr_schools" <= 3
ORDER BY "nr_schools" DESC;
