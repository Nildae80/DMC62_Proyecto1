import streamlit as st
import numpy as np
import pandas as pd
import libreria_funciones_proyecto1 as lf
from librería_clases_proyecto1 import Servidor

st.set_page_config(
    page_title="Proyecto 1 | Python Analytics",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="expanded"
)

/* =========================================================
   PROYECTO 1 | ESTILOS CORPORATIVOS
   Paleta: Gris Ejecutivo + Azul Corporativo
   Archivo pensado para Streamlit
   ========================================================= */

/* ---------- PALETA ---------- */
:root {
    --bg-main: #F3F4F6;
    --bg-card: #FFFFFF;
    --bg-dark: #1F2937;
    --bg-dark-2: #111827;

    --blue: #2563EB;
    --blue-dark: #1D4ED8;
    --blue-light: #3B82F6;
    --blue-soft: #EFF6FF;

    --text: #111827;
    --text-secondary: #4B5563;
    --text-muted: #6B7280;

    --border: #D1D5DB;
    --border-light: #E5E7EB;

    --success: #059669;
    --warning: #D97706;
    --danger: #DC2626;

    --shadow-sm: 0 2px 8px rgba(15, 23, 42, 0.06);
    --shadow-md: 0 8px 24px rgba(15, 23, 42, 0.10);
    --shadow-blue: 0 8px 25px rgba(37, 99, 235, 0.18);

    --radius: 14px;
    --transition: 180ms ease;
}

/* ---------- FONDO GENERAL ---------- */
.stApp {
    background:
        radial-gradient(circle at 85% 5%, rgba(37, 99, 235, 0.06), transparent 28%),
        linear-gradient(135deg, #F8FAFC 0%, var(--bg-main) 100%);
    color: var(--text);
}

/* Evita que la barra superior robe protagonismo */
header[data-testid="stHeader"] {
    background: rgba(243, 244, 246, 0.82);
    backdrop-filter: blur(12px);
}

/* ---------- CONTENEDOR PRINCIPAL ---------- */
.main .block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
    animation: pageEnter 500ms ease both;
}

@keyframes pageEnter {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* ---------- TIPOGRAFÍA ---------- */
html, body, [class*="css"] {
    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
}

h1, h2, h3, h4 {
    color: var(--text) !important;
    font-weight: 750 !important;
    letter-spacing: -0.025em;
}

h1 {
    font-size: clamp(2rem, 4vw, 3rem) !important;
}

h2 {
    font-size: 1.65rem !important;
}

h3 {
    font-size: 1.25rem !important;
}

p, li, label {
    color: var(--text-secondary);
}

/* ---------- SIDEBAR ---------- */
section[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg, #1F2937 0%, #111827 100%);
    border-right: 1px solid rgba(255,255,255,0.08);
    box-shadow: 8px 0 30px rgba(15, 23, 42, 0.12);
}

section[data-testid="stSidebar"] > div {
    padding-top: 1.5rem;
}

section[data-testid="stSidebar"] * {
    color: #F9FAFB !important;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #FFFFFF !important;
}

section[data-testid="stSidebar"] img {
    border-radius: 12px;
    transition: transform var(--transition), filter var(--transition);
}

section[data-testid="stSidebar"] img:hover {
    transform: scale(1.025);
    filter: drop-shadow(0 0 12px rgba(59,130,246,0.35));
}

/* Selector del sidebar */
section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 10px !important;
    transition: all var(--transition);
}

section[data-testid="stSidebar"] div[data-baseweb="select"] > div:hover {
    border-color: rgba(59,130,246,0.8) !important;
    box-shadow: 0 0 0 3px rgba(59,130,246,0.12);
}

/* ---------- SELECTORES GENERALES ---------- */
div[data-baseweb="select"] > div {
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    background: #FFFFFF !important;
    transition: border-color var(--transition), box-shadow var(--transition);
}

div[data-baseweb="select"] > div:hover {
    border-color: var(--blue-light) !important;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.08);
}

/* ---------- INPUTS ---------- */
div[data-baseweb="input"] {
    border-radius: 10px !important;
}

div[data-baseweb="input"] > div {
    background: #FFFFFF !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    transition: all var(--transition);
}

div[data-baseweb="input"] > div:hover {
    border-color: #93C5FD !important;
}

div[data-baseweb="input"] > div:focus-within {
    border-color: var(--blue) !important;
    box-shadow:
        0 0 0 3px rgba(37,99,235,0.12),
        0 4px 14px rgba(37,99,235,0.08);
}

/* Texto de inputs */
div[data-baseweb="input"] input {
    color: var(--text) !important;
    font-weight: 500;
}

/* ---------- FORMULARIOS ---------- */
div[data-testid="stForm"] {
    background: rgba(255,255,255,0.94);
    border: 1px solid var(--border-light);
    border-radius: var(--radius);
    padding: 1.4rem;
    box-shadow: var(--shadow-sm);
    transition: transform var(--transition), box-shadow var(--transition);
}

div[data-testid="stForm"]:hover {
    box-shadow: var(--shadow-md);
}

/* ---------- BOTONES ---------- */
.stButton > button,
.stFormSubmitButton > button {
    background: linear-gradient(135deg, var(--blue), var(--blue-dark)) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.65rem 1.25rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.01em;
    box-shadow: 0 5px 14px rgba(37,99,235,0.20);
    transition:
        transform var(--transition),
        box-shadow var(--transition),
        filter var(--transition);
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    color: #FFFFFF !important;
    transform: translateY(-2px);
    box-shadow: 0 9px 22px rgba(37,99,235,0.28);
    filter: brightness(1.05);
}

.stButton > button:active,
.stFormSubmitButton > button:active {
    transform: translateY(0);
}

/* ---------- MÉTRICAS ---------- */
div[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid var(--border-light);
    border-left: 4px solid var(--blue);
    border-radius: 12px;
    padding: 1rem 1.1rem;
    box-shadow: var(--shadow-sm);
    transition: transform var(--transition), box-shadow var(--transition);
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    box-shadow: var(--shadow-blue);
}

div[data-testid="stMetricLabel"] {
    color: var(--text-secondary) !important;
    font-weight: 650 !important;
}

div[data-testid="stMetricValue"] {
    color: var(--text) !important;
    font-weight: 800 !important;
}

/* ---------- DATAFRAMES / TABLAS ---------- */
div[data-testid="stDataFrame"] {
    border: 1px solid var(--border-light);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: var(--shadow-sm);
    background: #FFFFFF;
}

/* ---------- ALERTAS ---------- */
div[data-testid="stAlert"] {
    border-radius: 11px !important;
    border: 1px solid var(--border-light) !important;
    box-shadow: var(--shadow-sm);
}

/* ---------- INFO ---------- */
div[data-testid="stAlert"][kind="info"] {
    background: var(--blue-soft);
}

/* ---------- DIVISORES ---------- */
hr {
    border: none !important;
    height: 1px !important;
    background: linear-gradient(
        90deg,
        transparent,
        #CBD5E1,
        transparent
    ) !important;
    margin: 1.5rem 0 !important;
}

/* ---------- IMÁGENES PRINCIPALES ---------- */
.main img {
    border-radius: 14px;
    transition: transform 250ms ease, filter 250ms ease;
}

.main img:hover {
    transform: translateY(-2px);
    filter: drop-shadow(0 10px 18px rgba(15,23,42,0.12));
}

/* ---------- CONTENEDORES / COLUMNAS ---------- */
div[data-testid="column"] {
    transition: transform var(--transition);
}

/* ---------- RADIO / CHECKBOX ---------- */
div[role="radiogroup"] label,
div[data-testid="stCheckbox"] label {
    color: var(--text-secondary) !important;
}

/* ---------- FOCUS ACCESIBLE ---------- */
button:focus-visible,
input:focus-visible,
textarea:focus-visible,
select:focus-visible {
    outline: 3px solid rgba(37,99,235,0.28) !important;
    outline-offset: 2px;
}

/* ---------- SCROLLBAR ---------- */
::-webkit-scrollbar {
    width: 9px;
    height: 9px;
}

::-webkit-scrollbar-track {
    background: #E5E7EB;
}

::-webkit-scrollbar-thumb {
    background: #9CA3AF;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--blue);
}

/* ---------- RESPONSIVE ---------- */
@media (max-width: 768px) {
    .main .block-container {
        padding: 1rem;
    }

    h1 {
        font-size: 2rem !important;
    }

    h2 {
        font-size: 1.4rem !important;
    }

    div[data-testid="stForm"] {
        padding: 1rem;
    }
}

/* ---------- REDUCCIÓN DE MOVIMIENTO ---------- */
@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
    }
}



st.sidebar.title("Especialización en Python for Analytics")
imagen = st.sidebar.image("Python_logo.png", width=200)
modulos = st.sidebar.selectbox("Selecciones el modulo",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])
st.sidebar.image("DMC.png", width=150)

# Creamos 3 columnas (la central es más ancha para dar espacio)
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
  st.image("Python_logo.png", width=300)
  st.title("PROYECTO 1 📋")
  st.markdown("---")

st.subheader("Proyecto Aplicado en Streamlit – Fundamentos de Programación")

if modulos == "Home":
  col1, col2 = st.columns(2)

  with col1:
      st.subheader("👤 Datos del Estudiante")
      st.markdown("**Nombre completo:** Nilda Echevarria Meza")
      st.markdown(
          "**Información general:** Ingeniero de Sistemas, con experiencia en el sector de mas de 5 años "
      )
        
  with col2:
      st.subheader("📚 Información del Curso")
      st.markdown("**Nombre del módulo:** Programación con Python y Streamlit")
      st.markdown("**Año:** 2026")
  
  st.markdown("---")
  
  # Breve descripción del proyecto
  st.subheader("📌 Descripción del Proyecto")
  st.info("""
  Esta aplicación fue desarrollada como parte de la evaluación práctica del módulo. Su objetivo principal es proveer una interfaz interactiva y fácil de usar para la gestión de registros mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar).
  
  **Principales funcionalidades:**
  - **Flujo de caja con listas:** Formulario dinámico Formulario de Registra tu Movimientos.
  - **Registro con NumPy, arrays y DataFrame:** Formulario dinámico Registro de Productos.
  - **Uso de funciones desde una librería externa:** Formulario dinámico de registro para calcular el tiempo de transferencia de un archivo con funciones
  - **Uso de clases desde una librería externa con CRUD:** Formulario dinámico para el monitoreo e inspección del estado, disponibilidad y uso de almacenamiento de servidores mediante Poo (Programación Orientada a Objetos).
  """)

  st.markdown("---")
  st.subheader("📌 Tecnologías utilizadas:")
  st.info("""
  GIT, Python, Streamlit, NumPy, Pandas.
  """)
  

##EJERCICIO 1
elif modulos == "Ejercicio 1":
  st.header("Te encuentas en la ventana del Ejercicio 1")
  st.write("En este ejercicio se deberá desarrollar un pequeño módulo para registrar movimientos financieros en una lista vacía.")
 
  if "movimientos" not in st.session_state:
    st.session_state.movimientos = []

  st.subheader("Formulario de Registra tu Movimientos ✏️")

  with st.form("form_movimientos", clear_on_submit=True):
    concepto = st.text_input("Ingresa el concepto del movimiento")
    tipo_Movimiento = st.selectbox("Selecciones el tipo de movimiento",["Ingreso","Gasto"],index=None,placeholder="Seleccione tipo de movimiento...")
    importe = float(st.number_input("Ingresa el importe del movimiento S/ ", value=0.00, min_value=0.0, step=0.5, format="%.2f"))
    btn_guardar = st.form_submit_button("Guardar ➕")
    
    if btn_guardar:
      ingresos_total = 0
      gastos_total = 0
  
      if concepto.strip() == "":
        st.warning("Por favor, ingresa un movimiento antes de presionar el botón.")
      elif tipo_Movimiento == None:
        st.warning("Por favor, ingresa el tipo de movimiento antes de presionar el botón.")
      elif importe == 0:
        st.warning("Por favor, ingresa el importe antes de presionar el botón.")
      elif importe < 0:
        st.warning("Por favor, el campo importe no puede ser menor a cero.")
      else:
        st.session_state.movimientos.append((concepto,tipo_Movimiento,importe))
        st.success(f"¡Movimiento '{concepto}' agregado con éxito!")  
      
    #Saldo total:
    saldo_total = sum(
      mov[2] if mov[1] == "Ingreso" else -mov[2] 
      for mov in st.session_state.movimientos
    )
    
    #Ingresos total:
    ingresos_total = sum(
      mov[2] if mov[1] == "Ingreso" else 0
      for mov in st.session_state.movimientos
    )
  
    #Gastos total:
    gastos_total = sum(
      mov[2] if mov[1] == "Gasto" else 0
      for mov in st.session_state.movimientos
    )
  
    if len(st.session_state.movimientos) > 0:
      #Creamos el DataFrame
      df_movimientos = pd.DataFrame(
        st.session_state.movimientos, 
        columns=["Concepto", "Tipo de Movimiento", "Importe"]
      )
      
      st.subheader("📊 Listado de movimientos:")
      #st.write(st.session_state.movimientos)        #Si lo queremos mostrar como una lista
      #Mostrar en una tabla con dataframe
      st.dataframe(
        df_movimientos,
        use_container_width=True,
        column_config={"Importe": st.column_config.NumberColumn("Importe", format="S/ %.2f")}
      )
      st.write("Ingresos total: ", f"{ingresos_total:.2f}")
      st.write("Gastos total: ", f"{gastos_total:.2f}")
      st.write("Saldo total: ", f"{saldo_total:.2f}")
    
      if saldo_total > 0:
        st.metric(
          label="Flujo de caja", 
          value="A FAVOR", 
          delta="+"
        )
      elif saldo_total < 0:
        st.metric(
          label="Flujo de caja", 
          value="EN CONTRA", 
          delta="-"
        )
      else:
        st.metric(
          label="Flujo de caja", 
          value="CUADRADO", 
          delta="+"
        )
    else:
      st.info("Aún no hay movimientos registrados.")


##EJERCICIO 2
elif modulos == "Ejercicio 2":
  st.header("Te encuentas en la ventana del Ejercicio 2")
  st.write("En este ejercicio se deberá crear un formulario para registrar información usando arreglos de NumPy. La idea es registrar productos, ventas o registros similares mediante widgets y botones.")
  
  if "inventario" not in st.session_state:
    st.session_state.inventario = np.empty((0, 5), dtype=object) # arreglo vacío de 2 dimensiones con 5 columnas
  
  st.subheader("Formulario de Registro de Productos ✏️")

  with st.form("form_inventario", clear_on_submit=True):
    nombre = st.text_input("Ingresa el nombre del Producto")
    categoria = st.selectbox("Selecciona la categoría del producto", ["Abarrotes","Bebidas","Mascotas","Libreria"],index=None,placeholder="Seleccione la categoría...")
    precio = float(st.number_input("Ingresa el precio de cada producto (S/) ", value=0.00, min_value=0.0, step=0.5, format="%.2f"))
    cantidad = int(st.number_input("Cantidad", min_value=1, step=1))
    btn_guardar = st.form_submit_button("Guardar ➕")
    
    if btn_guardar:
      if nombre.strip() == "":
        st.warning("Por favor, ingresa un producto antes de presionar el botón.")
      elif categoria == None:
        st.warning("Por favor, ingresa el tipo de categoría antes de presionar el botón.")
      elif precio == 0:
        st.warning("Por favor, ingresa el precio del producto antes de presionar el botón.")
      elif precio < 0:
        st.warning("Por favor, el campo precio del producto no puede ser menor a cero.")
      elif cantidad == 0:
        st.warning("Por favor, ingresa la cantidad de productos antes de presionar el botón.")
      elif precio < 0:
        st.warning("Por favor, el campo cantidad del producto no puede ser menor a cero.")
      else:
        total = precio * cantidad  # Calcular el total
        nuevo_registro = np.array([[nombre, categoria, precio, cantidad, total]], dtype=object)   # Crear una nueva fila para el arreglo
        st.session_state.inventario = np.vstack((st.session_state.inventario, nuevo_registro))  # Agregar la nueva fila al arreglo existente usando np.vstack
        st.success(f"¡Producto '{nombre}' agregado con éxito!.")
    
    #Mostrar los datos guardados en una tabla
    if st.session_state.inventario.shape[0] > 0:
        st.subheader("📦 Inventario de productos")
        # Convertimos el arreglo de NumPy a DataFrame solo para visualizarlo en la UI
        df_mostrar = pd.DataFrame(
            st.session_state.inventario,
            columns=["Producto", "Categoría", "Precio", "Cantidad", "Total"],
        )
    
        st.dataframe(
            df_mostrar,
            use_container_width=True,
            column_config={
                "Precio": st.column_config.NumberColumn("Precio", format="S/ %.2f"),
                "Total": st.column_config.NumberColumn("Total", format="S/ %.2f"),
            },
        )  
        total_general = np.sum(st.session_state.inventario[:, 4].astype(float))
        st.metric("Importe Total Acumulada", f"S/ {total_general:,.2f}")  
    else:
        st.info("Aún no hay productos registrados.")
  

elif modulos == "Ejercicio 3":
    st.header("Te encuentras en la ventana del Ejercicio 3")
    st.write("En este ejercicio se usará funciones desde una librería externa.")
    
    if "tiempo" not in st.session_state or st.session_state.tiempo.shape[1] != 4:
        st.session_state.tiempo = np.empty((0, 4), dtype=object)
    
    st.subheader("Formulario de registro para calcular el tiempo de transferencia de un archivo con `funciones` ✏️")

    tipo_Funcion = st.selectbox(
        "Seleccione el tipo de función",
        ["Calcular tiempo de transferencia de archivo", "Otro"],
        index=None,
        placeholder="Seleccione tipo de opción..."
    )

    if tipo_Funcion == "Calcular tiempo de transferencia de archivo":
        with st.form("form_funcion", clear_on_submit=True):
            tamano_archivo = float(st.number_input(
                "Ingresa el tamaño del archivo (MB)",
                value=0.00, min_value=0.0, step=0.1, format="%.2f"
            ))
            velocidad = float(st.number_input(
                "Ingresa la velocidad de transferencia (MBPS)",
                value=0.00, min_value=0.0, step=0.1, format="%.2f"
            ))
            
            btn_guardar = st.form_submit_button("Guardar ➕")

            if btn_guardar:
                if velocidad <= 0 or tamano_archivo <= 0:
                    st.error("El tamaño del archivo y la velocidad deben ser mayores a 0.")
                else:
                    # 1. Llamada a la función externa
                    resultado_tiempo = lf.calcular_tiempo_transferencia_archivo(tamano_archivo, velocidad)
                    minutos = resultado_tiempo["tiempo_minutos"]
                    segundos = resultado_tiempo["tiempo_segundos"]

                    # 2. Guardar dentro del session_state (dentro del botón)
                    nuevo_registro = np.array([[tamano_archivo, velocidad, minutos, segundos]], dtype=object)
                    st.session_state.tiempo = np.vstack((st.session_state.tiempo, nuevo_registro))
                    
                    st.success(f"Cálculo exitoso: {minutos} min, {segundos} seg.")
                    st.info("¡Cálculo realizado y guardado con éxito!", icon="✅")
                    #st.rerun()

    elif tipo_Funcion == "Otro":
        st.info("No se tiene implementado otras funciones por el momento.")
    else:
        st.warning("Elija una opción del menú desplegable para continuar.")

    # --- TABLA HISTÓRICA (Fuera del formulario y de los if de selección) ---
    if st.session_state.tiempo.shape[0] > 0:
        st.subheader("⚡ Tabla histórica de resultados obtenidos")
        df_mostrar = pd.DataFrame(
            st.session_state.tiempo,
            columns=["Tamaño (MB)", "Velocidad (MBPS)", "Tiempo en Minutos", "Tiempo en Segundos"]
        )
        st.dataframe(
            df_mostrar,
            use_container_width=True,
            column_config={
                "Tamaño (MB)": st.column_config.NumberColumn("Tamaño (MB)", format="%.2f MB"),
                "Velocidad (MBPS)": st.column_config.NumberColumn("Velocidad (MBPS)", format="%.2f MBPS"),
                "Tiempo en Minutos": st.column_config.NumberColumn("Tiempo (min)", format="%.2f min"),
                "Tiempo en Segundos": st.column_config.NumberColumn("Tiempo (seg)", format="%.2f seg"),
            },
        )
    else:
        st.info("Aún no hay ejecuciones registradas.")


