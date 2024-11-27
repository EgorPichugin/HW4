class ResultService:
    
#region Constructor

    def __init__(self, results: list[str], cursor):
        self.courseResults = results
        self.cursor = cursor

#endregion

#region Public Methods

    def Start(self) -> None:
        try:
            for courseResult in self.courseResults:
                self._importData(courseResult)

            print('=> Data to StudentDimension, TimeDimension and FactGrades tables successfully inserted.\n')
        except Exception as e:
                print(f'Unexpected error: {e}')

#endregion

#region Private Methods

    def _importData(self, courseResult: str) -> None:

        results: list[str] = courseResult["results"]
        courseKey: str = courseResult["course"]
        lecturerKey: str = courseResult["examinator"]
        timeKey: str = courseResult["date"]
        
        self._importDataToTimeDimension(timeKey)

        for result in results:
            self._imporDataToStudentDimension(result)
            self._importDataToFactGrades(lecturerKey, courseKey, timeKey, result)

    def _imporDataToStudentDimension(self, result: str) -> None:
        self.cursor.execute(
                """
                INSERT INTO UniversitySchema.StudentDimension (StudentKey, Name)
                VALUES (%s, %s)
                ON CONFLICT (StudentKey) DO NOTHING
                """,
                (result["matno"], result["name"])
            )
        
    def _getSemester(self, month: str) -> str:
        semester_mapping: dict[str, str] = {
            "01" : "winter",
            "02" : "winter",
            "03" : "winter",
            "04" : "winter",
            "05" : "winter",
            "06" : "winter",
            "07" : "summer",
            "08" : "summer",
            "09" : "summer",
            "10" : "summer",
            "11" : "summer",
            "12" : "summer",
        }

        return semester_mapping.get(month)
    
    def _importDataToTimeDimension(self, dateKey: str):
        date: list[str] = dateKey.split("-")

        year, month, day, semester = "NaN", "NaN", "NaN", "NaN"

        if len(date) > 0:
            year = date[0]
        if len(date) > 1:
            month = date[1]
            semester = self._getSemester(month)
        if len(date) > 2:
            day = date[2]

        self.cursor.execute(
                """
                INSERT INTO UniversitySchema.TimeDimension (TimeKey, Day, Month, Semester, Year)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (TimeKey) DO NOTHING
                """,
                (dateKey, day, month, semester, year)
            )

    def _importDataToFactGrades(self, lecturerKey: str, courseKey: str, timeKey, result: str) -> None:
        self.cursor.execute(
                """
                INSERT INTO UniversitySchema.FactGrades (MatNumberKey, Grade, LecturerKey, CourseKey, TimeKey, StudentKey, StudyPlanKey)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (MatNumberKey) DO NOTHING
                """,
                (result["matno"], result["grade"], lecturerKey, courseKey, timeKey, result["matno"], result["studyplan"])
            )

#endregion

