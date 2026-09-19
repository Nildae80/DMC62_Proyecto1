import streamlit as st
import numpy as np
import pandas as pd

from libreria_funciones_proyecto1 import Servidor

st.sidebar.title("Especialización en Python for Analytics")
imagen = st.sidebar.image("Python_logo.png", width=200)
modulos = st.sidebar.selectbox("Selecciones el modulo",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])
st.sidebar.image("DMC.png", width=150)

# Creamos 3 columnas (la central es más ancha para dar espacio)
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
  st.image("Python_logo.png", width=300)
  st.title("PROYECTO 1 📋")
  
if modulos == "Home":
  st.header("Proyecto Aplicado en Streamlit – Fundamentos de Programación")
  st.subheader("Elaborado por: Nilda Echevarria Meza")
  st.subheader("Módulo 1 – Python Fundamentals")
  st.write("Información general del estudiante: Ingeniero de Sistemas, con experiencia en el sector de mas de 5 años")
  st.write("Año: 2026")
  st.write("Breve descripción del proyecto: Este proyecto representa la primera aplicación práctica del módulo y permitirá evidenciar el uso de estructuras de datos, widgets, funciones, clases y lógica de programación en una interfaz interactiva.")
  st.write("Tecnologías utilizadas: GIT, Stramlit")

##EJERCICIO 1
elif modulos == "Ejercicio 1":
  st.header("Te encuentas en la ventana del Ejercicio 1")
  st.write("En este ejercicio se deberá desarrollar un pequeño módulo para registrar movimientos financieros en una lista vacía.")
  
  if "movimientos" not in st.session_state:
    st.session_state.movimientos = []

  st.subheader("Formulario de Registra tu Movimientos ✏️")
    
  concepto = st.text_input("Ingresa el concepto del movimiento")
  tipo_Movimiento = st.selectbox("Selecciones el tipo de movimiento",["Ingreso","Gasto"],index=None,placeholder="Seleccione tipo de movimiento...")
  importe = float(st.number_input("Ingresa el importe del movimiento S/ ", value=0.00, min_value=0.0, step=0.5, format="%.2f"))
  
  if st.button("Guardar ➕"):
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
    
    st.subheader("Listado de movimientos:")
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
  
  nombre = st.text_input("Ingresa el nombre del Producto")
  categoria = st.selectbox("Selecciona la categoría del producto", ["Abarrotes","Bebidas","Mascotas","Libreria"],index=None,placeholder="Seleccione la categoría...")
  precio = float(st.number_input("Ingresa el precio de cada producto (S/) ", value=0.00, min_value=0.0, step=0.5, format="%.2f"))
  cantidad = int(st.number_input("Cantidad", min_value=1, step=1))
  
  if st.button("Guardar ➕"):
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
      st.subheader("Inventario de productos")
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


