CREATE TABLE IF NOT EXISTS "passengers" (
  "id" INTEGER,
  "first_name" TEXT NOT NULL,
  "last_name" TEXT NOT NULL,
  "age" INTEGER NOT NULL CHECK("age" >= 0),
  PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "check-ins" (
  "id" INTEGER,
  "passenger_id" INTEGER,
  "flight_id" INTEGER,
  "checkin_time" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY("id"),
  FOREIGN KEY("passenger_id") REFERENCES "passengers"("id"),
  FOREIGN KEY("flight_id") REFERENCES "flights"("id")
);

CREATE TABLE IF NOT EXISTS "airlines" (
  "id" INTEGER,
  "name" TEXT NOT NULL,
  "concourse" TEXT NOT NULL CHECK("concourse" REGEXP '^[ABCDEFT]+$'),
  PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "flights" (
  "id" INTEGER,
  "airline_id" INTEGER,
  "flight_number" INTEGER NOT NULL,
  "from_airport_code" TEXT NOT NULL,
  "to_airport_code" TEXT NOT NULL,
  "departure_at" DATETIME NOT NULL,
  "arrival_at" DATETIME NOT NULL,
  PRIMARY KEY("id"),
  FOREIGN KEY("airline_id") REFERENCES "airlines"("id")
);

