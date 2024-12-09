SELECT "city", COUNT("name") AS "number_of_schools" FROM "schools"
WHERE "TYPE" = 'Public School'
GROUP BY "city" ORDER BY "number_of_schools" DESC, "name" ASC
LIMIT 10;
