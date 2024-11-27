class DepartmentDimensionService():

#region Constructor

    def __init__(self, sourceData: str, cursor):
        self.sourceData = sourceData
        self.cursor = cursor

#endregion

#region Public Methods

    def Start(self):
        try:
            self._insertDepartmentDimension("bachelor")
            self._insertDepartmentDimension("master")

            print('=> Data to DepartmentDimension table successfully inserted.\n')
        
        except Exception as e:
            print(f'Unexpected error: {e}')

#endregion

#region Private Methods

    def _insertDepartmentDimension(self, degree: str) -> None:
        for program in self.sourceData[degree]:
            self.cursor.execute(
                """
                INSERT INTO UniversitySchema.DepartmentDimension (DepartmentKey, DepartmentName, UniversityName)
                VALUES (%s, %s, %s)
                ON CONFLICT (DepartmentKey) DO NOTHING
                """,
                (program["department"], program["department"], "Universität Klagenfurt")
            )

#endregion