import streamlit as st
import numpy as np
import pandas as pd
import libreria_funciones_proyecto1 as lf

st.sidebar.title("Menú lateral")

modulos = st.sidebar.selectbox("Selecciones el modulo",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulos == "Home":
  st.image("DMC.png", width = 300)
  st.title("PROYECTO 1")
  st.title("APLICACIÓN EN STREAMLIT")
  st.header("Elaborado por: Nilda Echevarria")
  st.subheader("Modulo 1")
  st.write("Información general del estudiante: ")
  st.write("Año: 2026")
  st.write("Breve descripción del proyecto: Este proyecto representa la primera aplicación práctica del módulo y permitirá evidenciar el uso de estructuras de datos, widgets, funciones, clases y lógica de programación en una interfaz interactiva.")
  st.write("Tecnologías utilizadas: GIT, Stramlit")


elif modulos == "Ejercicio 1":
  st.header("Te encuentas en la ventana del Ejercicio 1")
  st.write("En este ejercicio se deberá desarrollar un pequeño módulo para registrar movimientos financieros en una lista vacía.")
  
  if "movimientos" not in st.session_state:
    st.session_state.movimientos = []

  st.subheader("Formulario de Registra tu Movimientos")
  
  concepto = st.text_input("Ingresa el concepto del movimiento")
  tipo_Movimiento = st.selectbox("Selecciones el tipo de movimiento",["Ingreso","Gasto"],index=None,placeholder="Seleccione tipo de movimiento...")
  importe = float(st.number_input("Ingresa el importe del movimiento S/ ", value=0.00, min_value=0.0, step=0.5, format="%.2f"))
  
  if st.button("Guardar"):
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

elif modulos == "Ejercicio 2":
  st.header("Te encuentas en la ventana del Ejercicio 2")
  st.write("En este ejercicio se deberá crear un formulario para registrar información usando arreglos de NumPy. La idea es registrar productos, ventas o registros similares mediante widgets y botones.")
  
  if "inventario" not in st.session_state:
    st.session_state.inventario = np.empty((0, 5), dtype=object) # arreglo vacío de 2 dimensiones con 5 columnas
  
  st.subheader("Formulario de Registro de Productos")
  
  nombre = st.text_input("Ingresa el nombre del Producto")
  categoria = st.selectbox("Selecciona la categoría del producto", ["Abarrotes","Bebidas","Mascotas","Libreria"],index=None,placeholder="Seleccione la categoría...")
  precio = float(st.number_input("Ingresa el precio de cada producto (S/) ", value=0.00, min_value=0.0, step=0.5, format="%.2f"))
  cantidad = int(st.number_input("Cantidad", min_value=1, step=1))
  
  if st.button("Guardar"):
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
  st.subheader("Inventario")
  
  if st.session_state.inventario.shape[0] > 0:
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
  
      # Ejemplo de operaciones vectorizadas con NumPy sobre la matriz
      total_general = np.sum(st.session_state.inventario[:, 4].astype(float))
      st.metric("Venta Total Acumulada", f"S/ {total_general:,.2f}")
  
  else:
      st.info("Aún no hay productos registrados.")


elif modulos == "Ejercicio 3":
  st.header("Te encuentas en la ventana del Ejercicio 3")
  st.write("En este ejercicio se usara funciones desde una librería externa.")

  if "tiempo_transferencia" not in st.session_state:
    st.session_state.inventario = np.empty((0, 5), dtype=object) # arreglo vacío de 2 dimensiones con 5 columnas
  
  st.subheader("Formulario de registro para calcular el tiempo de transferencia de un archivo")
    
  tamano_archivo = float(st.number_input("Ingresa el tamaño del archivo (MB) ", value=0.00, min_value=0.0, step=0.1, format="%.2f"))
  velocidad = float(st.number_input("Ingresa la velocidad de transferencia (MBPS) ", value=0.00, min_value=0.0, step=0.1, format="%.2f"))

  if st.button("Ejecutar",type="primary"):
    resultado_tiempo =  lf.calcular_tiempo_transferencia_archivo(tamano_archivo,velocidad)
    st.write(f"El resultado de tu valor futuro de inversion es: {resultado_tiempo["tiempo_minutos"]}")
    st.write(f"El resultado de tu valor futuro de inversion es: {resultado_tiempo["tiempo_segundos"]}")

else:
  st.header("Te encuentas en la ventana de ejercicio 4")


