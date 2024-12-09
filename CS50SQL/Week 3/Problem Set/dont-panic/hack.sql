-- Update the password for the admin account
UPDATE "users" 
SET "password" = '982c0381c279d139fd221fce974916e7'
WHERE "username" = 'admin';

-- Delete the log from db
DELETE FROM "user_logs"
WHERE "old_username" = 'admin'
AND "new_password" = '982c0381c279d139fd221fce974916e7';

-- Insert the fabricated logs to show that someone else changed the logs
INSERT INTO "user_logs" ("type", "old_username", "new_username", "old_password", "new_password")
SELECT 'update', 'admin', 'emily33', NULL,(
--    SELECT "password" FROM "users"
--    WHERE "username" = 'admin'
--)
    SELECT "password" from "users"
    WHERE "username" = 'emily33'
);

