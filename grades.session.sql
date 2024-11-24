CREATE SCHEMA IF NOT EXISTS UniversitySchema;

CREATE TABLE UniversitySchema.StudyPlanDimension(
    StudyPlanKey TEXT PRIMARY KEY,
    StudyPlanTitle TEXT,
    Degree TEXT,
    Branch TEXT
);

CREATE TABLE UniversitySchema.UniversityDimension(
    UniversityKey TEXT PRIMARY KEY,
    UniversityName TEXT
);

CREATE TABLE IF NOT EXISTS UniversitySchema.DepartmentDimension(
    DepartmentKey TEXT PRIMARY KEY,
    DepartmentName TEXT,
    UniversityKey TEXT REFERENCES UniversitySchema.UniversityDimension
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

CREATE TABLE IF NOT EXISTS UniversitySchema.DayDimension(
    DayKey TEXT PRIMARY KEY,
    Day TEXT
);

CREATE TABLE IF NOT EXISTS UniversitySchema.MonthDimension(
    MonthKey TEXT PRIMARY KEY,
    Month TEXT
);

CREATE TABLE IF NOT EXISTS UniversitySchema.SemesterDimension(
    SemesterKey TEXT PRIMARY KEY,
    Semester TEXT
);

CREATE TABLE IF NOT EXISTS UniversitySchema.YearDimension(
    YearKey TEXT PRIMARY KEY,
    Year TEXT
);

CREATE TABLE IF NOT EXISTS UniversitySchema.TimeDimension(
    TimeKey TEXT PRIMARY KEY,
    DayKey TEXT REFERENCES UniversitySchema.DayDimension,
    MonthKey TEXT REFERENCES UniversitySchema.MonthDimension,
    SemesterKey TEXT REFERENCES UniversitySchema.SemesterDimension,
    YearKey TEXT REFERENCES UniversitySchema.YearDimension
);

CREATE TABLE IF NOT EXISTS UniversitySchema.FactGrades (
    Greade TEXT,
    StudyPlanKey TEXT REFERENCES UniversitySchema.StudyPlanDimension,
    LecturerKey TEXT REFERENCES UniversitySchema.LecturerDimension,
    CourseKey TEXT REFERENCES UniversitySchema.CourseDimension,
    TimeKey TEXT REFERENCES UniversitySchema.TimeDimension,
    StudentKey TEXT REFERENCES UniversitySchema.StudentDimension,
    StudentPlanKey TEXT REFERENCES UniversitySchema.StudyPlanDimension
);



-- DROP TABLE IF EXISTS UniversitySchema.studyplandimension;
-- DROP TABLE IF EXISTS UniversitySchema.UniversityDimension;
-- DROP SCHEMA IF EXISTS UniversitySchema;

-- retrieve schemas names
-- SELECT schema_name 
-- FROM information_schema.schemata;

-- SELECT table_name
-- FROM information_schema.tables
-- WHERE table_schema = 'universityschema';

DELETE FROM UniversitySchema.UniversityDimension;
DELETE FROM UniversitySchema.StudyPlanDimension;