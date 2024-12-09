SELECT "districts"."name", "expenditures"."per_pupil_expenditure", "staff_evaluations"."exemplary"
FROM "expenditures" INNER JOIN "districts" ON "districts"."id" = "expenditures"."district_id"
INNER JOIN "staff_evaluations" ON "districts"."id" = "staff_evaluations"."district_id"
WHERE "districts"."state" = 'MA' AND "expenditures"."per_pupil_expenditure" > (
    SELECT AVG("per_pupil_expenditure") FROM "expenditures"
    WHERE "expenditures"."district_id" IN (
        SELECT "districts"."id" FROM "districts"
        WHERE "districts"."state" = 'MA'
    )
) AND "staff_evaluations"."exemplary" > (
    SELECT AVG("staff_evaluations"."exemplary") FROM "staff_evaluations"
    WHERE "staff_evaluations"."district_id" IN (
        SELECT "districts"."id" FROM "districts"
        WHERE "districts"."state" = 'MA'
    )
)
ORDER BY "staff_evaluations"."exemplary" DESC,
"expenditures"."per_pupil_expenditure"
