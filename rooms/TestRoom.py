import rooms.Rooms


class Test(rooms.Rooms.Room):

    def __init__(self):
        super().__init__([])

    def getDescription(self) -> str:
        return "dit is een kamer beschrijving"
