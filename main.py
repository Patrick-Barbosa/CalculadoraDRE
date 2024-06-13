import streamlit as st
import pandas as pd

## CRIANDO UM DRE PARA CALCULAR O PAYBACK DE UMA FRANQUIA DE RESTAURANTE

def calcular(margemTarget, custosFixos, custosVariaveis, taxaIfood):
    #fatRange = range(int(custosFixos), 10000000, float(0.5))
    fat = custosFixos
    while True:
        valorIfood = taxaIfood*0.2*fat
        custosTotais = custosFixos + (custosVariaveis * fat) + valorIfood
        margemHipotese = (fat - custosTotais) / fat
        if abs(margemTarget - margemHipotese) < 0.0000004:
            break
        fat += 0.1
    return fat
    

def main():
    st.title("DRE Calculator")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write('Custos Fixos')
        investimentoInicial = st.number_input('Investimento Inicial')
        ocupacao = st.number_input('Ocupação')
        pessoal = st.number_input('Pessoal')
        utilidades = st.number_input('Utilidades')
        servicosGerais = st.number_input('Serviços Gerais')
        matEscritorio = st.number_input('Material de Escritorio')
        contador = st.number_input('Contador')

    with col2:
        st.write('Custos Variáveis')
        fundoMKT = st.number_input('% Fundo de MKT', value=2) / 100
        royalties = st.number_input('% Royalties', value=6) / 100
        mktLocal = st.number_input('% Mkt Local', value=0.2) / 100
        custoTicketCartao = st.number_input('% Custo Ticket e Cartao', value=2) / 100
        cmv = st.number_input('% CMV', value=34) / 100
        freteRegião = st.number_input('% Frete da Região', value=2) / 100
        taxaDelivery = st.number_input('% Taxa Delivery', value=18.75) / 100
        taxas = st.number_input('% Taxas', value=9) / 100

    
    if st.button("Calcular"):
        custosFixos = ocupacao + pessoal + utilidades + matEscritorio + servicosGerais + contador
        custosVariaveis = fundoMKT + royalties + mktLocal + custoTicketCartao + cmv + freteRegião + taxas
        Ponto_de_Equilíbrio = calcular(0, custosFixos, custosVariaveis, taxaDelivery)
        margemCinco = calcular(0.05, custosFixos, custosVariaveis, taxaDelivery)
        margemSete = calcular(0.07, custosFixos, custosVariaveis, taxaDelivery)
        margemDez= calcular(0.10, custosFixos, custosVariaveis, taxaDelivery)
        margemDoze = calcular(0.12, custosFixos, custosVariaveis, taxaDelivery)
        
        # Mostrar resultados
        st.write("Cenários de Faturamento:")
        st.write(f'Ponto de Equilíbrio: R$ {Ponto_de_Equilíbrio:.2f}')
        st.write(f'Margem 5%: R$ {margemCinco:.2f}')
        st.write(f'Margem 7%: R$ {margemSete:.2f}')
        st.write(f'Margem 10%: R$ {margemDez:.2f}')
        st.write(f'Margem 12%: R$ {margemDoze:.2f}')

if __name__ == "__main__":
    main()
