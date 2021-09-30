from abc import abstractmethod

class Command:
    commandname = ""

    def __init__(self, name):
        commandname = name

    def getName(self):
        return self.commandname


@abstractmethod
def execute(self):
