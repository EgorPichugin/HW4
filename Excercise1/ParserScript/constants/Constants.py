
# Provide paths to json files
class Constants:
    metadata: str = "path/to/json"
    corses: str = "path/to/json"

    class Results:
        _blockchainsBpm: str = "path/to/json"
        _dataEngineering: str = "path/to/json"
        _datenbaken: str = "path/to/json"
        _esop: str = "path/to/json"
        _interop: str = "path/to/json"
        _parallel: str = "path/to/json"
        _processEngineering: str = "path/to/json"
        _webTech: str = "path/to/json"

        collection: list[str] = [_blockchainsBpm, _dataEngineering, _datenbaken, _esop, _interop, _parallel, _processEngineering, _webTech]