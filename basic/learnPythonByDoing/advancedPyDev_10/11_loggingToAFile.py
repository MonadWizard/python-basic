import logging

#run properly on pycham 
logging.basicConfig(format = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', 
                    datefmt = '%d-%m-%Y %H:%M:%S',
                    level = logging.DEBUG,
                    filename = 'logs.txt')

logger = logging.getLogger('books')

logger.info('This will not show up.')
logger.warning('this wil.l')
logger.debug('This is a debug message.')
logger.critical('A critical error occurred.')



"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""







