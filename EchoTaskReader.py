import PyEcho
from settings import *


class EchoTaskReader():

    def __init__(self):
        self.echo = PyEcho.PyEcho(USER, PASSWORD)
        self.task_list = []
        self.update_time = 600

    def update_tasks(self):
        tasks = self.echo.tasks()

        for task in tasks:
            if task not in self.task_list:
                self.task_list.append(task)

    def run_next_task(self):
        task = self.task_list.pop(0)

    def change_update_time(self, time):
        self.update_time = time
