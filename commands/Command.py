from abc import abstractmethod


class Command:
    commandName: str

    def __init__(self, name):
        self.commandName = name

    def getName(self) -> str:
        return self.commandName

    @abstractmethod
    def execute(self): pass
