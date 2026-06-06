# Documento Técnico Maestro: project_context.md

## 1. Visión General y Dominio del Proyecto

**Objetivo Core:**  
El propósito principal del sistema es demostrativo y educativo; busca ilustrar la aplicación práctica de una estructura de datos lineal abstracta (Lista Simple Enlazada) integrada como motor de gestión de estado dentro de un entorno gráfico interactivo (un clon simplificado del juego *Dinosaurio de Chrome*). Resuelve el problema de negocio de visualizar y operar dinámicamente sobre la memoria en un escenario en tiempo real.

**Casos de Uso Principales:**
*   **Actor: Usuario/Jugador**
    *   **Flujos:** Interactúa con la aplicación evadiendo obstáculos a través de un salto accionado por teclado (Espacio o Flecha Arriba). Consume el estado visual (puntuación y renderizado).
*   **Actor: Bucle de Juego (System Daemon)**
    *   **Flujos:** Gestiona proceduralmente la instanciación de obstáculos basada en temporizadores aleatorios, computa las leyes físicas (gravedad, colisión Bounding Box), actualiza la pantalla a 60 FPS y administra la memoria dinámica destruyendo las entidades que abandonan la pantalla.

## 2. Matriz del Stack Tecnológico

| Capa / Dominio | Tecnología / Herramienta | Propósito en el Proyecto |
| :--- | :--- | :--- |
| **Capa de Presentación / Cliente** | `Pygame` | Motor de renderizado 2D, manejo del bucle principal de interfaz de usuario, captura de eventos de hardware (teclado) y renderizado de primitivas y fuentes. |
| **Lógica de Servidor / Aplicación** | `Python 3.x` | Lenguaje base. Orquestación lógica usando un enfoque híbrido: Estructurado proceduralmente para el *Game Loop* y Orientado a Objetos (POO) para el modelado de entidades y la estructura de datos. |
| **Capa de Datos & Almacenamiento** | `Estructura en Memoria Propia` | Implementación desde cero de una *Singly Linked List* (`ListaSimple`, `Nodo`). Actúa como la "base de datos" volátil en RAM para las entidades de tipo obstáculo. |
| **Infraestructura & Herramientas** | `venv`, `requirements.txt` | Aislamiento de dependencias locales (entorno virtualizado de Python) y declaración explícita de librerías externas de terceros (`pygame`). |

## 3. Arquitectura del Sistema y Flujo de Datos

**Patrón Arquitectónico:**  
Monolito de escritorio bajo el patrón **Game Loop** acoplado a un diseño de **Estructuras de Datos Personalizadas**. La lógica no está dividida en servicios independientes, sino que se ejecuta de manera síncrona en un único hilo y proceso.

**Comunicación e Integración:**  
La integración se realiza internamente a través de importaciones de módulos directas en el mismo nivel espacial. `Juego_Dino.py` funciona como el Módulo Controlador (Main Entrypoint), el cual instancia y orquesta a los Módulos de Datos Abstractos (`Lista_Simple.py` y `Nodo.py`). Todo reside y se comunica a través del espacio de memoria compartida asignado por el intérprete de Python.

**Flujo de Datos (Data Flow):**
1.  **Input / Generación:** El bucle principal registra el tiempo; al alcanzar un umbral estocástico, se instancia un objeto `Cactus`.
2.  **Encapsulamiento / Escritura:** El controlador invoca el método de la estructura de datos, empaquetando la referencia del objeto `Cactus` en la propiedad `dato` de un nuevo `Nodo` y acoplándolo a la cadena lógica en la RAM.
3.  **Procesamiento (Lectura/Update):** Un generador interno (`__iter__`) expone los datos iterativamente al Game Loop, aplicándoles transformaciones espaciales en el plano X y cálculos de intersección matemática.
4.  **Recolección de Basura / Borrado:** Mediante una validación algorítmica constante de la cabeza de la lista, si el dato encapsulado supera los límites lógicos de la pantalla, se rompe el enlace del nodo cabeza para forzar la liberación de memoria, devolviendo la estabilidad al ciclo.

## 4. Lógica de Negocio Core y Reglas de Dominio

*   **Procesamiento y Transformación (Físicas 2D Integradas):**  
    El sistema implementa una simulación cinemática básica basada en un marco de actualización continuo. La entidad principal (`Dinosaurio`) posee una regla de acumulación donde `velocidad_y += gravedad` en cada ciclo, actualizando su posición en `y`. Este procesamiento cuenta con una interrupción física rígida simulando el suelo (`y = ALTO - self.alto - 20`), limitando su transformación negativa.
