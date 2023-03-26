from loguru import logger
import time

logger.add('app.log', format='{time} {level} {message}', level='DEBUG')

@logger.catch
def sum(a,b):
    logger.debug(f'Adding {a} and {b} ')
    stime = time.time()
    res = a + b
    etime = time.time()
    logger.debug(f'Result: {res}. Execution time:{etime - stime} seconds')
    return res

if __name__ == "__main__":
    a = 1
    b = 5
    sum(a,b)