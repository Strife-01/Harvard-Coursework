SELECT "districts"."name" FROM
"districts" INNER JOIN "expenditures"
ON "districts"."id" = "expenditures"."district_id"
WHERE "expenditures"."pupils" = (
    SELECT "pupils" FROM "expenditures"
    ORDER BY "pupils" ASC LIMIT 1
);
