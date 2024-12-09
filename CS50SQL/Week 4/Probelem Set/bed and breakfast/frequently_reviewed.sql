CREATE VIEW "frequently_reviewed" AS
SELECT "listings"."id" AS "id",
"property_type", "host_name",
COUNT("reviews"."id") AS "reviews"
FROM "listings" INNER JOIN "reviews"
ON "listings"."id" = "reviews"."listing_id"
GROUP BY "listing_id"
ORDER BY "reviews" DESC LIMIT 100;
