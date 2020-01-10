import uptime
import datetime
from logger import logger


def get_system_uptime():
    logger.debug('Getting uptime')
    ts = uptime.uptime()
    td = datetime.timedelta(seconds=ts)
    return f'up {td.days} days, {td.seconds // 3600}:{(td.seconds // 60) % 60}'
