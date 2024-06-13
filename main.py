import streamlit as st

## CRIANDO UM DRE PARA CALCULAR O PAYBACK DE UMA FRANQUIA DE RESTAURANTE

def calcular(margemTarget, custosFixos, custosVariaveis, taxaIfood):
    fat = custosFixos
    while True:
        valorIfood = taxaIfood*0.2*fat
        custosTotais = custosFixos + (custosVariaveis * fat) + valorIfood
        margemHipotese = (fat - custosTotais) / fat
        if abs(margemTarget - margemHipotese) < 0.0000004:
            break
        fat += 0.1
    return fat
    
def payback(Faturamento, Margem, InvestimentoInicial):
    return round((InvestimentoInicial / (Faturamento * Margem)), 2)

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
        fatMargemCinco = calcular(0.05, custosFixos, custosVariaveis, taxaDelivery)
        fatMargemSete = calcular(0.07, custosFixos, custosVariaveis, taxaDelivery)
        fatMargemDez= calcular(0.10, custosFixos, custosVariaveis, taxaDelivery)
        fatMargemDoze = calcular(0.12, custosFixos, custosVariaveis, taxaDelivery)
        
        col3, col4, col5 = st.columns(3)
        # Mostrar resultados
        with col3:
            st.write("Faturamento:")
            st.write(f'Ponto de Equilíbrio: R$ {Ponto_de_Equilíbrio:.1f}')
            st.write(f'Margem 5%: R$ {fatMargemCinco:.1f}')
            st.write(f'Margem 7%: R$ {fatMargemSete:.1f}')
            st.write(f'Margem 10%: R$ {fatMargemDez:.1f}')
            st.write(f'Margem 12%: R$ {fatMargemDoze:.1f}')
        with col4:
            st.write('Lucro Mensal:')
            st.write(f'P.E: N/A')
            st.write(f'5%: R$ {fatMargemCinco * 0.05:.0f}')
            st.write(f'7%: R$ {fatMargemSete * 0.07:.0f}')
            st.write(f'10%: R$ {fatMargemDez * 0.10:.0f}')
            st.write(f'12%: R$ {fatMargemDoze * 0.12:.0f}')
        with col5:
            st.write("Payback:")
            st.write('P.E: N/A')
            st.write(f'5%: {payback(fatMargemCinco, 0.05, investimentoInicial):.0f} Meses')
            st.write(f'7%: {payback(fatMargemSete, 0.07, investimentoInicial):.0f} Meses')
            st.write(f'10%: {payback(fatMargemDez, 0.10, investimentoInicial):.0f} Meses')
            st.write(f'12%: {payback(fatMargemDoze, 0.12, investimentoInicial):.0f} Meses')
            
if __name__ == "__main__":
    main()
