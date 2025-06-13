import streamlit as st

# Inicializa banca
if "banca" not in st.session_state:
    st.session_state.banca = 100.00

st.title("💡 Calculadora de Aposta Inteligente")

# Exibe banca
st.markdown(f"### 💰 Banca atual: R$ {st.session_state.banca:.2f}")

# Entradas do usuário
odd = st.number_input("📈 Odd da aposta", min_value=1.01, step=0.01)
prob_estimada = st.slider("🔮 Sua chance da aposta bater (%)", 1, 100, 60)
percentual = st.slider("📊 % da banca a apostar", 1, 100, 5)

# Botão de calcular
if st.button("💸 Calcular Aposta"):
    try:
        prob = prob_estimada / 100
        odd_justa = 1 / prob
        texto_valor = "✅ Aposta de valor!" if odd > odd_justa else "❌ Odd abaixo do justo."

        stake = st.session_state.banca * (percentual / 100)
        retorno = stake * odd
        lucro = retorno - stake

        st.success(f"""
        🎯 **Stake sugerida**: R$ {stake:.2f}  
        💸 **Retorno total**: R$ {retorno:.2f}  
        💰 **Lucro possível**: R$ {lucro:.2f}  
        {texto_valor}
        """)
    except:
        st.error("Erro nos cálculos. Verifique os dados.")

# Botões de resultado
col1, col2 = st.columns(2)

with col1:
    if st.button("✅ Ganhei"):
        stake = st.session_state.banca * (percentual / 100)
        ganho = stake * (odd - 1)
        st.session_state.banca += ganho
        st.success(f"Banca atualizada: +R$ {ganho:.2f}")

with col2:
    if st.button("❌ Perdi"):
        stake = st.session_state.banca * (percentual / 100)
        st.session_state.banca -= stake
        st.error(f"Banca atualizada: -R$ {stake:.2f}")
