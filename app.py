import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Trabalho APS - Ricardo Roberto", layout="wide")

# Sidebar para navegação entre as 11 questões
st.sidebar.title("Lista de Exercícios 01")
opcao = st.sidebar.selectbox("Selecione a Questão", [f"Questão {i:02d}" for i in range(1, 12)])

# --- QUESTÃO 01: CONTA DE LUZ ---
if opcao == "Questão 01":
    st.header("⚡ Controle de Consumo de Energia")
    if 'luz' not in st.session_state: st.session_state.luz = []
    
    with st.form("luz_form"):
        d, k, v = st.date_input("Data"), st.number_input("KW"), st.number_input("Valor")
        if st.form_submit_button("Salvar"):
            st.session_state.luz.append({"Data": d, "KW": k, "Valor": v})
            
    if st.session_state.luz:
        df = pd.DataFrame(st.session_state.luz)
        st.table(df)
        st.write(f"**Média:** {df['KW'].mean():.2f} KW | **Máximo:** {df['KW'].max()} | **Mínimo:** {df['KW'].min()}")

# --- QUESTÃO 02: TEXTOSAÍDA ---
elif opcao == "Questão 02":
    st.header("🎨 Formatador de Texto")
    txt = st.text_input("Digite o texto", "Exemplo")
    col1, col2, col3 = st.columns(3)
    cor = col1.color_picker("Cor", "#000000")
    tam = col2.slider("Tamanho", 10, 70, 20)
    fmt = col3.selectbox("Fonte", ["Arial", "Courier", "Times New Roman"])
    st.markdown(f'<p style="color:{cor}; font-size:{tam}px; font-family:{fmt};">{txt}</p>', unsafe_allow_html=True)

# --- QUESTÃO 04: REMÉDIOS ---
elif opcao == "Questão 04":
    st.header("💊 Gestão de Medicamentos")
    nome = st.text_input("Remédio")
    inicio = st.time_input("Hora de Início")
    intervalo = st.number_input("Intervalo (horas)", 1, 24, 8)
    if st.button("Gerar Agenda"):
        proximo = datetime.combine(datetime.today(), inicio)
        for i in range(4): # Simula as próximas 4 doses
            st.write(f"Dose {i+1}: {proximo.strftime('%H:%M')}")
            proximo += timedelta(hours=intervalo)

# --- QUESTÃO 06: COMANDA PADARIA ---
elif opcao == "Questão 06":
    st.header("🥖 Comanda Eletrônica - Doce Sabor")
    if 'itens' not in st.session_state: st.session_state.itens = []
    with st.container():
        p = st.text_input("Produto")
        q = st.number_input("Qtd", 1)
        v = st.number_input("Preço Unit.", 0.0)
        if st.button("Add Item"):
            st.session_state.itens.append({"Item": p, "Qtd": q, "Total": q*v})
    if st.session_state.itens:
        df_c = pd.DataFrame(st.session_state.itens)
        st.dataframe(df_c)
        st.error(f"Total Geral: R$ {df_c['Total'].sum():.2f}")

# --- QUESTÃO 11: HERANÇA ---
elif opcao == "Questão 11":
    st.header("👥 Cadastro Pessoa / Funcionário")
    tipo = st.radio("Tipo", ["Funcionário", "Cliente"])
    nome = st.text_input("Nome")
    if tipo == "Funcionário":
        sal = st.number_input("Salário Atual", 1500.0)
        perc = st.slider("Reajuste (%)", 0, 50, 10)
        st.write(f"Novo Salário: R$ {sal * (1 + perc/100):.2f}")
    else:
        st.text_input("Profissão")
        st.success(f"Cliente {nome} cadastrado.")

else:
    st.info(f"Implementação da {opcao} seguindo a mesma lógica de classes e atributos.")
