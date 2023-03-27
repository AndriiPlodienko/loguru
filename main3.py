from loguru import logger
import requests
import time

logger.add('web.log')

@logger.catch
def get_content(url):
    logger.info('Getting content')
    start_time = time.time()

    response = requests.get(url)

    end_time = time.time()
    delta_time = end_time - start_time

    logger.info(f'Finished getting content from page {url} in {delta_time} sec.')
    logger.info(f'Response status code {response.status_code}')
    logger.info(f'Response content: {response.content}')

    return response.content

if __name__ == "__main__":
    url = input('Your url:')