import logging
import coloredlogs


logger = logging.getLogger('portal-board')

h = logging.StreamHandler()
h.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
logger.addHandler(h)

coloredlogs.install(level='DEBUG', logger=logger)
logger.debug('Initialized logger')
