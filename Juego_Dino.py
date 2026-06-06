import pygame
import random
import sys
from Lista_Simple import ListaSimple

# --- Constantes Globales ---
ANCHO, ALTO = 800, 300
FPS = 60
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (34, 139, 34)

class Dinosaurio:
    """Modelo del jugador con físicas básicas."""
    def __init__(self):
        self.ancho = 40
        self.alto = 60
        self.x = 50
        self.y = ALTO - self.alto - 20
        self.velocidad_y = 0
        self.gravedad = 0.6
        self.en_suelo = True
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def saltar(self):
        if self.en_suelo:
            self.velocidad_y = -12
            self.en_suelo = False

    def actualizar(self):
        # Aplicar gravedad
        self.velocidad_y += self.gravedad
        self.y += self.velocidad_y

        # Colisión con el suelo
        if self.y >= ALTO - self.alto - 20:
            self.y = ALTO - self.alto - 20
            self.en_suelo = True
            self.velocidad_y = 0
            
        self.rect.topleft = (self.x, self.y)

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, NEGRO, self.rect)

class Cactus:
    """Modelo del obstáculo que será almacenado en los Nodos de la Lista."""
    def __init__(self, x):
        self.ancho = 20
        self.alto = 40
        self.x = x
        self.y = ALTO - self.alto - 20
        self.velocidad = 5
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def actualizar(self):
        self.x -= self.velocidad
        self.rect.topleft = (self.x, self.y)

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, VERDE, self.rect)

def ejecutar_juego():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Dino Game - Implementación con Lista Enlazada")
    reloj = pygame.time.Clock()

    dino = Dinosaurio()
    lista_obstaculos = ListaSimple() # ¡Aquí instanciamos tu estructura de datos!
    
    timer_spawn = 0
    puntuacion = 0
    fuente = pygame.font.SysFont("Arial", 24)

    jugando = True
    while jugando:
        # 1. Captura de Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE or evento.key == pygame.K_UP:
                    dino.saltar()

        # 2. Lógica y Spawns
        dino.actualizar()
        puntuacion += 1

        # Generar nuevos obstáculos aleatoriamente
        timer_spawn += 1
        if timer_spawn > random.randint(60, 120):
            nuevo_cactus = Cactus(ANCHO)
            lista_obstaculos.insertar_al_final(nuevo_cactus) # Inserción algorítmica
            timer_spawn = 0

        # 3. Actualización iterando la Lista Simple
        # Usamos el método __iter__ que agregamos a Lista_Simple
        for cactus in lista_obstaculos:
            cactus.actualizar()
            
            # Detección de colisiones (Caja contra Caja)
            if dino.rect.colliderect(cactus.rect):
                print(f"¡Colisión! Puntuación final: {puntuacion // 10}")
                jugando = False

        # Liberación de memoria (Eliminamos nodos que salen por la izquierda)
        # Revisamos la cabeza de la lista de forma constante O(1)
        if lista_obstaculos.cabeza and lista_obstaculos.cabeza.dato.x < -50:
            lista_obstaculos.eliminar_al_inicio()

        # 4. Renderizado Visual
        pantalla.fill(BLANCO)
        
        # Dibujar línea del suelo
        pygame.draw.line(pantalla, NEGRO, (0, ALTO - 20), (ANCHO, ALTO - 20), 2)
        
        dino.dibujar(pantalla)
        for cactus in lista_obstaculos:
            cactus.dibujar(pantalla)
            
        texto_pts = fuente.render(f"Puntos: {puntuacion // 10}", True, NEGRO)
        pantalla.blit(texto_pts, (10, 10))

        pygame.display.flip()
        reloj.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    ejecutar_juego()