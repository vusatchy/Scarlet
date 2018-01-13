import abc


class AbstractHandler(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def predicate(self, message):
        """This method should return boolean value"""

    @abc.abstractmethod
    def handle(self, bot, message):
        """This method should handle message"""
