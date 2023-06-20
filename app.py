import streamlit as st
import calendar
import datetime

def calcular_gasto_passagens(valor_passagem_onibus, valor_passagem_ferry, valor_transporte_ferry, dias_utilizados_ferry, dias_utilizados_onibus, valor_carro_taxi, dias_utilizados_carro_taxi):
    dias_uteis = obter_dias_uteis()
    gasto_semanal = 0
    
    if dias_utilizados_onibus > 0:
        gasto_semanal += (valor_passagem_onibus * 2) * dias_utilizados_onibus
    
    if dias_utilizados_ferry > 0:
        gasto_semanal += (valor_passagem_ferry * 2 + valor_transporte_ferry) * dias_utilizados_ferry
    
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

def main():
    st.title("Calculadora de Gastos com Passagens")

    valor_passagem_onibus = st.number_input("Valor da passagem de ônibus (ida e volta): R$", min_value=0.0, value=0.0)
    dias_utilizados_onibus = st.number_input("Dias da semana utilizados no ônibus (ida e volta):", min_value=0, value=0)

    valor_passagem_ferry = st.number_input("Valor da passagem de ferry (ida e volta): R$", min_value=0.0, value=0.0)
    dias_utilizados_ferry = st.number_input("Dias da semana utilizando o ferry boat:", min_value=0, value=0)
    valor_transporte_ferry = st.number_input("Valor do transporte até o ferry (ida e volta): R$", min_value=0.0, value=0.0)

    valor_carro_taxi = st.number_input("Valor do carro/taxi (ida e volta): R$", min_value=0.0, value=0.0)
    dias_utilizados_carro_taxi = st.number_input("Dias da semana utilizando o carro/taxi:", min_value=0, value=0)

    if st.button("Calcular"):
        gasto_semanal, gasto_mensal = calcular_gasto_passagens(valor_passagem_onibus, valor_passagem_ferry, valor_transporte_ferry, dias_utilizados_ferry, dias_utilizados_onibus, valor_carro_taxi, dias_utilizados_carro_taxi)
        st.write(f"Gasto semanal: R$ {gasto_semanal:.2f}")
        st.write(f"Gasto mensal: R$ {gasto_mensal:.2f}")

if __name__ == "__main__":
    main()
