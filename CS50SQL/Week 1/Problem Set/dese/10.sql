SELECT "name", "per_pupil_expenditure" FROM
"districts" INNER JOIN "expenditures"
ON "districts"."id" = "expenditures"."district_id"
WHERE "districts"."state" = 'MA'
ORDER BY "per_pupil_expenditure" DESC LIMIT 10;
