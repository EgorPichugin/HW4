from ParserScript.Parsers.DataImporter import DataImporter

importer: DataImporter = DataImporter()
importer.ConnectToDatabase()
importer.Parse()
importer.InitializeServices()
importer.ImportData()
importer.CloseConnection()