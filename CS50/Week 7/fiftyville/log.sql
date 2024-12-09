-- Keep a log of any SQL queries you execute as you solve the mystery.

.schema
SELECT * FROM crime_scene_reports WHERE day = 28 AND month = 7 AND street = 'Humphrey Street';
.schema airports
SELECT * FROM airports;
.schema flights
SELECT * FROM flights JOIN airports ON flights.origin_airport_id = airports.id WHERE month = 7 and day = 29 and city = 'Fiftyville' ORDER BY hour ASC;
SELECT destination_airport_id FROM flights JOIN airports ON flights.origin_airport_id = airports.id WHERE month = 7 and day = 29 and city = 'Fiftyville' ORDER BY hour ASC;
.schema phone_calls 
select caller, receiver, duration from phone_calls WHERE day = 28 and month = 7 and duration <= 60 ORDER BY id;
.schema atm_transactions 
select * from atm_transactions WHERE day = 28 AND  month = 7 and atm_location = 'Leggett Street' order by id;
.schema bank_accounts 
.schema people
.schema bakery_security_logs 
SELECT * from bakery_security_logs where day = 28 and month = 7 and hour = 10 and minute >= 14 and minute <= 26;
SELECT name, account_number FROM people join bank_accounts on people.id = bank_accounts.person_id where account_number IN (28500762, 28296815, 76054385, 49610011, 16153065);
SELECT name, phone_number from people where name in ('Luca', 'Kenny', 'Taylor', 'Bruce', 'Brooke');
SELECT name, phone_number from people where  phone_number = '(375) 555-8161';
.schema passengers 
.schema people 
select passport_number from people where name = 'Bruce';
SELECT flight_id from passengers WHERE passport_number = 5773159633;
.schema flights
SELECT destination_airport_id from flights WHERE id = 36;