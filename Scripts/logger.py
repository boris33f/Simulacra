import sims4
from sims4 import commands

class Logger(object):
    # CLS values
    _current_connection = None

    @classmethod
    def set_connection(cls, _connection):
        cls._current_connection = _connection

    @classmethod
    def log(cls, msg: str = ""):
        if cls._current_connection is None:
            return
        output = sims4.commands.CheatOutput(cls._current_connection)
        output(msg)
