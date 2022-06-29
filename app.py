import streamlit as st

# Carga de de funcion que contiene el motor de calculo
from modulo_fuzzy import calcula_propina


def main():
	st.title("Fuzzy Logic")
	Calidad = st.slider('Calidad', 0, 10)
	Servicio = st.slider('Servicio', 0, 10)

	if st.button('Calcular propina'):
		valor = calcula_propina(Calidad,Servicio)
		st.text('El valor de la propina es: {}'.format(valor))

if __name__ == '__main__':
	main()