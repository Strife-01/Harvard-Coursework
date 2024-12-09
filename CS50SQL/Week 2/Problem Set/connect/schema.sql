CREATE TABLE IF NOT EXISTS "users" (
  "id" INTEGER,
  "first_name" TEXT NOT NULL,
  "last_name" TEXT NOT NULL,
  "username" TEXT NOT NULL UNIQUE,
  -- The stored passwords are hashed and salted
  -- before they are introduces into the database
  "password" TEXT NOT NULL,
  PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "schools_and_universities" (
  "id" INTEGER,
  "name" TEXT NOT NULL,
  -- Type ex: “Elementary School”, “Middle School”, “High School”, “Lower School”, “Upper School”, “College”, “University”, etc.
  "type" TEXT NOT NULL,
  "location" TEXT NOT NULL,
  "year" INTEGER,
  PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "companies" (
  "id" INTEGER,
  "name" TEXT NOT NULL,
  -- Industrie ex: “Education”, “Technology, “Finance”, etc.
  "industrie" TEXT NOT NULL,
  "location" TEXT NOT NULL,
  PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "people_connections" (
  "person_is_following_id" INTEGER,
  "person_is_followed_id" INTEGER,
  FOREIGN KEY("person_is_following_id") REFERENCES "users"("id"),
  FOREIGN KEY("person_is_followed_id") REFERENCES "users"("id")
);

CREATE TABLE IF NOT EXISTS "schools_connections" (
  "person_id" INTEGER,
  -- This can be any type of school
  "educational_institution_id" INTEGER,
  "start_date" DATE NOT NULL,
  -- DEFAULT NULL means that the person is still studying at the particular institution
  "end_date" DATE DEFAULT NULL,
  -- Ex: “BA”, “MA”, “PhD”, etc.
  "deg_type" TEXT NOT NULL,
  FOREIGN KEY("person_id") REFERENCES "users"("id"),
  FOREIGN KEY("educational_institution_id") REFERENCES "schools_and_universities"("id"),
  PRIMARY KEY("person_id", "educational_institution_id")
);

CREATE TABLE IF NOT EXISTS "companies_connections" (
  "person_id" INTEGER,
  "companie_id" INTEGER,
  "start_affiliation_date" DATE NOT NULL,
  -- DEFAULT NULL means that the person is still affiliated with the company
  "end_affliation_date" DATE DEFAULT NULL,
  "company_position_title" TEXT NOT NULL,
  FOREIGN KEY("person_id") REFERENCES "users"("id"),
  FOREIGN KEY("companie_id") REFERENCES "companies"("id"),
  PRIMARY KEY("person_id", "companie_id")
);
