import tkinter as tk
import random
import os
import sys


from PIL import Image, ImageTk, ImageOps

# ==========================================
# 1. CONFIGURACION GENERAL
# ==========================================

ventana = tk.Tk()
ventana.title("Guess the Number")
ventana.geometry("520x700")
ventana.resizable(False, False)

FONDO = "#080B18"
COLOR_TARJETA = "#0B1020"
COLOR_PRIMARIO = "#00E5FF"
COLOR_TEXTO = "#F8FAFC"
COLOR_SECUNDARIO = "#94A3B8"

NEON_MORADO = "#A855F7"
NEON_VERDE = "#39FF88"
NEON_ROJO = "#FF4566"

ventana.configure(bg=FONDO)

# ==========================================
# 2. TEXTOS EN ESPAÑOL E INGLES
# ==========================================

TEXTOS = {
    "es": {
        "titulo_ventana": "Adivina el Numero",
        "seleccion_titulo": "ADIVINA EL NUMERO",
        "seleccion_subtitulo": "SELECCIONA TU IDIOMA PARA CONTINUAR",
        "boton_espanol": "ESPAÑOL",
        "boton_ingles": "ENGLISH",
        "selector_dificultad": "ELIGE LA DIFICULTAD",
        "facil": "FACIL",
        "normal": "NORMAL",
        "dificil": "DIFICIL",
        "descripcion_facil": "Rango 1 - 50",
        "descripcion_normal": "Rango 1 - 100",
        "descripcion_dificil": "Rango 1 - 500",
        "rango": "RANGO DE NUMEROS: {} - {}",
        "error_rango": "¡Elige un numero entre {} y {}!",
        "titulo_juego": "ADIVINA EL NUMERO",
        "instrucciones": "INGRESA EL NUMERO • SUPERA EL JUEGO",
        "inicio": "¡Ingresa un numero para comenzar!",
        "intentos": "INTENTOS RESTANTES: {}",
        "error_numero": "¡Por favor, ingresa un numero valido!",
        "victoria": "¡GANASTE! ¡FELICIDADES!",
        "mayor": "¡Prueba con un numero mas alto!",
        "menor": "¡Prueba con un numero mas bajo!",
        "derrota": "¡FIN DEL JUEGO! EL NUMERO ERA: {}",
        "titulo_victoria": "¡VICTORIA!",
        "titulo_derrota": "¡JUEGO TERMINADO!",
        "adivinar": "▶  ADIVINAR AHORA",
        "reiniciar": "VOLVER A JUGAR",
        "pie": "Desarrollado con Python y Tkinter"
    },
    "en": {
        "titulo_ventana": "Guess the Number",
        "seleccion_titulo": "GUESS THE NUMBER",
        "seleccion_subtitulo": "SELECT YOUR LANGUAGE TO CONTINUE",
        "boton_espanol": "ESPAÑOL",
        "boton_ingles": "ENGLISH",
        "selector_dificultad": "CHOOSE YOUR DIFFICULTY",
        "facil": "EASY",
        "normal": "NORMAL",
        "dificil": "HARD",
        "descripcion_facil": "Range 1 - 50",
        "descripcion_normal": "Range 1 - 100",
        "descripcion_dificil": "Range 1 - 500",
        "rango": "NUMBER RANGE: {} - {}",
        "error_rango": "Choose a number between {} and {}!",
        "titulo_juego": "GUESS THE NUMBER",
        "instrucciones": "ENTER THE NUMBER • BEAT THE GAME",
        "inicio": "Enter a number to start!",
        "intentos": "ATTEMPTS REMAINING: {}",
        "error_numero": "Please enter a valid number!",
        "victoria": "YOU WIN! CONGRATULATIONS!",
        "mayor": "Try a higher number!",
        "menor": "Try a lower number!",
        "derrota": "GAME OVER! THE NUMBER WAS: {}",
        "titulo_victoria": "VICTORY!",
        "titulo_derrota": "GAME OVER!",
        "adivinar": "▶  GUESS NOW",
        "reiniciar": "PLAY AGAIN",
        "pie": "Developed with Python & Tkinter"
    }
}

idioma_actual = "en"
dificultad_actual = "normal"
rango_minimo = 1
rango_maximo = 100
numero_secreto = random.randint(rango_minimo, rango_maximo)
intentos = 5
juego_activo = True

