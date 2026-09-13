import streamlit as st

st.sidebar.title("Menú lateral")

modulos = st.sidebar.selectbox("Selecciones el modulo",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulos == "Home":
  st.title("PROYECTO 1")
  st.title("APLICACIÓN EN STREAMLIT")

  st.header("Elaborado por: Nilda Echevarria")
  st.subheader("Modulo 1")
  st.write("Información general del estudiante: ")
  st.write("Año: 2026")
  st.write("Breve descripción del proyecto: Este proyecto representa la primera aplicación práctica del módulo y permitirá evidenciar el uso de estructuras de datos, widgets, funciones, clases y lógica de programación en una interfaz interactiva.")
  st.write("Tecnologías utilizadas: ")

elif modulos == "Ejercicio 1":
  st.write("Te encuentas en la ventana de ejercicio 1")
  st.write("En este ejercicio se deberá desarrollar un pequeño módulo para registrar movimientos financieros en una lista vacía.")
  
  concepto = st.text_input("Ingresa el concepto del movimiento")
  tipoMovimiento = st.selectbox("Selecciones el tipo de movimiento",["Ingreso","Gasto"])
  valor = st.number_input("Ingresa el importe del movimiento", value=0)
  
  movimiento = list(range(concepto, tipoMovimiento, valor)

  st.write(movimiento)

elif modulos == "Ejercicio 2":
  st.write("Te encuentas en la ventana de ejercicio 2")

elif modulos == "Ejercicio 3":
  st.write("Te encuentas en la ventana de ejercicio 3")

else:
  st.write("Te encuentas en la ventana de ejercicio 4")


