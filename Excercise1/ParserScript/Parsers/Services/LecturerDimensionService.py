import re

class LecturerDimensionService:

#region Constructor

    def __init__(self, sourceData: str, cursor):
        self.sourceData = sourceData
        self.cursor = cursor

#endregion

#region Public Methods

    def Start(self):
            lecturers: list[str] = self.sourceData["lecturers"]

            try:
                for lecturer in lecturers:
                    parsedDict: dict[str, str] = self._parseLecturer(lecturer["name"])
                    rank: str = parsedDict["rank"]
                    title: str = parsedDict["title"]
                    name: str = parsedDict["name"]

                    self.cursor.execute(
                        """
                        INSERT INTO UniversitySchema.LecturerDimension (LecturerKey, Name, Rank, Title, DepartmentKey)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (LecturerKey) DO NOTHING
                        """,
                        (lecturer["id"], name, rank, title, lecturer["department"])
                    )
                
                print('=> Data to LecturerDimension table successfully inserted.\n')

            except Exception as e:
                print(f'Unexpected error: {e}')

#endregion

#region Private Methods

    def _parseLecturer(self, name: str) -> dict[str, str]:
            pattern: str = r"^(?P<rank>[\w\.\-]+(?:[\s\-][\w\.\-]+)*)(?:\s+)(?P<title>[\w\.\-]+(?:[\s\.\-][\w\.\-]+)*)(?:\s+)(?P<name>.+)$"

            match = re.match(pattern, name)
        
            if match:
                return match.groupdict()  # Возвращаем результат в виде словаря
            else:
                return None
        
#endregion