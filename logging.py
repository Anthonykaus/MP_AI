import logging

class Logger:
    def __init__(self, name="AI_Project", level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # Create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Add formatter to ch
        ch.setFormatter(formatter)

        # Add ch to logger
        self.logger.addHandler(ch)

    def log(self, message, level=logging.INFO):
        if level == logging.DEBUG:
            self.logger.debug(message)
        elif level == logging.INFO:
            self.logger.info(message)
        elif level == logging.WARNING:
            self.logger.warning(message)
        elif level == logging.ERROR:
            self.logger.error(message)
        elif level == logging.CRITICAL:
            self.logger.critical(message)

# Example usage
if __name__ == "__main__":
    logger = Logger()
    logger.log("This is an info message")
    logger.log("This is a debug message", level=logging.DEBUG)
