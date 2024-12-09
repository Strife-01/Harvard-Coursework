SELECT "to_user_id", COUNT("to_user_id") AS "nr_messages" FROM "messages"
WHERE "from_user_id" = (
    SELECT "id" FROM "users"
    WHERE "username" = 'creativewisdom377'
) GROUP BY "to_user_id"
ORDER BY "nr_messages" DESC
LIMIT 3;
