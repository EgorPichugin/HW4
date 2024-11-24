import json
import psycopg2

class MetadataParserService:

    def __init__(self, json_path):
        self.json_path: str = json_path

    def ConnectToDatabase(self) -> None:
        self.conn: psycopg2.connection = psycopg2.connect(
            dbname="Grades",
            user="postgres",
            password="qwerty",
            host="localhost",
            port="5432"
        )

        self.cursor = self.conn.cursor()

        with self.conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            if result:
                print("Successfully connected")
            else:
                print("No connection with database")

    def Parse(self) -> None:
        with open(self.json_path, 'r') as file:
            self.data: str = json.load(file)
        
        self._insertDataInUniversityDimension()
        self._insertDataInStudyPlanDimension()

    def CloseConnection(self) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def _insertDataInUniversityDimension(self):
        self.cursor.execute(
            """
            INSERT INTO UniversitySchema.UniversityDimension (UniversityKey, UniversityName)
            VALUES (%s, %s)
            """,
            (self.data["id"], self.data["name"])
        )

    def _insertDataInStudyPlanDimension(self):
        self._insertStudyPlan("Bachelor", "bachelor_study_plans")
        self._insertStudyPlan("Master", "master_study_plans")
            
    def _insertStudyPlan(self, type: str, title: str):
        for plan in self.data[title]:
            self.cursor.execute(
                """
                INSERT INTO UniversitySchema.StudyPlanDimension (StudyPlanKey, StudyPlanTitle, Degree, Branch)
                VALUES (%s, %s, %s, %s)
                """,
                (plan["id"], plan["name"], type, plan["branch"])
            )