# ==========================================
# 3. IMAGEN DE FONDO
# ==========================================

DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.join(DIRECTORIO_BASE, "background.png")

etiqueta_fondo = None

try:
    imagen_fondo = Image.open(ruta_imagen)
    imagen_fondo = ImageOps.fit(
        imagen_fondo,
        (520, 700),
        method=Image.Resampling.LANCZOS
    )
    foto_fondo = ImageTk.PhotoImage(imagen_fondo)

    etiqueta_fondo = tk.Label(
        ventana,
        image=foto_fondo,
        bd=0
    )
    etiqueta_fondo.place(x=0, y=0, relwidth=1, relheight=1)
    etiqueta_fondo.lower()

except FileNotFoundError:
    # El juego puede funcionar incluso si no encuentra la imagen.
    ventana.configure(bg=FONDO)

# ==========================================
# 4. FUNCIONES GENERALES
# ==========================================

def agregar_efecto_boton(boton, color_normal, color_hover):
    boton.bind(
        "<Enter>",
        lambda evento: boton.config(bg=color_hover)
    )
    boton.bind(
        "<Leave>",
        lambda evento: boton.config(bg=color_normal)
    )


def animar_victoria(paso=0):
    colores = [NEON_VERDE, COLOR_PRIMARIO, NEON_MORADO]

    if paso < 9:
        color = colores[paso % len(colores)]
        titulo.config(fg=color)
        etiqueta_resultado.config(fg=color)
        tarjeta_juego.config(highlightbackground=color)

        ventana.after(180, lambda: animar_victoria(paso + 1))
    else:
        titulo.config(fg=NEON_VERDE)
        etiqueta_resultado.config(fg=NEON_VERDE)
        tarjeta_juego.config(highlightbackground=NEON_VERDE)


def animar_derrota(paso=0):
    colores = [NEON_ROJO, NEON_MORADO]

    if paso < 8:
        color = colores[paso % len(colores)]
        titulo.config(fg=color)
        etiqueta_resultado.config(fg=color)
        tarjeta_juego.config(highlightbackground=color)

        ventana.after(180, lambda: animar_derrota(paso + 1))
    else:
        titulo.config(fg=NEON_ROJO)
        etiqueta_resultado.config(fg=NEON_ROJO)
        tarjeta_juego.config(highlightbackground=NEON_ROJO)


# ==========================================
# 5. PANTALLA DE SELECCION DE IDIOMA
# ==========================================

def limpiar_pantalla():
    """Elimina los elementos actuales sin borrar la imagen de fondo."""
    for widget in ventana.winfo_children():
        if widget is not etiqueta_fondo:
            widget.destroy()


def mostrar_selector_idioma():
    """Primera pantalla: permite elegir el idioma."""
    ventana.title("Guess the Number | Language")
    limpiar_pantalla()

    marco_idioma = tk.Frame(
        ventana, bg=COLOR_TARJETA, padx=30, pady=28,
        highlightthickness=2, highlightbackground="#087CA8"
    )
    marco_idioma.pack(padx=30, pady=125)

    tk.Label(
        marco_idioma, text="✦  CYBER GAME  ✦",
        font=("Bahnschrift", 10, "bold"),
        bg=COLOR_TARJETA, fg=NEON_MORADO
    ).pack(pady=(0, 12))

    tk.Label(
        marco_idioma, text="GUESS THE NUMBER",
        font=("Bahnschrift SemiBold", 25),
        bg=COLOR_TARJETA, fg=COLOR_PRIMARIO
    ).pack(pady=(0, 10))

    tk.Label(
        marco_idioma, text="SELECT YOUR LANGUAGE",
        font=("Bahnschrift", 10, "bold"),
        bg=COLOR_TARJETA, fg=COLOR_SECUNDARIO
    ).pack(pady=(0, 22))

    boton_espanol = tk.Button(
        marco_idioma, text="ES   |   ESPAÑOL",
        command=lambda: mostrar_selector_dificultad("es"),
        font=("Bahnschrift", 12, "bold"),
        bg=COLOR_PRIMARIO, fg=FONDO,
        activebackground="#7DF9FF", activeforeground=FONDO,
        relief="flat", cursor="hand2", width=20, pady=12, borderwidth=0
    )
    boton_espanol.pack(pady=8)
    agregar_efecto_boton(boton_espanol, COLOR_PRIMARIO, "#7DF9FF")

    boton_ingles = tk.Button(
        marco_idioma, text="EN   |   ENGLISH",
        command=lambda: mostrar_selector_dificultad("en"),
        font=("Bahnschrift", 12, "bold"),
        bg=NEON_MORADO, fg=COLOR_TEXTO,
        activebackground="#C084FC", activeforeground=COLOR_TEXTO,
        relief="flat", cursor="hand2", width=20, pady=12, borderwidth=0
    )
    boton_ingles.pack(pady=8)
    agregar_efecto_boton(boton_ingles, NEON_MORADO, "#C084FC")

    tk.Label(
        marco_idioma, text="PYTHON  •  TKINTER  •  CYBER GAMING",
        font=("Segoe UI", 8, "bold"),
        bg=COLOR_TARJETA, fg=COLOR_SECUNDARIO
    ).pack(pady=(22, 0))


