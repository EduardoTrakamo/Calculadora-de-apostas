import streamlit as st

st.set_page_config(page_title="Calculadora de Aposta Inteligente")

# Inicializa a banca no session_state
if "banca" not in st.session_state:
    st.session_state["banca"] = 100.00

st.title("💡 Calculadora de Aposta Inteligente")

# Exibe a banca atual
st.subheader(f"🪙 Banca atual: R$ {st.session_state['banca']:.2f}")

# Entrada para atualizar a banca
nova_banca = st.number_input("✏️ Digite nova banca:", min_value=0.0, value=st.session_state["banca"], step=1.0, format="%.2f")
if st.button("🔄 Atualizar banca"):
    st.session_state["banca"] = nova_banca
    st.success(f"✅ Banca atualizada para R$ {nova_banca:.2f}")

st.divider()

# Entradas da aposta
odd = st.number_input("📈 Odd da aposta", min_value=1.01, step=0.01, format="%.2f")
prob = st.slider("🔮 Sua chance da aposta bater (%)", 1, 100, 60)
percentual = st.slider("📊 % da banca a apostar", 1, 100, 5)

# Botão para calcular
if st.button("💸 Calcular Aposta"):
    prob_estimada = prob / 100
    percentual_aposta = percentual / 100
    odd_justa = 1 / prob_estimada
    valor_esperado = (odd * prob_estimada) - 1
    stake = st.session_state["banca"] * percentual_aposta
    retorno = stake * odd
    lucro = stake * (odd - 1)

    valor_txt = "✅ Aposta de valor!" if odd > odd_justa else "❌ Odd abaixo do justo."

    st.info(f"""
    🎯 Stake sugerida: R$ {stake:.2f}  
    💸 Retorno total: R$ {retorno:.2f}  
    💰 Lucro possível: R$ {lucro:.2f}  
    {valor_txt}
    """)

# Botões para ganhar ou perder aposta
col1, col2 = st.columns(2)

with col1:
    if st.button("✅ Ganhei"):
        stake = st.session_state["banca"] * (percentual / 100)
        ganho = stake * (odd - 1)
        st.session_state["banca"] += ganho
        st.success(f"🏆 Ganhou R$ {ganho:.2f}. Nova banca: R$ {st.session_state['banca']:.2f}")

with col2:
    if st.button("❌ Perdi"):
        stake = st.session_state["banca"] * (percentual / 100)
        st.session_state["banca"] -= stake
        st.error(f"💔 Perdeu R$ {stake:.2f}. Nova banca: R$ {st.session_state['banca']:.2f}")
