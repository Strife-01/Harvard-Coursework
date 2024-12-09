CREATE INDEX IF NOT EXISTS "student_enrolled_into_course" ON "enrollments" ("student_id", "course_id");
CREATE INDEX IF NOT EXISTS "course_satisfies_criteria" ON "satisfies" ("course_id", "requirement_id");
-- CREATE INDEX IF NOT EXISTS "semester_courses" ON "courses" ("semester");
CREATE INDEX IF NOT EXISTS "enrollment_course_id" ON "enrollments" ("course_id");
