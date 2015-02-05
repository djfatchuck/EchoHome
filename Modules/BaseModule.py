class BaseModule():

    def __init__(self):
        self.commands = {'sample': self.sample_test}

    def execute_task(self, task='sample', **kwargs):
        try:
            self.commands[task](**kwargs)
        except KeyError:
            print "This is not a known task"

    def sample_test(self, **kwargs):
        print "This is a sample task"

