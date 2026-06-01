import logging

class LogLevelError(Exception):
    """Raised when the log level is invalid."""
    pass

class Logger:
    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def log(self, level: str, message: str) -> None:
        if level.upper() == 'INFO':
            self.logger.info(message)
        elif level.upper() == 'WARNING':
            self.logger.warning(message)
        elif level.upper() == 'ERROR':
            self.logger.error(message)
        elif level.upper() == 'DEBUG':
            self.logger.debug(message)
        else:
            raise LogLevelError('Invalid log level')

# initialize and use the logger
logger = Logger('my_logger')
logger.log('INFO', 'Hello, world!')
