CREATE VIEW "total" AS
SELECT "locality", SUM("families") AS "families",
SUM("households") AS "households",
SUM("population") AS "population",
SUM("male") AS "males",
SUM("female") AS "females"
FROM "census"
GROUP BY "locality";
