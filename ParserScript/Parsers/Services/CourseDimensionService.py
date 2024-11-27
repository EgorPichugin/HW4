class CourseDimensionService:

#region Constructor

    def __init__(self, sourceData: str, cursor):
        self.sourceData = sourceData
        self.cursor = cursor

#endregion

#region Public Methods

    def Start(self):
            try:
                self._insertCourseDimension("bachelor")
                self._insertCourseDimension("master")

                print('=> Data to CourseDimension table successfully inserted.\n')

            except Exception as e:
                print(f'Unexpected error: {e}')

#endregion

#region Private Methods

    def _insertCourseDimension(self, degree: str) -> None:
        for program in self.sourceData[degree]:
            self.cursor.execute(
                """
                INSERT INTO UniversitySchema.CourseDimension (CourseKey, Name, Type, ECTS, Level, DepartmentKey)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (CourseKey) DO NOTHING
                """,
                (program["id"], program["title"], program["type"], program["ECTS"], degree, program["department"])
            )


#endregion