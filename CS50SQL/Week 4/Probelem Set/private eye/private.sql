-- Create an aggregate TABLE

CREATE TABLE IF NOT EXISTS "triplets" (
    "id_sentence" INTEGER NOT NULL,
    "start_char" INTEGER NOT NULL,
    "nr_char" INTEGER NOT NULL
);

-- Populate the aggregate table

INSERT INTO "triplets" (
    "id_sentence",
    "start_char",
    "nr_char"
) VALUES
    (14, 98, 4),
    (114, 3, 5),
    (618, 72, 9),
    (630, 7, 3),
    (932, 12, 5),
    (2230, 50, 7),
    (2346, 44, 10),
    (3041, 14, 5);

-- Curate the needed propositions

CREATE VIEW IF NOT EXISTS "message" AS
SELECT substr("sentence", "start_char", "nr_char") AS "phrase"
FROM "sentences" INNER JOIN "triplets" ON "sentences"."id" = "triplets"."id_sentence";

