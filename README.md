# 🦖 Dino Game - Lista Simple Enlazada

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-2.5+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)

Un clon educativo e interactivo del clásico juego del *Dinosaurio de Chrome*, construido en **Python** utilizando **Pygame**. El propósito central de este proyecto no es solo entretener, sino servir como un entorno de demostración técnica en tiempo real para visualizar y operar sobre una **Lista Simple Enlazada** (Singly Linked List) dinámica, gestionando la memoria y las físicas a 60 FPS.

---

## 📑 Tabla de Contenidos

- [Características Principales](#-características-principales)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Requisitos Previos](#-requisitos-previos)
- [Guía de Instalación](#-guía-de-instalación)
- [Ejecución y Uso](#-ejecución-y-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Contribución](#-contribución)
- [Licencia](#-licencia)

---

## ✨ Características Principales

*   🎮 **Motor Físico Integrado:** Cinemática 2D con simulación de gravedad continua y colisiones precisas (AABB Bounding Boxes).
*   🧠 **Estructura de Datos Abstrata:** Todo el motor de generación de obstáculos (Cactus) se almacena interactuando en RAM a través de una *Singly Linked List* creada desde cero.
*   🚀 **Gestor de Memoria Dinámico O(1):** Destrucción inteligente y liberación de referencias de nodos (`eliminar_al_inicio()`) en cuanto los obstáculos abandonan el límite visible de la pantalla, previniendo *Memory Leaks*.
*   🔄 **Renderizado a 60 FPS:** Integración síncrona perfecta entre el *Game Loop*, captura de eventos de hardware y renderizado de gráficos.
*   🎲 **Generación Procedural:** Instanciación estocástica de obstáculos a lo largo del paso del tiempo de supervivencia.

---

## 🛠 Tecnologías Utilizadas

| Categoría | Tecnología | Rol / Propósito |
| :--- | :--- | :--- |
| **Lenguaje Core** | `Python 3.x` | Lógica de Servidor, POO y modelado matemático. |
| **Motor Gráfico** | `Pygame` | Renderizado gráfico 2D, interfaz visual, captura de inputs. |
| **Arquitectura** | `Monolito + Game Loop` | Manejo sincrónico de eventos, *update* de estados y dibujado. |
| **Capa de Datos** | `Linked List` Custom | Abstracción para el almacenamiento en memoria y recolector de basura. |

---

## 📋 Requisitos Previos

Asegúrate de contar con las siguientes herramientas instaladas en tu sistema antes de proceder:

*   **Python 3.8** o superior.
*   **Git** (para clonar el repositorio).
*   **pip** (Administrador de paquetes de Python).

Puedes verificar tus versiones instaladas ejecutando los siguientes comandos en tu terminal:

```bash
python --version
pip --version
git --version
```

---

## 💻 Guía de Instalación

Sigue estos pasos para obtener una copia local y configurarla en menos de 2 minutos.

**1. Clona el repositorio:**
```bash
git clone [URL_DEL_REPOSITORIO]
```

**2. Navega al directorio del proyecto:**
```bash
cd ListaSimple-DinoGame
```

**3. Crea y activa un entorno virtual (Opcional pero Recomendado):**
*En Windows:*
```bash
python -m venv venv
.\venv\Scripts\activate
```
*En macOS/Linux:*
```bash
python3 -m venv venv
source venv/bin/activate
```

**4. Instala las dependencias necesarias:**
```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecución y Uso

Una vez instaladas las dependencias, inicializar el juego es muy sencillo. 

Para levantar el entorno interactivo, ejecuta el controlador principal:

```bash
python Juego_Dino.py
```

### 🎮 Controles Básicos

*   <kbd>Espacio</kbd> o <kbd>↑</kbd> (Flecha Arriba): **Saltar** (Evita el contacto con los obstáculos verdes para sobrevivir el mayor tiempo posible).
*   <kbd>X</kbd> (Botón de Ventana): **Cerrar el Juego**.

---

## 📁 Estructura del Proyecto

El repositorio persigue una separación clara entre las directivas del juego (*Controller/View*) y los algoritmos de Estructuras de Datos (*Model*).

```text
/ListaSimple-DinoGame
├── venv/                       # Entorno virtual aislado
├── Juego_Dino.py               # Main Entrypoint: Game Loop, UI, controles y Físicas
├── Lista_Simple.py             # Lógica estructural de la lista enlazada abstracta
├── Nodo.py                     # Unidad básica de memoria y contenedor de entidades
└── requirements.txt            # Manifiesto de dependencias (Ej. Pygame)
```

---

## 🤝 Contribución

¡Las contribuciones siempre son bienvenidas! Este proyecto fue pensado como un entorno de educación interactivo; si tienes en mente implementar mejoras como doble salto, *Type Hinting*, mejoras de O(N) a O(1) para las inserciones, o nuevos obstáculos, anímate.

1. Haz un **Fork** del proyecto.
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`).
3. Realiza tus commits (`git commit -m 'Añadir nueva Caracteristica'`).
4. Haz **Push** a la rama (`git push origin feature/NuevaCaracteristica`).
5. Abre un **Pull Request**.

---

## 📄 Licencia

Distribuido bajo la Licencia **MIT**. Consulta el archivo `LICENSE` (o asume sus directivas básicas de software libre) para más información.
