import logging


class LogsGen:
    @staticmethod
    def logs():
        logging.basicConfig(filename="../Logs/nopcomm.logs",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m-%d-%y %I:%M:%S %p',
                            filemode='w', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def ddt_logs():
        logging.basicConfig(filename="../Logs/ddt_nopcomm.logs",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m-%d-%y %I:%M:%S %p',
                            filemode='w', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def customer_create_logs():
        logging.basicConfig(filename="../Logs/customer_create_nopcomm.logs",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m-%d-%y %I:%M:%S %p',
                            filemode='w', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger