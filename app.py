import streamlit as st

st.title("PROYECTO 1")
st.title("APLICACIÓN EN STREAMLIT")
st.header("Elaboraro por: Nilda Echevarria")
st.subheader("Nombre del módulo: Modulo 1")
st.write("Información general del estudiante: ")
st.write("Año: 2026")
st.write("Breve descripción del proyecto: Este proyecto representa la primera aplicación práctica del módulo y permitirá evidenciar el uso de estructuras de datos, widgets, funciones, clases y lógica de programación en una interfaz interactiva.")
st.write("Tecnologías utilizadas: ")
st.sidebar.title("Menú lateral")

modulos = st.selectbox("Selecciones el modulo",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])
