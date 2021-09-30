import rooms.Rooms


class Test(rooms.Rooms.Base):

    def __init__(self):
        super().__init__([])

    def getDescription(self) -> str:
        return "dit is een kamer beschrijving"
