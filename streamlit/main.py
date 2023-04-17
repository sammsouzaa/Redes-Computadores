import streamlit as st

st.title('supimpa!!')

st.write('Qual o seu nome? ')

nome = st.text_input('Digite aqui: ')

st.write(f"Seja bem vindo {nome} ao meu sitezinho")
