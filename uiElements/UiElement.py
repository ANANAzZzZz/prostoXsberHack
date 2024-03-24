class UIElement:
    def __init__(self, ord_par: int = 0):
        self.ord = ord_par
        self.elementType = self.__class__.__name__