def mostrar_selector_dificultad(idioma):
    """Segunda pantalla: permite elegir el nivel de dificultad."""
    global idioma_actual
    idioma_actual = idioma
    textos = TEXTOS[idioma_actual]

    limpiar_pantalla()
    ventana.title(textos["titulo_ventana"])

    marco_dificultad = tk.Frame(
        ventana, bg=COLOR_TARJETA, padx=30, pady=25,
        highlightthickness=2, highlightbackground="#087CA8"
    )
    marco_dificultad.pack(padx=30, pady=95)

    tk.Label(
        marco_dificultad, text="✦  GAME SETTINGS  ✦",
        font=("Bahnschrift", 10, "bold"),
        bg=COLOR_TARJETA, fg=NEON_MORADO
    ).pack(pady=(0, 12))

    tk.Label(
        marco_dificultad, text=textos["selector_dificultad"],
        font=("Bahnschrift SemiBold", 19),
        bg=COLOR_TARJETA, fg=COLOR_PRIMARIO
    ).pack(pady=(0, 20))

    opciones = [
        ("facil", "descripcion_facil", "easy", NEON_VERDE, "#86EFAC"),
        ("normal", "descripcion_normal", "normal", COLOR_PRIMARIO, "#7DF9FF"),
        ("dificil", "descripcion_dificil", "hard", NEON_MORADO, "#C084FC")
    ]

    for clave_nombre, clave_desc, nivel, color, hover in opciones:
        bloque = tk.Frame(marco_dificultad, bg=COLOR_TARJETA)
        bloque.pack(fill="x", pady=5)

        boton = tk.Button(
            bloque, text=textos[clave_nombre],
            command=lambda dificultad=nivel: iniciar_juego(idioma, dificultad),
            font=("Bahnschrift", 12, "bold"),
            bg=color, fg=FONDO if color != NEON_MORADO else COLOR_TEXTO,
            activebackground=hover, activeforeground=FONDO,
            relief="flat", cursor="hand2", width=20, pady=9, borderwidth=0
        )
        boton.pack()
        agregar_efecto_boton(boton, color, hover)

        tk.Label(
            bloque, text=textos[clave_desc],
            font=("Segoe UI", 9),
            bg=COLOR_TARJETA, fg=COLOR_SECUNDARIO
        ).pack(pady=(3, 0))

    boton_volver = tk.Button(
        marco_dificultad,
        text="←  " + ("VOLVER" if idioma == "es" else "BACK"),
        command=mostrar_selector_idioma,
        font=("Segoe UI", 9, "bold"),
        bg=COLOR_TARJETA, fg=COLOR_SECUNDARIO,
        activebackground=COLOR_TARJETA, activeforeground=COLOR_PRIMARIO,
        relief="flat", cursor="hand2"
    )
    boton_volver.pack(pady=(15, 0))


# 6. INICIAR EL JUEGO EN EL IDIOMA ELEGIDO
# ==========================================

