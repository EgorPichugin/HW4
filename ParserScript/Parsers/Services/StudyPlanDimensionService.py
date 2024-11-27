class StudyPlanDimensionService():

#region Constructor

    def __init__(self, sourceData: str, cursor):
        self.sourceData = sourceData
        self.cursor = cursor

#endregion

#region Public Methods

    def Start(self):
        try:
            self._insertStudyPlan("Bachelor", "bachelor_study_plans")
            self._insertStudyPlan("Master", "master_study_plans")

            print('=> Data to StudyPlanDimension table successfully inserted.\n')
        
        except Exception as e:
            print(f'Unexpected error: {e}')

#endregion

#region Private Methods

    def _insertStudyPlan(self, type: str, title: str):
        for plan in self.sourceData[title]:
            self.cursor.execute(
                """
                INSERT INTO UniversitySchema.StudyPlanDimension (StudyPlanKey, StudyPlanTitle, Degree, Branch)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (StudyPlanKey) DO NOTHING
                """,
                (plan["id"], plan["name"], type, plan["branch"])
            )

#endregion