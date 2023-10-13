import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

data = pd.read_csv('esterilizacion_caninos_felinos.csv', delimiter=";")


st.header("Tabla esterilizacion caninos y felinos")
data

data = data.dropna()
st.header("Tabla con limpieza de datos")
data

#filtro 1
st.header("Filtro 1")
st.write ("Mostrar solo especie caninos")
filtro1 = data[data["especie"] != "F"]

st.dataframe(filtro1)

#filtro 2
st.header("Filtro 2")
st.write ("Mostrar las mascotas esterilizadas de raza LOBO SIBERIANO")

filtro2 = data[(data["raza"] == "LOBO SIBERIANO") & (data["especie"] == "C")]
st.dataframe(filtro2)


#filtro 3

st.header("Filtro 3")
st.write ("Mostrar todos las mascotas esterilizadas en comunas diferentes a castilla")
filtro3 = data[(data["comuna"]!="Castilla")]
st.dataframe(filtro3)

#filtro 4

st.header("Filtro 4")
st.write ("Mostrar todos las mascotas de genero hembra felinas esterilizadas en Guayabal")
filtro4 = data[(data["comuna"]=="Guayabal") &  (data["N_dosis"] == "H") &  (data["especie"] == "F")]
st.dataframe(filtro4)


#filtro 5
st.header("Filtro 5")
st.write ("Mostrar todos las mascotas de genero macho felinos esterilizadas en Aranjuez")
filtro5 = data[(data["comuna"]=="Aranjuez") &  (data["N_dosis"] == "M") &  (data["especie"] == "F")]
st.dataframe(filtro5)

#filtro 6
st.header("Filtro 6")
st.write ("Mostrar todos las mascotas de raza angora")
filtro6 = data[(data["raza"]=="Angora") ]
st.dataframe(filtro6)

#filtro 7
st.header("Filtro 7")
st.write ("Mostrar todos las mascotas de genero macho canino esterilizadas en barrio  Moravia")
filtro7 = data[(data["barrio"]=="Moravia") &  (data["N_dosis"] == "M") &  (data["especie"] == "C")]
st.dataframe(filtro7)

#filtro 8
st.header("Filtro 8")
st.write ("Mostrar todos las mascotas de raza labrador esterilizadas ")
filtro8 = data[(data["raza"]=="Labrador")]
st.dataframe(filtro8)

#filtro 9
st.header("Filtro 9")
st.write ("Mostrar todos las mascotas de raza criolla felino macho esterilizadas ")
filtro9 = data[(data["raza"]=="Siames")&  (data["N_dosis"] == "M") &  (data["especie"] == "F")]
st.dataframe(filtro9)

#filtro 10
st.header("Filtro 10")
st.write ("Mostrar todos las mascotas de raza Weimaraner hembras ")
filtro10 = data[(data["raza"]=="Weimaraner")&  (data["N_dosis"] == "H")]
st.dataframe(filtro10)



print(data.head())