def iniciar_juego(idioma, dificultad):
    global idioma_actual, dificultad_actual, rango_minimo, rango_maximo
    global numero_secreto, intentos, juego_activo
    global tarjeta_juego, titulo, etiqueta_resultado
    global etiqueta_intentos, barras_energia, entrada_numero
    global boton_adivinar, boton_reiniciar, pie_pagina

    idioma_actual = idioma
    dificultad_actual = dificultad
    textos = TEXTOS[idioma_actual]

    rangos = {
        "easy": (1, 50),
        "normal": (1, 100),
        "hard": (1, 500)
    }
    rango_minimo, rango_maximo = rangos[dificultad_actual]
    numero_secreto = random.randint(rango_minimo, rango_maximo)
    intentos = 5
    juego_activo = True

    ventana.title(textos["titulo_ventana"])

    # Quitar la pantalla de seleccion.
    for widget in ventana.winfo_children():
        if widget is not etiqueta_fondo:
            widget.destroy()

    # ======================================
    # TARJETA PRINCIPAL
    # ======================================

    tarjeta_juego = tk.Frame(
        ventana,
        bg=COLOR_TARJETA,
        padx=25,
        pady=20,
        highlightthickness=2,
        highlightbackground="#087CA8"
    )
    tarjeta_juego.pack(padx=30, pady=25)

    # ======================================
    # TITULO
    # ======================================

    titulo = tk.Label(
        tarjeta_juego,
        text=textos["titulo_juego"],
        font=("Bahnschrift SemiBold", 25),
        bg=COLOR_TARJETA,
        fg=COLOR_PRIMARIO
    )
    titulo.pack(pady=(15, 8))

    # ======================================
    # INSTRUCCIONES
    # ======================================

    instrucciones = tk.Label(
        tarjeta_juego,
        text=textos["instrucciones"],
        font=("Bahnschrift", 10, "bold"),
        bg=COLOR_TARJETA,
        fg=COLOR_SECUNDARIO
    )
    instrucciones.pack(pady=8)

    # ======================================
    # RANGO
    # ======================================

    etiqueta_rango = tk.Label(
        tarjeta_juego,
        text=textos["rango"].format(rango_minimo, rango_maximo),
        font=("Segoe UI", 10, "bold"),
        bg=COLOR_TARJETA,
        fg=COLOR_PRIMARIO
    )
    etiqueta_rango.pack(pady=12)

    # ======================================
    # CAMPO DE ENTRADA
    # ======================================

    entrada_numero = tk.Entry(
        tarjeta_juego,
        font=("Consolas", 22, "bold"),
        justify="center",
        width=15,
        relief="flat",
        bg=FONDO,
        fg=COLOR_TEXTO,
        insertbackground=COLOR_PRIMARIO,
        highlightthickness=2,
        highlightbackground="#263449",
        highlightcolor=COLOR_PRIMARIO
    )
    entrada_numero.pack(pady=15, ipady=12)

    # ======================================
    # RESULTADO
    # ======================================

    etiqueta_resultado = tk.Label(
        tarjeta_juego,
        text=textos["inicio"],
        font=("Segoe UI", 11, "bold"),
        bg=COLOR_TARJETA,
        fg=COLOR_TEXTO
    )
    etiqueta_resultado.pack(pady=12)

    # ======================================
    # INTENTOS
    # ======================================

    etiqueta_intentos = tk.Label(
        tarjeta_juego,
        text=textos["intentos"].format(intentos),
        font=("Segoe UI", 10, "bold"),
        bg=COLOR_TARJETA,
        fg=COLOR_SECUNDARIO
    )
    etiqueta_intentos.pack(pady=12)

    # ======================================
    # BARRAS DE ENERGIA
    # ======================================

    marco_energia = tk.Frame(tarjeta_juego, bg=COLOR_TARJETA)
    marco_energia.pack(pady=5)

    barras_energia = []

    for i in range(5):
        barra = tk.Frame(
            marco_energia,
            bg=NEON_VERDE,
            width=45,
            height=10
        )
        barra.pack(side="left", padx=5)
        barra.pack_propagate(False)
        barras_energia.append(barra)

    # ======================================
    # BOTON PARA ADIVINAR
    # ======================================

    boton_adivinar = tk.Button(
        tarjeta_juego,
        text=textos["adivinar"],
        command=comprobar_numero,
        font=("Bahnschrift", 14, "bold"),
        bg=COLOR_PRIMARIO,
        fg=FONDO,
        activebackground="#7DF9FF",
        activeforeground=FONDO,
        relief="flat",
        cursor="hand2",
        padx=35,
        pady=12,
        borderwidth=0
    )
    boton_adivinar.pack(pady=15)
    agregar_efecto_boton(boton_adivinar, COLOR_PRIMARIO, "#7DF9FF")

    # ======================================
    # BOTON PARA REINICIAR
    # ======================================

    boton_reiniciar = tk.Button(
        tarjeta_juego,
        text=textos["reiniciar"],
        command=reiniciar_juego,
        font=("Segoe UI", 10, "bold"),
        bg=NEON_MORADO,
        fg=COLOR_TEXTO,
        activebackground="#9333EA",
        activeforeground=COLOR_TEXTO,
        relief="flat",
        cursor="hand2",
        padx=30,
        pady=10,
        borderwidth=0
    )
    boton_reiniciar.pack_forget()
    agregar_efecto_boton(boton_reiniciar, NEON_MORADO, "#C084FC")

    # ======================================
    # PIE DE PAGINA
    # ======================================

    pie_pagina = tk.Label(
        tarjeta_juego,
        text=textos["pie"],
        font=("Segoe UI", 9),
        bg=COLOR_TARJETA,
        fg=COLOR_SECUNDARIO
    )
    pie_pagina.pack(side="bottom", pady=12)

    entrada_numero.focus_set()


