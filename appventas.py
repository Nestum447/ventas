import pandas as pd
import streamlit as st
from db import init_db, add_sale, get_sales
from datetime import datetime


import os



init_db()

st.title('Carpio Entreprises Registro Diario de Ventas')

db_path = 'ventas.db'  # Cambia esto si usas un nombre diferente para la base de datos
st.write(f"La base de datos está guardada en: {os.path.abspath(db_path)}")
with st.form("sales_form"):
    date = st.date_input('Fecha', value=datetime.now().date())
    product = st.text_input('Producto')
    quantity = st.number_input('Cantidad', min_value=1, value=1)
    price = st.number_input('Precio', min_value=0.0, value=0.0, step=0.01)
    submitted = st.form_submit_button('Registrar Venta')

    if submitted:
        add_sale(date, product, quantity, price)
        st.success('Venta registrada correctamente!')

#st.subheader('Historial de Ventas')
#sales = get_sales()
#for sale in sales:
 #   st.write(f"Fecha: {sale[0]}, Producto: {sale[1]}, Cantidad: {sale[2]}, Precio: ${sale[3]:.2f}")

sales = get_sales()
if sales:
    # Crear un DataFrame con las ventas
    df = pd.DataFrame(sales, columns=['Fecha', 'Producto', 'Cantidad', 'Precio'])
    st.subheader('Historial de Ventas')
    
    # Mostrar el DataFrame como una tabla interactiva
    st.dataframe(df)
else:
    st.warning('No se han registrado ventas aún.')
    
