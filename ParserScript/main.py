from Parsers.MetaDataParser import MetadataParserService
from constants.Constants import Constants

metadataParser: MetadataParserService = MetadataParserService(Constants.metadata)
metadataParser.ConnectToDatabase()
metadataParser.Parse()
metadataParser.CloseConnection()