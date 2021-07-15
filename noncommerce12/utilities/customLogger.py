import logging

class LogGen:
    @staticmethod
    def runmethod():
        logging.basicConfig(filename="Logs\\log2.log",format='%(asctime)s:%(levelname)s:%(message)s:',datefmt="%Y-%m-%d %H:%M:%S",force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        print("Logging method running")
        return logger

