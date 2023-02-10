import logging
from logging.handlers import TimedRotatingFileHandler
import time

class Logger:

    def logSetup(self):
        logger = logging.getLogger('app.log')
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(fmt='[%(asctime)s] %(message)s',datefmt = '%y-%m-%d %H:%M:%S')
        fh = TimedRotatingFileHandler('app.log',when='midnight')# when='S', interval=5)
        fh.setFormatter(formatter)
        fh.suffix = "%Y-%m-%d"
        logger.addHandler(fh)

        for i in range(20):
            logger.debug(f'Hello world {i+1}')
            # logging.debug("Logging test...")
            #logging.info("Hello World")
            # logging.warning("The program may not function properly")
            # logging.error("The program encountered an error")
            # logging.critical("The program crashed")
            time.sleep(1)
        return logger


log = Logger()
log.logSetup()

# if __name__ == '__main__':
#     pass