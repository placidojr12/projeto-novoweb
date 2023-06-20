import streamlit as st
import calendar
import datetime

def calcular_gasto_passagens(valor_passagem_onibus, valor_passagem_ferry, valor_carro_taxi, dias_utilizados_ferry, dias_utilizados_carro_taxi, dias_utilizados_onibus):
    dias_uteis = obter_dias_uteis()
    gasto_semanal = 0
    
    if dias_utilizados_onibus > 0:
        gasto_semanal += (valor_passagem_onibus * 2) * dias_utilizados_onibus
    
    if dias_utilizados_ferry > 0:
        gasto_semanal += (valor_passagem_ferry * 2) * dias_utilizados_ferry
    
    if dias_utilizados_carro_taxi > 0:
        gasto_semanal += (valor_carro_taxi * 2) * dias_utilizados_carro_taxi
    
    gasto_mensal = gasto_semanal * 4  # Multiplica o gasto semanal por 4 semanas
    return gasto_semanal, gasto_mensal

def obter_dias_uteis():
    dias_uteis = 0
    ano = datetime.date.today().year
    mes = datetime.date.today().month
    _, num_dias = calendar.monthrange(ano, mes)
    for dia in range(1, num_dias + 1):
        if calendar.weekday(ano, mes, dia) < 5:
            dias_uteis += 1
    return dias_uteis

titulo_label = st.title("Calculadora de Gastos com Passagens")
valor_passagem_onibus_label = st.markdown("Valor da passagem de ônibus (ida e volta):")
valor_passagem_onibus_entry = st.text_input("", key="passagem_onibus")

dias_utilizados_onibus_label = st.markdown("Dias da semana utilizados no ônibus (ida e volta):")
dias_utilizados_onibus_entry = st.number_input("", min_value=0, key="dias_onibus")

valor_passagem_ferry_label = st.markdown("Valor da passagem de ferry (ida e volta): R$")
valor_passagem_ferry_entry = st.text_input("", key="passagem_ferry")

dias_utilizados_ferry_label = st.markdown("Dias da semana utilizando o ferry boat:")
dias_utilizados_ferry_entry = st.number_input("", min_value=0, key="dias_ferry")

valor_carro_taxi_label = st.markdown("Valor do carro/taxi (ida e volta): R$")
valor_carro_taxi_entry = st.text_input("", key="carro_taxi")

dias_utilizados_carro_taxi_label = st.markdown("Dias da semana utilizando carro/taxi:")
dias_utilizados_carro_taxi_entry = st.number_input("", min_value=0, key="dias_carro_taxi")

calcular_button = st.button("Calcular")

resultado_semanal_label = st.empty()
resultado_mensal_label = st.empty()

def exibir_resultado():
    try:
        if valor_passagem_onibus_entry != "":
            valor_passagem_onibus = float(valor_passagem_onibus_entry)
        else:
            valor_passagem_onibus = 0.0
        
        if valor_passagem_ferry_entry != "":
            valor_passagem_ferry = float(valor_passagem_ferry_entry)
        else:
            valor_passagem_ferry = 0.0
        
        if valor_carro_taxi_entry != "":
            valor_carro_taxi = float(valor_carro_taxi_entry)
        else:
            valor_carro_taxi = 0.0
        
        dias_utilizados_ferry = int(dias_utilizados_ferry_entry)
        dias_utilizados_carro_taxi = int(dias_utilizados_carro_taxi_entry)
        dias_utilizados_onibus = int(dias_utilizados_onibus_entry)
        
        gasto_semanal, gasto_mensal = calcular_gasto_passagens(valor_passagem_onibus, valor_passagem_ferry, valor_carro_taxi, dias_utilizados_ferry, dias_utilizados_carro_taxi, dias_utilizados_onibus)
        
        resultado_semanal_label.text(f"Gasto semanal: R$ {gasto_semanal:.2f}")
        resultado_mensal_label.text(f"Gasto mensal: R$ {gasto_mensal:.2f}")
        
    except ValueError:
        st.error("Por favor, digite valores numéricos válidos.")

if calcular_button:
    exibir_resultado()
