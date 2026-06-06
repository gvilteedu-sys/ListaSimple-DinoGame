from Nodo import Nodo

class ListaSimple:
    """Clase que gestiona la estructura y operaciones de la lista."""
    def __init__(self):
        self.cabeza = None     # La lista inicia vacía

    def insertar_al_inicio(self, dato):
        """Inserta un nuevo nodo al principio de la lista."""
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        # Comentamos los prints para no saturar la consola durante el juego a 60 FPS
        # print(f"-> Insertado {dato} al inicio.")

    def insertar_al_final(self, dato):
        """Inserta un nuevo nodo al final de la lista."""
        nuevo_nodo = Nodo(dato)
        
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        
        actual.siguiente = nuevo_nodo

    def eliminar(self, dato):
        """Busca y elimina la primera ocurrencia de un dato."""
        actual = self.cabeza
        anterior = None

        while actual and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente

        if not actual:
            return

        if not anterior:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente

    # --- NUEVOS MÉTODOS PARA INTEGRACIÓN GRÁFICA ---
    
    def eliminar_al_inicio(self):
        """
        Extrae y elimina el primer nodo de la lista. 
        Vital para liberar memoria cuando un obstáculo sale de la pantalla.
        """
        if getattr(self, 'cabeza', None) is None:
            return None
        
        nodo_eliminado = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return nodo_eliminado.dato

    def __iter__(self):
        """
        Permite iterar la estructura dinámicamente en el bucle principal del juego.
        Ejemplo: for obstaculo in mi_lista: ...
        """
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente
            
    # -----------------------------------------------

    def mostrar_lista(self):
        """Recorre la lista e imprime los elementos visualmente."""
        if not self.cabeza:
            print("La lista está vacía.")
            return

        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        
        print(" -> ".join(elementos) + " -> None")