import logging
#Level

#Numeric value

#CRITICAL 50
#ERROR 40
#WARNING 30
#INFO 20
#DEBUG 10
#NOTSET 0
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

#set level de co the logging cac loai log
print("setting level")
logging.basicConfig(level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

#save to file
#logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

logging.basicConfig(filename='app.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
logging.info("Running Urban Planning")
logging.critical('This is a critical message')
