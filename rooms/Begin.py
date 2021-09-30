import rooms.Rooms


class Badkamer(rooms.Rooms.Base):

    def __init__(self):
        super().__init__([])

    def getDescription(self) -> str:
        return "Je komt in een badkamr terecht. Je ziet een kast en een lavabo."

    def do(self):
        input("wat doe je ? ")
        if input == "sterven":
            print("Je valt plots dood. Hartaavnal. spijtig !")