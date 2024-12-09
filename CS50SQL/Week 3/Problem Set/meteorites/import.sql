-- For debugging
DROP TABLE IF EXISTS "tmp";
DROP TABLE IF EXISTS "meteorites";

-- Crete the table with the data that we need
CREATE TABLE IF NOT EXISTS "meteorites" (
    "id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    "class" TEXT NOT NULL,
    "mass" REAL,
    "discovery" TEXT CHECK("discovery" IN ('Fell', 'Found')),
    "year" INTEGER,
    "lat" REAL,
    "long" REAL,
    PRIMARY KEY("id")
);

-- Create a tmp table
CREATE TABLE IF NOT EXISTS "tmp" (
    "name" TEXT,
    "id" INTEGER,
    "nametype" TEXT,
    "class" TEXT,
    "mass" TEXT,
    "discovery" TEXT,
    "year" INTEGER,
    "lat" TEXT,
    "long" TEXT
);
-- Import the data from the csv file in a temp table
.import --csv --skip 1 meteorites.csv tmp

-- Insert data from temp into the final table
INSERT INTO "meteorites" ("name", "class", "mass", "discovery", "year", "lat", "long")
SELECT "name", "class", 
    iif("mass" != '', ROUND("mass", 2), NULL) AS "mass",
    "discovery",
    iif("year" != '', "year", NULL) AS "year",
    iif("lat" != '', ROUND("lat", 2), NULL) AS "lat",
    iif("long" != '', ROUND("long", 2), NULL) AS "long"
FROM "tmp"
WHERE "nametype" != 'Relict'
ORDER BY "year" ASC, "name" ASC;

-- Drop tmp table
-- DROP TABLE IF EXISTS "tmp";
