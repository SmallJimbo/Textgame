import rooms.Begin


def start():
   kamer = rooms.Begin.Badkamer()
   print(kamer.getDescription())
   kamer.do()