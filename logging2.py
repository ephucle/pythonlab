import logging
#https://realpython.com/python-logging/

#It should be noted that calling basicConfig() to configure the root logger works only if the root logger has not been configured before. Basically, this function can only be called once.

#basic config for logging module
#logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
#logging.basicConfig(filename='app.log', filemode='w', format='%(process)d-%(levelname)s-%(message)s')
#logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)
#logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
logging.basicConfig(filename='app.log', filemode='a', format='%(filename)s %(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

logging.warning('This will get logged to a file')
logging.warning('This is a Warning')





#format='%(name)s - %(levelname)s - %(message)s'
#>>> cat('app.log')
#root - WARNING - This will get logged to a file
#root - WARNING - This is a Warning
#>>>

#format='%(process)d-%(levelname)s-%(message)s'
#>>> cat('app.log')
#4740-WARNING-This will get logged to a file
#4740-WARNING-This is a Warning
#>>>


#logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')

#>>> cat('app.log')
#2020-05-29 11:07:30,539 - This will get logged to a file
#2020-05-29 11:07:30,539 - This is a Warning
#2020-05-29 11:07:30,539 - Admin logged in
#>>>


#logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning('Admin logged out')

#>>> cat ('app.log')
#29-May-20 11:09:54 - This will get logged to a file
#29-May-20 11:09:54 - This is a Warning
#29-May-20 11:09:54 - Admin logged in
#29-May-20 11:09:54 - Admin logged out
#>>>

#logging file filename
#logging.basicConfig(filename='app.log', filemode='a', format='%(filename)s %(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
#logging2.py 2020-05-29 12:36:10 - This will get logged to a file
#logging2.py 2020-05-29 12:36:10 - This is a Warning
#logging2.py 2020-05-29 12:36:10 - Admin logged in
#logging2.py 2020-05-29 12:36:10 - Admin logged out
#>>>