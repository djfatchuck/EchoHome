import PyEcho
import time
from settings import *


class EchoToDoReader():

    def __init__(self):
        self.echo = PyEcho.PyEcho(USER, PASSWORD)
        self.sleep_time = 5
        self.command_list = {}

    def run(self):
        if self.echo:
            tasks = self.echo.tasks()
            for task in tasks:
                command = task['text']
                #TODO add commands handling
                self.echo.deleteTask(task)
        time.sleep(self.sleep_time)


class EchoCardReader():

    def __init__(self):
        self.echo = PyEcho.PyEcho(USER, PASSWORD)
        self.sleep_time = 5
        self.command_list = {}

    def run(self):
        if self.echo:
            cards = self.echo.cards()
            for card in cards:
                try:
                    text = card['playbackAudioAction']['mainText']
                except TypeError:
                    pass
                #TODO add commands handling
                self.echo.deleteTask(card)
        time.sleep(self.sleep_time)