*   **Gestión de Estado y Concurrencia (Memory Management & O(1) Cleanup):**  
    Una regla algorítmica crítica implementada es el control de fugas de memoria (Memory Leaks). Debido a que los obstáculos se generan ad infinitum, la regla estipula: `if lista_obstaculos.cabeza and lista_obstaculos.cabeza.dato.x < -50: lista_obstaculos.eliminar_al_inicio()`. Esto desvincula la referencia del primer nodo en complejidad de tiempo O(1), permitiendo que el *Garbage Collector* nativo limpie eficientemente el estado de la RAM.
*   **Validaciones y Dominio (Detección de Colisión AABB):**  
    La validación de finalización de juego se fundamenta en Axis-Aligned Bounding Boxes. A cada entidad se le adjunta un rectángulo (`pygame.Rect`). La regla de negocio evalúa la superposición de estas mallas vectoriales por cada frame activo a través de `dino.rect.colliderect(cactus.rect)`. Su confirmación muta irremisiblemente el estado maestro de juego (`jugando = False`).
*   **Patrón Generador para Exposición de Dominio Dinámico:**  
    En lugar de permitir exposición directa de memoria, la estructura de datos implementa un método mágico `__iter__` que provee un flujo (yield) de las entidades internas bajo demanda. Esto permite al consumidor superior encapsular el acceso de bajo nivel sin depender directamente del diseño estructurado con punteros `siguiente`.

## 5. Topología del Repositorio

```text
/ListaSimple-DinoGame
├── venv/                       # (Directorio) Entorno virtual aislado de ejecución.
├── __pycache__/                # (Directorio) Archivos intermedios precompilados de Python (.pyc).
├── Juego_Dino.py               # (Archivo) Main Controller, Game Loop, Físicas y Renderizado UI.
├── Lista_Simple.py             # (Archivo) Implementación Core de la Estructura de Datos (Linked List).
├── Nodo.py                     # (Archivo) Clase atómica que representa cada punto de memoria de la Lista.
└── requirements.txt            # (Archivo) Manifiesto de dependencias de empaquetado.
```

**Diccionario Estructural:**
*   **`Juego_Dino.py`:** Módulo de entrada y representación. Acopla el control lógico (Controller) y la vista visual (View/UI) gestionando estado visual, eventos del usuario y orquestando entidades.
*   **`Lista_Simple.py`:** Módulo de servicio de capa de datos. Totalmente agnóstico a la UI de visualización. Representa las responsabilidades de inserción, navegación modular y eliminación segura en base a punteros referenciales lógicos.
*   **`Nodo.py`:** Módulo de modelo puro en su mínima expresión. Contenedor binario responsable de almacenar una referencia al dato vivo (`Cactus`) y un puntero estático de memoria referenciado al elemento secuencial continuo.
*   **`requirements.txt` / `venv`:** Configuración declarativa de infraestructura garantizando la reproductibilidad del servidor/entorno.

## 6. Observaciones Técnicas y Calidad del Código

**Riesgos de Rendimiento y Cuellos de Botella:**
*   **Inserción O(N) Degradante:** La inserción de los cactus utiliza la función `insertar_al_final()`. Al carecer la `ListaSimple` de un puntero a la cola (`self.cola`), la rutina se ve forzada a iterar todos los obstáculos desde la cabeza al final cada vez que un cactus se crea. Aunque mitiga esto vaciando nodos inútiles, frente a variaciones exponenciales de tasa de *spawn*, resultaría en una saturación de la CPU.

**Deuda Técnica y Calidad de Desarrollo:**
*   **Magic Numbers (Valores Quemados):** El código está saturado de valores literales atados a lógica matemática cruda (Ej. `ALTO - self.alto - 20`, posiciones mágicas `-50`, divisor de puntuaciones `// 10`). Esto vuelve el mantenimiento y refactorización altamente riesgoso y frágil ante cambios de resolución global.
*   **Ausencia de Type Hinting:** El sistema ignora completamente la sintaxis de tipado moderno de Python (Ej. `def insertar_al_final(self, dato: Cactus) -> None:`), mermando la capacidad de analizadores estáticos como *Mypy* o la inferencia de IDEs robustos para prevenir excepciones del tipo *AttributeError* si se introdujera accidentalmente a la lista algo distinto a un `Cactus`.
*   **Alta Fricción / Acoplamiento Condicional:** Los modelos de `Cactus` y `Dinosaurio` tienen alta adherencia contextual a la variable global `ALTO`, haciendo que estas entidades de Dominio sean imposibles de desacoplar, exportar o unit-testear apropiadamente de manera isolada.

## 7. Instrucciones Obligatorias para la IA (System Guidelines)

> [!WARNING]
> **REGLA ESTRICTA DE EJECUCIÓN**
> "Siempre muéstrame el código actualizado y completo, indicándome los cambios realizados y/o modificados respecto a la versión anterior."
