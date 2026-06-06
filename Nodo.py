class Nodo:
    """Clase que representa un nodo individual de la lista."""
    def __init__(self, dato):
        self.dato = dato       # El valor que almacena el nodo (Ahora será un objeto Cactus)
        self.siguiente = None  # Referencia al siguiente nodo