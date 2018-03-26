from text_query_handlers import PingHandler as ph
from text_query_handlers import RightHandler as rh
from text_query_handlers import GreetingHandler as gh
from text_query_handlers import HelloHandler as hh
from text_query_handlers import RandomHandler as randh
from text_query_handlers import LoveHandler as lh
from  text_query_handlers import ScheduleHandler as sh


class HandlersRegistration(object):
    handlers = []

    def registration(self):
        self.handlers.append(sh.ScheduleHandler())
        self.handlers.append(ph.PingHandler())
        self.handlers.append(rh.RightHandler())
        self.handlers.append(gh.GreetingHandler())
        self.handlers.append(hh.HelloHandler())
        self.handlers.append(randh.RandomHandle())
        self.handlers.append(lh.LoveHandle())

    def get_handlers(self):
        return self.handlers
