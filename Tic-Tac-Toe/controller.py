import logging
class Controller:

    def __init__(self, log_file):
        self.file_name = log_file
        logging.basicConfig(filename=log_file, level=logging.DEBUG)
        self.logging = logging.getLogger()
        logging.info("Controller initiated")

    def __str__(self):
        print "LOG FILE = " + self.file_name