##EJERCICIO 3
elif modulos == "Ejercicio 3":
  st.header("Te encuentras en la ventana del Ejercicio 3")
  st.write("En este ejercicio se usará funciones desde una librería externa.")
  
  # 1. Nombre de variable corregido en el session_state (2 columnas)
  if "tiempo" not in st.session_state:
    st.session_state.tiempo = np.empty((0, 2), dtype=object)
  
  st.subheader("Formulario de registro para calcular el tiempo de transferencia de un archivo con funciones")
  
  tipo_Funcion = st.selectbox("Seleccione el tipo de función",["Calcular tiempo de transferencia de archivo", "Otro"],index=None,placeholder="Seleccione tipo de movimiento...",)
  
  if tipo_Funcion == "Calcular tiempo de transferencia de archivo": 
    tamano_archivo = float(st.number_input("Ingresa el tamaño del archivo (MB)",value=0.00,min_value=0.0,step=0.1,format="%.2f",))
    velocidad = float(st.number_input("Ingresa la velocidad de transferencia (MBPS)",value=0.00,min_value=0.0,step=0.1,format="%.2f",))
  
    if st.button("Ejecutar", type="primary"):
      if velocidad <= 0 or tamano_archivo <= 0:
        st.error("El tamaño del archivo y la velocidad deben ser mayores a 0.")
      
      else:
        resultado_tiempo = lf.calcular_tiempo_transferencia_archivo(tamano_archivo, velocidad)
    
        minutos = resultado_tiempo["tiempo_minutos"]
        segundos = resultado_tiempo["tiempo_segundos"]

        if "tiempo" not in st.session_state or st.session_state.tiempo.shape[1] != 4:
          st.session_state.tiempo = np.empty((0, 4), dtype=object)
        
        nuevo_registro = np.array([[tamano_archivo, velocidad, minutos, segundos]], dtype=object)
        st.session_state.tiempo = np.vstack((st.session_state.tiempo, nuevo_registro))
    
        st.write(f"El tiempo de transferencia en: {minutos} minutos")
        st.write(f"El tiempo de transferencia en: {segundos} segundos")
        st.success("¡Cálculo realizado y guardado con éxito!")
  
  elif tipo_Funcion == "Otro":
    st.write("No se tiene implementado otras funciones")
  else:
    st.write("Elija una opción.")
  
  # Mostrar los datos guardados en una tabla
  if st.session_state.tiempo.shape[0] > 0:
    st.subheader("Tabla histórica de resultados obtenidos")
    df_mostrar = pd.DataFrame(st.session_state.tiempo,columns=["Tamaño (MB)","Velocidad (MBPS)","Tiempo en Minutos", "Tiempo en Segundos"],)
  
    # 3. Formato corregido para NumberColumn
    st.dataframe(df_mostrar,use_container_width=True,
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
  st.write("En este ejercicio se usara clases desde una librería externa con CRUD - Gestión e inspección de estado de servidores mediante la clase `Servidor`.")
 
  # 1. Inicialización en st.session_state (8 columnas)
  if "servidores" not in st.session_state or st.session_state.servidores.shape[1] != 8:
    st.session_state.servidores = np.empty((0, 8), dtype=object)
  
  # 2. Selección de acción CRUD mediante st.selectbox en el cuerpo principal
  opcion = st.selectbox("Seleccione la operación que desea realizar:",["Crear Servidor", "Ver Servidores", "Actualizar Servidor", "Eliminar Servidor"])
  st.divider()
  
  # CREAR
  if opcion == "Crear Servidor":
    st.subheader("Registrar un nuevo servidor")
  
    with st.form("form_crear_servidor", clear_on_submit=True):
      nombre = st.text_input("Nombre del Servidor")  
      tiempo_total = st.number_input("Tiempo Total de Operación (horas)",min_value=1.0,value=0.0,step=10.0,format="%.2f",)
      tiempo_caida = st.number_input("Tiempo de Caída (horas)",min_value=0.0,value=5.0,step=0.5,format="%.2f",)
      alm_total = st.number_input("Almacenamiento Total (GB)",min_value=1.0,value=1000.0,step=50.0,format="%.2f",)
      alm_usado = st.number_input("Almacenamiento Usado (GB)",min_value=0.0,value=400.0,step=10.0,format="%.2f",)
  
      btn_guardar = st.form_submit_button("Guardar Servidor", type="primary")
  
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
  
            st.success(f"Servidor '{nombre}' registrado con éxito.")
            st.rerun()
  
          except ValueError as err:
            st.error(f"Error de validación en la clase: {err}")
  
  # LEER
  elif opcion == "Ver Servidores":
      st.subheader("Listado de servidores")
  
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
  
              nuevo_t_total = st.number_input("Tiempo Total (h)",min_value=1.0,value=float(srv_actual[1]),step=10.0,format="%.2f",)
              nuevo_t_caida = st.number_input("Tiempo Caída (h)",min_value=0.0,value=float(srv_actual[2]),step=0.5,format="%.2f",)
              nuevo_alm_total = st.number_input("Almacenamiento Total (GB)",min_value=1.0,value=float(srv_actual[3]),step=50.0,format="%.2f",)
              nuevo_alm_usado = st.number_input("Almacenamiento Usado (GB)",min_value=0.0,value=float(srv_actual[4]),step=10.0,format="%.2f",)
  
              btn_actualizar = st.form_submit_button("Actualizar Registro", type="primary")
  
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
  
                      st.success("Servidor actualizado correctamente.")
                      st.rerun()
  
                  except ValueError as err:
                      st.error(f"Error de validación al actualizar: {err}")
      else:
          st.info("No hay servidores disponibles para actualizar.")
  
  # D - ELIMINAR
  elif opcion == "Eliminar Servidor":
      st.subheader("Eliminar servidor")
  
      if st.session_state.servidores.shape[0] > 0:
          nombres_del_srv = st.session_state.servidores[:, 0].tolist()
          srv_a_eliminar = st.selectbox("Seleccione el servidor a eliminar:", nombres_del_srv)
  
          if st.button("Eliminar Servidor", type="primary"):
              idx_del = np.where(st.session_state.servidores[:, 0] == srv_a_eliminar)[0][0]
  
              st.session_state.servidores = np.delete(st.session_state.servidores, idx_del, axis=0)
  
              st.success(f"Servidor '{srv_a_eliminar}' eliminado exitosamente.")
              st.rerun()
      else:
          st.info("No hay servidores disponibles para eliminar.")

