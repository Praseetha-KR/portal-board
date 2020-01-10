import attr
import datetime


@attr.s
class Status:
    time = attr.ib(default=datetime.datetime.now())
    network_speed = attr.ib(default=0.0)
    uptime = attr.ib(default='')

    def get_msg(self):
        return (
            f'Status on {self.time.strftime("%d %B %Y %H:%M:%S")}\n'
            f'network speed: {self.network_speed}\n'
            f'uptime: {self.uptime}'
        )
