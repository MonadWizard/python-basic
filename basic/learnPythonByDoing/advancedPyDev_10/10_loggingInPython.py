import logging

#run properly on pycham 
logging.basicConfig(format = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', level = logging.DEBUG)
logger = logging.getLogger('test_loger')

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







