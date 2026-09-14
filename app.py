import streamlit as st
import numpy as np

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
  importe = float(st.number_input("Ingresa el importe del movimiento", value=0.00))
  
  if st.button("Guardar"):
    ingresos_total = 0
    gastos_total = 0
    if concepto:
      st.session_state.movimientos.append((concepto,tipo_Movimiento,importe))
      st.success(f"¡'{concepto}' agregado con éxito!")
        
    else:
      st.warning("Por favor, ingresa un movimiento antes de presionar el botón.")
  
  total = sum(
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
    
  st.subheader("Elementos guardados:")
  st.write(st.session_state.movimientos)
  st.write("Ingresos total: ", f"{ingresos_total:.2f}")
  st.write("Gastos total: ", f"{gastos_total:.2f}")
  st.write("Saldo total: ", f"{total:.2f}")

  if total>0:
    st.subheader("Flujo de caja: A FAVOR")
  else
    st.subheader("Flujo de caja: EN CONTRA")


elif modulos == "Ejercicio 2":
  st.write("Te encuentas en la ventana de ejercicio 2")


elif modulos == "Ejercicio 3":
  st.write("Te encuentas en la ventana de ejercicio 3")


else:
  st.write("Te encuentas en la ventana de ejercicio 4")


