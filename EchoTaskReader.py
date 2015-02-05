import getpass
import PyEcho
import time
from settings import *

if USER == '' or PASSWORD == '':
    USER = raw_input('Email: ')
    PASSWORD = getpass.getpass()

class EchoTaskReader():

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
