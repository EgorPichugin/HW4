CREATE SCHEMA IF NOT EXISTS UniversitySchema;

CREATE TABLE UniversitySchema.StudyPlanDimension(
    StudyPlanKey TEXT PRIMARY KEY,
    StudyPlanTitle TEXT,
    Degree TEXT,
    Branch TEXT
);

CREATE TABLE IF NOT EXISTS UniversitySchema.DepartmentDimension(
    DepartmentKey TEXT PRIMARY KEY,
    DepartmentName TEXT,
    UniversityName TEXT
);

CREATE TABLE IF NOT EXISTS UniversitySchema.CourseDimension(
    CourseKey TEXT PRIMARY KEY,
    Name TEXT,
    Type TEXT,
    ECTS TEXT,
    Level TEXT,
    DepartmentKey TEXT REFERENCES UniversitySchema.DepartmentDimension
);

CREATE TABLE IF NOT EXISTS UniversitySchema.LecturerDimension(
    LecturerKey TEXT PRIMARY KEY,
    Name TEXT,
    Rank TEXT,
    Title TEXT,
    DepartmentKey TEXT REFERENCES UniversitySchema.DepartmentDimension
);

CREATE TABLE IF NOT EXISTS UniversitySchema.StudentDimension(
    StudentKey TEXT PRIMARY KEY,
    Name TEXT
);


CREATE TABLE IF NOT EXISTS UniversitySchema.TimeDimension(
    TimeKey TEXT PRIMARY KEY,
    Day TEXT,
    Month TEXT,
    Semester TEXT,
    Year TEXT
);

CREATE TABLE IF NOT EXISTS UniversitySchema.FactGrades (
    MatNumberKey TEXT PRIMARY KEY,
    Grade TEXT,
    LecturerKey TEXT REFERENCES UniversitySchema.LecturerDimension,
    CourseKey TEXT REFERENCES UniversitySchema.CourseDimension,
    TimeKey TEXT REFERENCES UniversitySchema.TimeDimension,
    StudentKey TEXT REFERENCES UniversitySchema.StudentDimension,
    StudyPlanKey TEXT REFERENCES UniversitySchema.StudyPlanDimension
);



DROP TABLE IF EXISTS UniversitySchema.studyplandimension;
DROP TABLE IF EXISTS UniversitySchema.UniversityDimension;
DROP TABLE IF EXISTS UniversitySchema.departmentdimension;
DROP TABLE IF EXISTS UniversitySchem.coursedimension
DROP TABLE IF EXISTS UniversitySchema.lecturerdimension;
DROP TABLE IF EXISTS UniversitySchema.StudentDimension;
DROP TABLE IF EXISTS UniversitySchema.DayDimension;
DROP TABLE IF EXISTS UniversitySchema.Monthimension;
DROP TABLE IF EXISTS UniversitySchema.SemesterDimension;
DROP TABLE IF EXISTS UniversitySchema.yeardimension;
DROP TABLE IF EXISTS UniversitySchema.timedimension;
DROP TABLE IF EXISTS UniversitySchem.FactGrades
-- DROP TABLE IF EXISTS UniversitySchema.FactGrades;
-- DROP SCHEMA IF EXISTS UniversitySchema;

-- retrieve schemas names
-- SELECT schema_name 
-- FROM information_schema.schemata;

-- SELECT table_name
-- FROM information_schema.tables
-- WHERE table_schema = 'universityschema';

DELETE FROM UniversitySchema.StudyPlanDimension;
DELETE FROM UniversitySchema.DepartmentDimension;
DELETE FROM UniversitySchema.CourseDimension;
DELETE FROM UniversitySchema.LecturerDimension;

DELETE FROM UniversitySchema.TimeDimension;
DELETE FROM UniversitySchema.StudentDimension;
DELETE FROM UniversitySchema.StudyPlanDimension;
-- CREATE TABLE IF NOT EXISTS UniversitySchema.DayDimension(
--     DayKey TEXT PRIMARY KEY,
--     Day TEXT
-- );

-- CREATE TABLE IF NOT EXISTS UniversitySchema.MonthDimension(
--     MonthKey TEXT PRIMARY KEY,
--     Month TEXT
-- );

-- CREATE TABLE IF NOT EXISTS UniversitySchema.SemesterDimension(
--     SemesterKey TEXT PRIMARY KEY,
--     Semester TEXT
-- );

-- CREATE TABLE IF NOT EXISTS UniversitySchema.YearDimension(
--     YearKey TEXT PRIMARY KEY,
--     Year TEXT
-- );