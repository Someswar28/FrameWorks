import logging

class logGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fileHandler = logging.FileHandler('.\\logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s: %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger





