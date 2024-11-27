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