# ==========================================
# 7. COMPROBAR EL NUMERO
# ==========================================

def comprobar_numero():
    global intentos, juego_activo

    if not juego_activo:
        return

    textos = TEXTOS[idioma_actual]

    try:
        numero_usuario = int(entrada_numero.get())
    except ValueError:
        etiqueta_resultado.config(
            text=textos["error_numero"],
            fg=NEON_ROJO
        )
        return

    if numero_usuario < rango_minimo or numero_usuario > rango_maximo:
        etiqueta_resultado.config(
            text=textos["error_rango"].format(rango_minimo, rango_maximo),
            fg=NEON_ROJO
        )
        return

    intentos -= 1

    # Actualizar las barras de energia.
    for i in range(5):
        if i < intentos:
            barras_energia[i].config(bg=NEON_VERDE)
        else:
            barras_energia[i].config(bg="#263449")

    # Victoria.
    if numero_usuario == numero_secreto:
        etiqueta_resultado.config(
            text=textos["victoria"],
            fg=NEON_VERDE
        )

        titulo.config(text=textos["titulo_victoria"])
        juego_activo = False
        boton_adivinar.config(state="disabled")
        boton_reiniciar.pack(before=pie_pagina, pady=5)
        animar_victoria()
        return

    # Pista: el numero secreto es mayor.
    elif numero_usuario < numero_secreto:
        etiqueta_resultado.config(
            text=textos["mayor"],
            fg=COLOR_PRIMARIO
        )

    # Pista: el numero secreto es menor.
    else:
        etiqueta_resultado.config(
            text=textos["menor"],
            fg=COLOR_PRIMARIO
        )

    etiqueta_intentos.config(
        text=textos["intentos"].format(intentos)
    )

    # Derrota.
    if intentos == 0 and juego_activo:
        etiqueta_resultado.config(
            text=textos["derrota"].format(numero_secreto),
            fg=NEON_ROJO
        )

        titulo.config(text=textos["titulo_derrota"])
        juego_activo = False
        boton_adivinar.config(state="disabled")
        boton_reiniciar.pack(before=pie_pagina, pady=5)
        animar_derrota()


# ==========================================
# 8. REINICIAR EL JUEGO
# ==========================================

def reiniciar_juego():
    global numero_secreto, intentos, juego_activo

    numero_secreto = random.randint(rango_minimo, rango_maximo)
    intentos = 5
    juego_activo = True

    textos = TEXTOS[idioma_actual]

    entrada_numero.delete(0, tk.END)

    etiqueta_resultado.config(
        text=textos["inicio"],
        fg=COLOR_TEXTO
    )

    titulo.config(
        text=textos["titulo_juego"],
        fg=COLOR_PRIMARIO
    )

    tarjeta_juego.config(highlightbackground="#087CA8")

    etiqueta_intentos.config(
        text=textos["intentos"].format(intentos)
    )

    for barra in barras_energia:
        barra.config(bg=NEON_VERDE)

    boton_adivinar.config(state="normal")
    boton_reiniciar.pack_forget()

    entrada_numero.focus_set()


# ==========================================
# 9. MOSTRAR LA PRIMERA PANTALLA
# ==========================================

mostrar_selector_idioma()

ventana.mainloop()
