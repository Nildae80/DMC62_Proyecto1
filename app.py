import streamlit as st
import numpy as np
import pandas as pd

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
  st.write("Tecnologías utilizadas: ")


elif modulos == "Ejercicio 1":
  st.header("Te encuentas en la ventana de ejercicio 1")
  st.write("En este ejercicio se deberá desarrollar un pequeño módulo para registrar movimientos financieros en una lista vacía.")
  
  if "movimientos" not in st.session_state:
    st.session_state.movimientos = []
    
  concepto = st.text_input("Ingresa el concepto del movimiento")
  tipo_Movimiento = st.selectbox("Selecciones el tipo de movimiento",["Ingreso","Gasto"])
  importe = float(st.number_input("Ingresa el importe del movimiento", value=0.00, min_value=0.0, step=0.5, format="%.2f"))
  
  if st.button("Guardar"):
    ingresos_total = 0
    gastos_total = 0
    if concepto:
      st.session_state.movimientos.append((concepto,tipo_Movimiento,importe))
      st.success(f"¡'{concepto}' agregado con éxito!")
        
    else:
      st.warning("Por favor, ingresa un movimiento antes de presionar el botón.")

  #Saldo final
  saldo_total = sum(
    mov[2] if mov[1] == "Ingreso" else -mov[2] 
    for mov in st.session_state.movimientos
  )
  
  #sumar los ingresos
  ingresos_total = sum(
    mov[2] if mov[1] == "Ingreso" else 0
    for mov in st.session_state.movimientos
  )

  #sumar los gastos
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
  #st.write(st.session_state.movimientos) #lo mostramos como una lista
  #Mostrar con formato de decimales en una tabla con dataframe
  st.dataframe(
    df_movimientos,
    use_container_width=True,
    column_config={"Importe": st.column_config.NumberColumn("Importe", format="S/ %.2f")}
  )
  st.write("Ingresos total: ", f"{ingresos_total:.2f}")
  st.write("Gastos total: ", f"{gastos_total:.2f}")
  st.write("Saldo total: ", f"{saldo_total:.2f}")

  if saldo_total > 0:
    st.subheader("Flujo de caja: A FAVOR")
    st.metric(
      label="Flujo de caja", 
      value="A FAVOR", 
      delta="+12%"
    )
  else:
    st.subheader("Flujo de caja: EN CONTRA")


elif modulos == "Ejercicio 2":
  st.header("Te encuentas en la ventana de ejercicio 2")
  st.write("En este ejercicio se deberá crear un formulario para registrar información usando arreglos de NumPy. La idea es registrar productos, ventas o registros similares mediante widgets y botones.")
  
  if "inventario" not in st.session_state:
    st.session_state.inventario = np.empty((0, 5), dtype=object) # arreglo vacío de 2 dimensiones con 5 columnas
  
  st.subheader("Formulario de Registro de Productos")
  
  nombre = st.text_input("Nombre del Producto")
  categoria = st.selectbox("Categoría", ["Abarrotes","Bebidas","Mascotas","Libreria"])
  precio = st.number_input("Precio ($)", min_value=0.0, step=0.5, format="%.2f")
  cantidad = st.number_input("Cantidad", min_value=1, step=1)
  boton_guardar = st.form_submit_button("Registrar Producto")
  
  if boton_guardar:
    if nombre.strip() == "":
      st.error("Por favor ingresa un nombre para el producto.")
    else:
      total = precio * cantidad  # Calcular el total
      nuevo_registro = np.array([[nombre, categoria, precio, cantidad, total]], dtype=object)   # Crear una nueva fila para el arreglo
      st.session_state.inventario = np.vstack((st.session_state.inventario, nuevo_registro))  # Agregar la nueva fila al arreglo existente usando np.vstack
      st.success(f"Producto '{nombre}' registrado con éxito.")
  
  #Mostrar los datos guardados en una tabla
  st.subheader("Registros guardados (NumPy Array)")
  
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
      st.metric("Venta Total Acumulada", f"${total_general:,.2f}")
  
  else:
      st.info("Aún no hay productos registrados.")


elif modulos == "Ejercicio 3":
  st.header("Te encuentas en la ventana de ejercicio 3")


else:
  st.header("Te encuentas en la ventana de ejercicio 4")


