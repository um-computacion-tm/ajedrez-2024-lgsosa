class Piece:  # Clase Padre
    def __init__(self, color):
        self.__color__ = color

    @property
    def color(self):
        return self.__color__
