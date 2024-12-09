CREATE TABLE IF NOT EXISTS "ingredients" (
  "id" INTEGER,
  "name" TEXT UNIQUE NOT NULL,
  "price_per_unit" REAL NOT NULL CHECK("price_per_unit" >= 0),
  -- 'pounds', 'grams', etc.
  "unit_type" TEXT NOT NULL,
  PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "donuts" (
  "id" INTEGER,
  "name" TEXT NOT NULL,
  "gluten_free" BOOLEAN NOT NULL,
  "price" REAL NOT NULL CHECK("price" > 0),
  PRIMARY KEY("id")
);

-- A donut contains the following ingredients
CREATE TABLE IF NOT EXISTS "contains" (
  "donut_id" INTEGER,
  "ingredient_id" INTEGER,
  FOREIGN KEY("donut_id") REFERENCES "donuts"("id"),
  FOREIGN KEY("ingredient_id") REFERENCES "ingredients"("id")
);

CREATE TABLE IF NOT EXISTS "customers" (
  "id" INTEGER,
  "first_name" TEXT NOT NULL,
  "last_name" TEXT NOT NULL,
  -- Parse it before entering it into the db '+CODE xxxx-xxx-xxx'
  "phone_number" TEXT NOT NULL,
  PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "orders" (
  "id" INTEGER,
  "order_number" INTEGER NOT NULL,
  "customer_id" INTEGER,
  FOREIGN KEY("customer_id") REFERENCES "customers"("id"),
  PRIMARY KEY("id")
);

-- A customer can order multiple donuts
CREATE TABLE IF NOT EXISTS "order_content" (
  "order_id" INTEGER,
  "donut_id" INTEGER,
  FOREIGN KEY("order_id") REFERENCES "orders"("id"),
  FOREIGN KEY("donut_id") REFERENCES "donuts"("id")
);

-- Customer history of orders
CREATE TABLE IF NOT EXISTS "orders_history" (
  "customer_id" INTEGER,
  "order_id" INTEGER,
  FOREIGN KEY("customer_id") REFERENCES "customers"("id"),
  FOREIGN KEY("order_id") REFERENCES "orders"("id")
);
