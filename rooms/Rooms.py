class Base:
    items = []

    def __init__(self, list_with_items):
        self.items = list_with_items;

    def do(self): pass

    def getDescription(self) -> str:
        pass
