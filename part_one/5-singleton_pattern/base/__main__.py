from logger_base import Logger

logger = Logger('my.log')
logger.write_log('Logging with classic Singleton pattern\n')
logger2 = Logger('***ignored***')   # ! if it works correctly this will be ignored as the file is already open.
logger2.write_log('Another log record\n')

logger.close_log()

with open('my.log', 'r') as f:
    for line in f:
        print(line, end='')