import loguru
from loguru import logger
import os

loguru.logger.add('info.log') #INITIAL

def copying(source, destinstion):
    with open(source, 'rb') as src:
        with open(destinstion, 'wb') as dst:
            while True:
                chunk = src.read(1024)
                if not chunk:
                    break
                dst.write(chunk)
    loguru.logger.info(f'File {src} was copied to {dst}')

src = input("Write path from")
dst = input("Write path to")
copying(src, dst)