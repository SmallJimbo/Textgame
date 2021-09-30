from abc import abstractmethod

class Command:
    commandname: str


    def __init__(self, name):
        commandname = name

    def getName(self) ->str:
        return self.commandname


@abstractmethod
def execute(self):
