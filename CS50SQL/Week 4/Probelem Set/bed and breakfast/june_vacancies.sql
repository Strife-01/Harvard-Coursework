CREATE VIEW "june_vacancies" AS
SELECT "listings"."id" AS "id",
"property_type", "host_name",
COUNT("date") AS "days_vacant"
FROM "listings" INNER JOIN "availabilities"
ON "listings"."id" = "availabilities"."listing_id"
WHERE "date" >= '2023-06-01' AND "date" < '2023-07-01' AND "available" = 'TRUE'
GROUP BY "listings"."id";
