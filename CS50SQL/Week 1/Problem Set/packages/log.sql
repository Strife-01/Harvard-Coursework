
-- *** The Lost Letter ***
-- See which names do the drivers have
SELECT name FROM drivers;
-- See how is the letter described in the db
select contents from packages where contents like '%letter%';
-- See how is the action repredented in the db
select action from scans;
-- Get the ids and contents of packages from 900 Somerville Avenue
SELECT "to_address_id" from "packages"
WHERE "from_address_id" = (
    SELECT "id" FROM "addresses"
    WHERE "address" = '900 Somerville Avenue'
) AND "contents" = 'Congratulatory letter';

-- Get the full answer
SELECT "address", "type" from "addresses"
WHERE "addresses"."id" = (
    SELECT "to_address_id" from "packages"
    WHERE "from_address_id" = (
        SELECT "id" FROM "addresses"
        WHERE "address" = '900 Somerville Avenue'
    ) AND "contents" = 'Congratulatory letter'
);

-- *** The Devious Delivery ***
-- Get the contents and the address of the package
SELECT * FROM "packages"
WHERE "from_address_id" IS NULL;
-- get the name of the address where it ended up
SELECT "address" FROM "addresses"
WHERE "id" = 50;

-- *** The Forgotten Gift ***
-- Get the contents of the package
SELECT * FROM "packages"
WHERE "from_address_id" = (
    SELECT "id" FROM "addresses"
    WHERE "address" = '109 Tileston Street'
;
-- Get the person who has it
SELECT "name" FROM "drivers"
WHERE "id" = (
    SELECT "driver_id" FROM "scans"
    WHERE "package_id" = (
        SELECT "id" FROM "packages"
        WHERE "from_address_id" = (
            SELECT "id" FROM "addresses"
            WHERE "address" = '109 Tileston Street'
        )
    )
);
