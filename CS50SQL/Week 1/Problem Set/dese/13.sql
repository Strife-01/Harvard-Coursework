SELECT "districts"."city", 
AVG("graduation_rates"."graduated") AS "Graduated per district",
AVG("graduation_rates"."dropped") AS "Dropted out per district",
AVG("graduation_rates"."excluded") AS "Expelled per district"
FROM "graduation_rates" INNER JOIN "schools"
ON "graduation_rates"."school_id" = "schools"."id"
INNER JOIN "districts"
ON "schools"."district_id" = "districts"."id"
GROUP BY "districts"."city"
ORDER BY "graduation_rates"."graduated" DESC,
"graduation_rates"."dropped" ASC,
"graduation_rates"."excluded" ASC;
