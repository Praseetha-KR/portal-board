import fastdotcom
from logger import logger


def get_network_speed():
    logger.debug('Fetching from fast.com')
    return fastdotcom.fast_com()