##EJERCICIO 4
else:
  st.header("Te encuentas en la ventana de ejercicio 4")
  st.write("En este ejercicio se usara clases desde una librería externa con CRUD - Gestión e inspección de estado de servidores mediante la clase `Servidor`.✏️")
 
  # 1. Inicialización en st.session_state (8 columnas)
  if "servidores" not in st.session_state or st.session_state.servidores.shape[1] != 8:
    st.session_state.servidores = np.empty((0, 8), dtype=object)
  
  # 2. Selección de acción CRUD mediante st.selectbox en el cuerpo principal
  opcion = st.selectbox("Seleccione la operación que desea realizar:",["Crear un nuevo Servidor", "Ver listado de Servidores", "Actualizar informacion del Servidor", "Eliminar un Servidor"])
  st.divider()
  
  # CREAR
  if opcion == "Crear un nuevo Servidor":
    st.subheader("Registrar un nuevo servidor")
  
    with st.form("form_crear_servidor", clear_on_submit=True):
      nombre = st.text_input("Nombre del Servidor")  
      tiempo_total = float(st.number_input("Tiempo Total de Operación (horas)",min_value=0.0,value=0.0,step=10.0,format="%.2f",))
      tiempo_caida = st.number_input("Tiempo de Caída (horas)",min_value=0.0,value=0.0,step=0.5,format="%.2f",)
      alm_total = st.number_input("Almacenamiento Total (GB)",min_value=0.0,value=0.0,step=50.0,format="%.2f",)
      alm_usado = st.number_input("Almacenamiento Usado (GB)",min_value=0.0,value=0.0,step=10.0,format="%.2f",)
  
      btn_guardar = st.form_submit_button("Guardar ➕")
  
      if btn_guardar:
        if not nombre.strip():
          st.error("Por favor ingrese un nombre para el servidor.")
        else:
          try:
            # Instanciación de la clase externa
            srv = Servidor(nombre=nombre.strip(),tiempo_total_h=tiempo_total,tiempo_caida_h=tiempo_caida,almacenamiento_total_gb=alm_total,almacenamiento_usado_gb=alm_usado,)
            resumen = srv.resumen()
            nueva_fila = np.array([[srv.nombre,srv.tiempo_total_h,srv.tiempo_caida_h,srv.almacenamiento_total_gb,srv.almacenamiento_usado_gb,resumen["disponibilidad_pct"],resumen["uso_almacenamiento_pct"],resumen["estado"],]],dtype=object,)
  
            st.session_state.servidores = np.vstack((st.session_state.servidores, nueva_fila))
            st.success(f"Servidor '{nombre}' registrado con éxito.", icon="✅")
            #st.rerun()            
  
          except ValueError as err:
            st.error(f"Error de validación en la clase: {err}")
           
  # LEER
  elif opcion == "Ver listado de Servidores":
      st.subheader("🖥️ Listado de servidores")
  
      if st.session_state.servidores.shape[0] > 0:
          df_servidores = pd.DataFrame(st.session_state.servidores,
              columns=["Servidor","Tiempo Total (h)","Tiempo Caída (h)","Almacenamiento Total (GB)","Almacenamiento Usado (GB)","Disponibilidad (%)","Uso Almacenamiento (%)","Estado",],)
  
          st.dataframe(df_servidores,use_container_width=True,
              column_config={
                  "Disponibilidad (%)": st.column_config.NumberColumn(format="%.2f %%"),
                  "Uso Almacenamiento (%)": st.column_config.NumberColumn(format="%.2f %%"),
                  "Tiempo Total (h)": st.column_config.NumberColumn(format="%.2f h"),
                  "Tiempo Caída (h)": st.column_config.NumberColumn(format="%.2f h"),
                  "Almacenamiento Total (GB)": st.column_config.NumberColumn(format="%.2f GB"),
                  "Almacenamiento Usado (GB)": st.column_config.NumberColumn(format="%.2f GB"),
              },
          )
      else:
          st.info("Aún no hay servidores registrados.")
  
  # ACTUALIZAR
  elif opcion == "Actualizar informacion del Servidor":
      st.subheader("Modificar datos de un servidor existente")
  
      if st.session_state.servidores.shape[0] > 0:
          nombres_servidores = st.session_state.servidores[:, 0].tolist()
          servidor_seleccionado = st.selectbox("Seleccione el servidor a editar:", nombres_servidores)
  
          idx = np.where(st.session_state.servidores[:, 0] == servidor_seleccionado)[0][0]
          srv_actual = st.session_state.servidores[idx]
  
          with st.form("form_actualizar_servidor"):
              nuevo_nombre = st.text_input("Nombre", value=str(srv_actual[0]))
  
              nuevo_t_total = st.number_input("Tiempo Total (h)",min_value=0.0,value=float(srv_actual[1]),step=10.0,format="%.2f",)
              nuevo_t_caida = st.number_input("Tiempo Caída (h)",min_value=0.0,value=float(srv_actual[2]),step=0.5,format="%.2f",)
              nuevo_alm_total = st.number_input("Almacenamiento Total (GB)",min_value=0.0,value=float(srv_actual[3]),step=50.0,format="%.2f",)
              nuevo_alm_usado = st.number_input("Almacenamiento Usado (GB)",min_value=0.0,value=float(srv_actual[4]),step=10.0,format="%.2f",)
  
              btn_actualizar = st.form_submit_button("Actualizar Registro")
  
              if btn_actualizar:
                  try:
                      srv_editado = Servidor(
                          nombre=nuevo_nombre.strip(),
                          tiempo_total_h=nuevo_t_total,
                          tiempo_caida_h=nuevo_t_caida,
                          almacenamiento_total_gb=nuevo_alm_total,
                          almacenamiento_usado_gb=nuevo_alm_usado,
                      )
  
                      resumen_editado = srv_editado.resumen()
  
                      st.session_state.servidores[idx] = [
                          srv_editado.nombre,
                          srv_editado.tiempo_total_h,
                          srv_editado.tiempo_caida_h,
                          srv_editado.almacenamiento_total_gb,
                          srv_editado.almacenamiento_usado_gb,
                          resumen_editado["disponibilidad_pct"],
                          resumen_editado["uso_almacenamiento_pct"],
                          resumen_editado["estado"],
                      ]
  
                      st.success("Servidor actualizado correctamente.", icon="✅")
                      #st.rerun()
  
                  except ValueError as err:
                      st.error(f"Error de validación al actualizar: {err}")
      else:
          st.info("No hay servidores disponibles para actualizar.")
  
  # ELIMINAR
  elif opcion == "Eliminar un Servidor":
      st.subheader("Eliminar servidor")
  
      if st.session_state.servidores.shape[0] > 0:
          nombres_del_srv = st.session_state.servidores[:, 0].tolist()
          srv_a_eliminar = st.selectbox("Seleccione el servidor a eliminar:", nombres_del_srv)
  
          if st.button("Eliminar Servidor"):
              srv_elim = np.where(st.session_state.servidores[:, 0] == srv_a_eliminar)[0][0]  
              st.session_state.servidores = np.delete(st.session_state.servidores, srv_elim, axis=0)  
              st.success(f"Servidor '{srv_a_eliminar}' eliminado exitosamente.", icon="✅")
              #st.rerun()
      else:
          st.info("No hay servidores disponibles para eliminar.")

