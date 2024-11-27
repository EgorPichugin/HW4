import json
import psycopg2
import re
from ParserScript.constants.Constants import Constants
from ParserScript.Parsers.Services.StudyPlanDimensionService import *
from ParserScript.Parsers.Services.DepartmentDimensionService import *
from ParserScript.Parsers.Services.CourseDimensionService import *
from ParserScript.Parsers.Services.LecturerDimensionService import *
from ParserScript.Parsers.Services.ResultsService import *

class DataImporter:

#region Constructor

    def __init__(self):
        self.metadataPath = Constants.metadata
        self.coursesPath = Constants.corses
        self.resultPaths: list[str] = Constants.Results.collection
        
#endregion

#region Public Methods``

    def Parse(self) -> None:
        try:
            self.metadata = DataImporter._loadJsonFromPath(self.metadataPath)
            self.coursesData = DataImporter._loadJsonFromPath(self.coursesPath)

            print('=> aau_metdata.json successfully parsed\n')
            print('=> aau_corses.json successfully parsed\n')
        except Exception as e:
            print(f'Unexpected error: {e}')

        self.parsedResultCollection: list[str] = []
        for resultPath in self.resultPaths:
            self.parsedResultCollection.append(DataImporter._loadJsonFromPath(resultPath))
            fileName: str = resultPath.split("\\")[-1]
            print(f'=> {fileName} successfully parsed\n')

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
                print("=> Successfully connected\n")
            else:
                print("No connection with database")


    def CloseConnection(self) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def InitializeServices(self):
        self.studyPlanDimensionService = StudyPlanDimensionService(self.metadata, self.cursor)
        self.departmentDimensionService = DepartmentDimensionService(self.coursesData, self.cursor)
        self.courseDimensionService = CourseDimensionService(self.coursesData, self.cursor)
        self.lecturerDimensionService = LecturerDimensionService(self.metadata, self.cursor)
        self.resultService = ResultService(self.parsedResultCollection, self.cursor)
        
    def ImportData(self):
        self.studyPlanDimensionService.Start()
        self.departmentDimensionService.Start()
        self.courseDimensionService.Start()
        self.lecturerDimensionService.Start()
        self.resultService.Start()

#endregion

#region Private Methods

    @staticmethod
    def _loadJsonFromPath(path: str):

        with open(path, 'r') as file:
                result: str = json.load(file)
        
        return result
    
#endregion