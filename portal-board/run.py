from utils.network import get_network_speed
from utils.system import get_system_uptime
from helpers.status import Status
from helpers.twitter import Twitter


# Get statuss
nwspeed = get_network_speed()
uptime = get_system_uptime()

status = Status(
    network_speed=nwspeed,
    uptime=uptime,
)
status_msg = status.get_msg()

# Tweet
twitter = Twitter()
twitter.tweet(msg=status_msg)
