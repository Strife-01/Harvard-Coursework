SELECT "schools"."name", "expenditures"."per_pupil_expenditure", "graduation_rates"."graduated"
FROM "graduation_rates" INNER JOIN "schools"
ON "graduation_rates"."school_id" = "schools"."id"
INNER JOIN "districts" ON "districts"."id" = "schools"."district_id"
INNER JOIN "expenditures" ON "expenditures"."district_id" = "districts"."id"
ORDER BY "expenditures"."per_pupil_expenditure" DESC, "schools"."name" ASC;
