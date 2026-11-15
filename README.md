<!-- ================= HEADER ================= -->

<div align="center">

# 🎮 GUESS THE NUMBER

### A Bilingual Number Guessing Game Built with Python and Tkinter

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GUI-Tkinter-blue?style=for-the-badge" alt="Tkinter">
  <img src="https://img.shields.io/badge/Images-Pillow-green?style=for-the-badge" alt="Pillow">
  <img src="https://img.shields.io/badge/Version_Control-Git-orange?style=for-the-badge&logo=git&logoColor=white" alt="Git">
</p>

<p>
  <strong>Interactive gameplay · Bilingual interface · Three difficulty levels</strong>
</p>

</div>

---

# 🇺🇸 English Version

## 📌 Introduction

**Guess The Number** is an interactive desktop game developed in Python using Tkinter. The objective is to guess a randomly generated secret number within a limited number of attempts.

The game features a bilingual interface, allowing users to choose between English and Spanish before starting. It also includes three difficulty levels, an interactive graphical interface, and a custom Cyber Gaming visual theme.

This project was developed as part of my journey in software development, with a focus on Python programming, application logic, graphical interfaces, and version control.

## ✨ Features

- 🌎 **Bilingual Interface:** Choose between English and Spanish.
- 🎯 **Three Difficulty Levels:**
  - Easy: Numbers from 1 to 50.
  - Normal: Numbers from 1 to 100.
  - Hard: Numbers from 1 to 500.
- ❤️ **Limited Attempts:** Five attempts to find the secret number.
- 💡 **Interactive Hints:** Receive clues indicating whether your guess is too high or too low.
- ⚡ **Energy Indicators:** Visual bars display the remaining attempts.
- 🎨 **Custom Cyber Gaming Design:** Dark interface with neon-inspired visual elements.
- 🖼️ **Custom Background:** Personalized background image integrated into the game interface.
- 🔄 **Replay Option:** Start a new game after winning or losing.

## 🛠️ Technologies and Tools

| Technology | Purpose |
|:---|:---|
| Python 3 | Main programming language |
| Tkinter | Graphical user interface (GUI) |
| Pillow | Image loading and processing |
| Random | Secret number generation |
| Git | Version control |
| GitHub | Source code hosting and project management |
| Visual Studio Code | Development environment |

### 🤖 AI-Assisted Development

AI tools were used as development support throughout this project to assist with problem-solving, code explanations, debugging, and improving development efficiency.

AI was used as a complementary tool in the learning and development process, helping explore solutions and reinforce programming concepts.

## 🚀 Installation and Execution

Follow these steps to download and run the game on your computer.

### 1. Install Python

Download and install Python from its official website:

