import logging

#############################################
#                                           #
#      'debug': logging.DEBUG,              #
#      'info': logging.INFO,                #
#      'warning': logging.WARNING,          #
#      'error': logging.ERROR,              #
#      'critical': logging.CRITICAL         #
#############################################

LOGGING_LEVEL = logging.INFO

# TODO: Use config file for logging
logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=LOGGING_LEVEL)