**[Download Python](https://www.python.org/downloads/)**

During installation on Windows, make sure to enable **Add Python to PATH**.

### 2. Download the Repository

Clone the repository using Git:

```bash
git clone https://github.com/santiurbdev/game_guess_the_number.git
```

Alternatively, open the GitHub repository, click **Code → Download ZIP**, and extract the downloaded folder.

### 3. Check the Project Files

Make sure both files are inside the same project folder:

```text
game_guess_the_number/
│
├── game.py
├── background.png
└── README.md
```

> **Important:** The `background.png` file is required for the custom game background to display correctly. Keep it in the same directory as `game.py`.

### 4. Install the Required Dependency

Open a terminal inside the project folder and run:

```bash
python -m pip install Pillow
```

Pillow is required to load and process the game's background image.

**Note:** Tkinter is included with most standard Python installations, so it usually does not require a separate pip installation.

If you want to verify that Tkinter is available, run:

```bash
python -m tkinter
```

A small test window should appear.

### 5. Run the Game

From the project directory, execute:

```bash
python game.py
```

On Windows, you can also use:

```bash
py game.py
```

The game window should open, allowing you to select your preferred language and difficulty level.

## 📁 Project Structure

| File | Description |
|:---|:---|
| `game.py` | Main game script containing the game logic, interface, language selection, and difficulty settings. |
| `background.png` | Custom background image used in the game's graphical interface. |
| `README.md` | Project documentation and installation instructions. |

## 🎯 Project Purpose

This project represents a practical exercise in Python development, focusing on:

- Programming logic and conditional statements.
- Random number generation.
- User input validation.
- Functions and application structure.
- Graphical user interface development.
- Working with external image resources.
- Version control using Git and GitHub.

---

# ES Versión en Español

## 📌 Introducción

**Adivina el Número** es un videojuego interactivo de escritorio desarrollado en Python utilizando Tkinter. Su objetivo consiste en descubrir un número secreto generado aleatoriamente dentro de una cantidad limitada de intentos.

El juego cuenta con una interfaz bilingüe que permite seleccionar entre español e inglés antes de comenzar. También incorpora tres niveles de dificultad, una interfaz gráfica interactiva y una estética visual personalizada inspirada en Cyber Gaming.

Este proyecto fue desarrollado como parte de mi proceso de formación en desarrollo de software, con énfasis en programación con Python, lógica de aplicaciones, interfaces gráficas y control de versiones.

## ✨ Características principales

- 🌎 **Interfaz bilingüe:** Permite seleccionar español o inglés.
- 🎯 **Tres niveles de dificultad:**
  - Fácil: números del 1 al 50.
  - Normal: números del 1 al 100.
  - Difícil: números del 1 al 500.
- ❤️ **Intentos limitados:** Cinco oportunidades para encontrar el número secreto.
- 💡 **Pistas interactivas:** Indica si el número ingresado es mayor o menor que el número secreto.
- ⚡ **Indicadores de energía:** Barras visuales que muestran los intentos disponibles.
- 🎨 **Diseño Cyber Gaming:** Interfaz oscura con elementos visuales inspirados en luces neón.
- 🖼️ **Fondo personalizado:** Imagen integrada en la interfaz gráfica del juego.
- 🔄 **Opción de reinicio:** Permite comenzar una nueva partida después de ganar o perder.

## 🛠️ Tecnologías y herramientas utilizadas

| Tecnología | Función |
|:---|:---|
| Python 3 | Lenguaje principal de programación |
| Tkinter | Desarrollo de la interfaz gráfica |
| Pillow | Carga y procesamiento de imágenes |
| Random | Generación del número secreto |
| Git | Control de versiones |
| GitHub | Alojamiento y gestión del código fuente |
| Visual Studio Code | Entorno de desarrollo |

### 🤖 Desarrollo asistido por inteligencia artificial

Durante el desarrollo de este proyecto se utilizaron herramientas de inteligencia artificial como apoyo para la resolución de problemas, explicación de código, depuración y optimización del tiempo de desarrollo.

La IA se utilizó como una herramienta complementaria dentro del proceso de aprendizaje, permitiendo explorar soluciones y reforzar conceptos de programación.

## 🚀 Instalación y ejecución

Sigue estos pasos para descargar y ejecutar el videojuego en tu computador.

### 1. Instalar Python

Descarga e instala Python desde su página oficial:

**[Descargar Python](https://www.python.org/downloads/)**

Durante la instalación en Windows, asegúrate de activar la opción **Add Python to PATH**.

### 2. Descargar el repositorio

Puedes clonar el repositorio utilizando Git:

```bash
git clone https://github.com/santiurbdev/game_guess_the_number.git
```

También puedes ingresar al repositorio en GitHub, seleccionar **Code → Download ZIP** y extraer la carpeta descargada.

### 3. Verificar los archivos del proyecto

Asegúrate de que ambos archivos estén dentro de la misma carpeta:

```text
game_guess_the_number/
│
├── game.py
├── background.png
└── README.md
```

> **Importante:** El archivo `background.png` es necesario para visualizar correctamente el fondo personalizado del videojuego. Debe permanecer en la misma carpeta que `game.py`.

### 4. Instalar la dependencia necesaria

Abre una terminal dentro de la carpeta del proyecto y ejecuta:

```bash
python -m pip install Pillow
```

Pillow es necesario para cargar y procesar la imagen de fondo del videojuego.

**Nota:** Tkinter viene incluido en la mayoría de las instalaciones estándar de Python, por lo que normalmente no necesita instalarse mediante pip.

Para comprobar que Tkinter está disponible, puedes ejecutar:

```bash
python -m tkinter
```

Debería aparecer una pequeña ventana de prueba.

### 5. Ejecutar el videojuego

Desde la terminal, ubicada en la carpeta del proyecto, ejecuta:

```bash
python game.py
```

En Windows también puedes utilizar:

```bash
py game.py
```

Se abrirá la ventana del videojuego, donde podrás seleccionar el idioma y el nivel de dificultad.

## 📁 Estructura del proyecto

| Archivo | Descripción |
|:---|:---|
| `game.py` | Script principal del videojuego. Contiene la lógica, interfaz, selección de idioma y niveles de dificultad. |
| `background.png` | Imagen personalizada utilizada como fondo de la interfaz gráfica del juego. |
| `README.md` | Documentación e instrucciones de instalación del proyecto. |

## 🎯 Objetivo del proyecto

Este proyecto representa un ejercicio práctico de desarrollo con Python, enfocado en fortalecer conocimientos sobre:

- Lógica de programación y estructuras condicionales.
- Generación de números aleatorios.
- Validación de datos ingresados por el usuario.
- Funciones y organización del código.
- Desarrollo de interfaces gráficas.
- Integración de recursos externos como imágenes.
- Control de versiones mediante Git y GitHub.

---

## 👨‍💻 Autor

<div align="center">

### Santiago Uribe Restrepo

**Software Development Student | Aspiring Backend Developer**

*Learning, building, and improving with every project.* /
*Aprendiendo, construyendo y mejorando con cada proyecto.*


</div>

---

<div align="center">

**⭐ Thanks for visiting this repository! | ¡Gracias por visitar este repositorio!**

</div>
