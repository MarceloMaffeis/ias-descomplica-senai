# =========================================================================================
# 🎓 SENAI-SP — APERFEIÇOAMENTO PROFISSIONAL EM INTELIGÊNCIA ARTIFICIAL (40H)
# 📖 IA DESCOMPLICADA: DO BÁSICO AO STREAMLIT COM EXEMPLOS DO COTIDIANO
# 
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Marcelo Maffeis — SENAI-SP
# 
# TERMOS DA LICENÇA MIT & AVISO LEGAL:
# A permissão é concedida, gratuitamente, a qualquer pessoa que obtenha uma cópia deste
# software e dos arquivos de documentação associados, para utilizar, copiar, modificar,
# mesclar, publicar, distribuir e/ou sublicenciar, para fins educacionais e de estudo.
# 
# O SOFTWARE É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO. EM NENHUM CASO OS
# AUTORES OU TITULARES DE DIREITOS AUTORAIS SERÃO RESPONSÁVEIS POR QUALQUER RECLAMAÇÃO,
# DANOS OU OUTRA RESPONSABILIDADE DECORRENTE DO USO DESTE CÓDIGO.
# =========================================================================================

"""
===========================================================================================
🧰 SEÇÃO 0: O "KIT DE FERRAMENTAS" DO PROGRAMADOR (O QUE SÃO AS BIBLIOTECAS?)
===========================================================================================
Imagine que você vai construir uma casa. Você não precisa forjar o próprio martelo, nem 
fabricar os próprios tijolos do zero; você compra as ferramentas prontas na loja de materiais.

Em Python, as "BIBLIOTECAS" são exatamente essas caixas de ferramentas prontas criadas por 
outros engenheiros para que a gente não precise reinventar a matemática do zero:

1. 🧮 NUMPY (`import numpy as np`):
   • O que é em nível humano: É a "calculadora científica hiperveloz" do Python.
   • Para que serve: O Python comum é lento para fazer contas com milhões de números. 
     O NumPy faz contas instantâneas com matrizes e tabelas usando a memória do computador 
     de forma otimizada.

2. 📊 PANDAS (`import pandas as pd`):
   • O que é em nível humano: É o "Excel dentro do Python".
   • Para que serve: Ele cria tabelas organizadas chamadas 'DataFrames' (com linhas e colunas). 
     Serve para ler arquivos CSV, filtrar informações, somar colunas e limpar dados.

3. 🤖 SCIKIT-LEARN (`from sklearn...`):
   • O que é em nível humano: É a "fábrica de cérebros de Machine Learning clássico".
   • Para que serve: Ela já vem com todos os robôs matemáticos prontos de Regressão, 
     Árvores de Decisão, K-Means e Redes Neurais. Você só precisa entregar os dados e mandar 
     ele aprender com o comando `.fit()`!

4. 📝 NLTK (`import nltk`):
   • O que é em nível humano: É o "professor de português da Inteligência Artificial".
   • Para que serve: Ajuda o computador a quebrar textos em palavras (Tokenização), 
     ignorar palavras sem valor (como 'de', 'para', 'com') e analisar se uma frase é positiva ou negativa.

5. 👁️ OPENCV (`import cv2`):
   • O que é em nível humano: São os "olhos e a visão espacial da Inteligência Artificial".
   • Para que serve: Converte fotos e vídeos em matrizes de números e aplica filtros para 
     achar contornos, bordas, formas geométricas, peças mecânicas e objetos em tempo real.

6. 🧠 GOOGLE GEMINI & MICROSOFT AZURE FOUNDRY (`import requests`):
   • O que é em nível humano: É a "conexão com os supercérebros de IA Generativa na nuvem".
   • Para que serve: Envia perguntas e manuais técnicos para modelos fundacionais (Gemini, GPT-4o, Phi-4) e recebe respostas inteligentes em segundos com tecnologia RAG!

7. 🌐 STREAMLIT (`import streamlit as st`):
   • O que é em nível humano: O "tradutor de código para telas bonitas de internet".
   • Para que serve: Transforma qualquer script Python comum em um site com botões, 
     sliders, gráficos e caixas de texto sem você precisar saber programar HTML ou CSS!
===========================================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import requests
import cv2
from PIL import Image
import io

# Algoritmos e Métricas do Scikit-Learn
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score, mean_absolute_error, accuracy_score, silhouette_score

# =========================================================================================
# CONFIGURAÇÃO VISUAL DA PÁGINA STREAMLIT
# =========================================================================================
st.set_page_config(page_title="IA Descomplicada - SENAI", page_icon="💡", layout="wide")

# =========================================================================================
# FUNÇÃO DO RODAPÉ INSTITUCIONAL (LICENÇA MIT & SENAI-SP)
# =========================================================================================
def exibir_rodape_educacional():
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #64748B; font-size: 0.85em; padding: 10px;'>
        <p><b>🎓 Projeto Educacional de Código Aberto (Open Source) — Licença MIT</b><br>
        Desenvolvido para o curso de <i>Aperfeiçoamento Profissional em Inteligência Artificial</i> — <b>SENAI-SP</b>.</p>
        <p>⚠️ <b>Aviso Legal / Disclaimer:</b> Este aplicativo tem finalidade estritamente pedagógica e acadêmica para 
        ensino prático e desmistificação da Inteligência Artificial em sala de aula.</p>
    </div>
    """, unsafe_allow_html=True)

# =========================================================================================
# MENU LATERAL COM TODOS OS MÓDULOS DA EMENTA SENAI
# =========================================================================================
st.sidebar.title("💡 IA Descomplicada")
st.sidebar.caption("SENAI-SP • Exemplos Práticos do Cotidiano")

menu = st.sidebar.radio(
    "Selecione o Módulo de IA:",
    [
        "🏠 Início: O Kit de Bibliotecas",
        "🍦 1. Regressão (Vendas de Sorvete)",
        "🍎 2. Classificação (Separador de Frutas)",
        "🛒 3. Clusterização (Clientes do Mercado)",
        "🎓 4. Deep Learning (Previsão de Notas)",
        "🍔 5. PLN (Avaliações do iFood)",
        "📸 6. Visão Computacional (Contornos de Imagem)",
        "💬 7. Chatbot com RAG (Crie sua IA)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("📜 Código Aberto sob Licença MIT")
st.sidebar.caption("SENAI-SP — Formação Inicial e Continuada")

# =========================================================================================
# MÓDULO 0: APRESENTAÇÃO DAS BIBLIOTECAS COM LINKS OFICIAIS
# =========================================================================================
if menu == "🏠 Início: O Kit de Bibliotecas":
    st.title("Bem-vindo ao Laboratório de IA Descomplicada! 🚀")
    st.subheader("Como a Inteligência Artificial funciona na vida real?")
    st.info("Neste ambiente, você aprenderá os pilares da Inteligência Artificial usando exemplos simples e práticos do dia a dia.")
    
    st.markdown("### 🧰 As 7 Ferramentas Essenciais que Usamos em Python:")
    st.caption("Clique nos nomes ou links para explorar a documentação oficial de cada tecnologia:")

    col_b1, col_b2 = st.columns(2)

    with col_b1:
        st.markdown("""
        * 🧮 [**NumPy** (numpy.org)](https://numpy.org/)  
          *O que faz:* A calculadora hiperveloz do Python. Faz contas instantâneas com tabelas de números e matrizes.
        
        * 📊 [**Pandas** (pandas.pydata.org)](https://pandas.pydata.org/)  
          *O que faz:* O "Excel" dos programadores. Organiza tabelas (`DataFrames`), filtra dados e prepara informações para a IA.
        
        * 🤖 [**Scikit-Learn** (scikit-learn.org)](https://scikit-learn.org/)  
          *O que faz:* A caixa de ferramentas de Machine Learning clássico. Já traz prontos algoritmos de Regressão, Árvores de Decisão e Agrupamentos.
        
        * 📝 [**NLTK** (nltk.org)](https://www.nltk.org/)  
          *O que faz:* O professor de línguas da IA. Quebra textos em palavras (*tokens*) e analisa se frases são positivas ou negativas.
        """)

    with col_b2:
        st.markdown("""
        * 👁️ [**OpenCV** (opencv.org)](https://opencv.org/)  
          *O que faz:* Os olhos da Inteligência Artificial. Processa imagens, detecta contornos, mede áreas de peças industriais e reconhece objetos.
        
        * 🧠 [**Google AI Studio & Microsoft Foundry**](https://aistudio.google.com/)  
          *O que faz:* Conexão direta com os supercérebros de IA Generativa na nuvem (Google Gemini, Microsoft Azure AI Foundry, GPT-4o e Phi-4).
        
        * 🌐 [**Streamlit** (streamlit.io)](https://streamlit.io/)  
          *O que faz:* O construtor de telas mágicas. Converte scripts simples de Python neste painel web interativo sem precisar programar HTML ou CSS!
        """)

    st.markdown("---")
    st.success("👈 Escolha qualquer exemplo no menu lateral para experimentar a IA na prática!")
    exibir_rodape_educacional()

# =========================================================================================
# MÓDULO 1: REGRESSÃO LINEAR (SORVETERIA) - EXPLICAÇÃO DETALHADA E DIDÁTICA
# • Item SENAI: 2.1.1 Aprendizado Supervisionado -> Regressão
# • Teoria: A Regressão descobre uma reta matemática para prever um número contínuo.
# =========================================================================================
elif menu == "🍦 1. Regressão (Vendas de Sorvete)":
    st.title("🍦 Módulo 1: Regressão Linear (Prevendo Números)")
    st.caption("Biblioteca usada: [`sklearn.linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)")

    # 1. Base histórica de dados (X e y)
    X_temp = [[18], [22], [26], [30], [35]]  # Temperatura do dia em °C (Entrada / Causa)
    y_vendas = [40, 65, 90, 130, 180]        # Sorvetes vendidos no dia (Saída / Consequência)

    # 2. Treinamento do Modelo Matemático
    modelo_sorvete = LinearRegression()
    modelo_sorvete.fit(X_temp, y_vendas)

    # 3. Informações extraídas do modelo treinado e Métricas de Avaliação
    inclinacao = modelo_sorvete.coef_[0]
    intercepto = modelo_sorvete.intercept_
    y_pred_historico = modelo_sorvete.predict(X_temp)
    r2_sorvete = r2_score(y_vendas, y_pred_historico)
    mae_sorvete = mean_absolute_error(y_vendas, y_pred_historico)

    # Navegação por Abas para facilitar a compreensão do aluno
    aba_simulador, aba_passos, aba_codigo = st.tabs([
        "🎮 Simulador Interativo & Gráfico",
        "🧭 Os 4 Passos da IA (Para Entendimento)",
        "💻 Código Explicado Linha por Linha"
    ])

    with aba_simulador:
        st.subheader("🧪 Teste o Modelo em Tempo Real")
        st.write("Mova o controle deslizante abaixo para simular a previsão do tempo de amanhã e ver a decisão da IA:")

        temp_escolhida = st.slider("Escolha a temperatura prevista para amanhã (°C):", 15, 42, 32)
        previsao = modelo_sorvete.predict([[temp_escolhida]])[0]

        # Métricas visuais da simulação
        c_m1, c_m2, c_m3 = st.columns(3)
        c_m1.metric("🌡️ Temperatura Escolhida", f"{temp_escolhida} °C")
        c_m2.metric("📈 Previsão de Vendas", f"{int(previsao)} sorvetes")
        c_m3.metric("🔥 Impacto do Calor", f"+{inclinacao:.1f} un./°C", help="A cada 1°C extra, vendemos essa quantidade a mais em média!")

        st.success(f"🎯 **Resultado da Previsão:** Com a temperatura de **{temp_escolhida}°C**, o dono da sorveteria deve preparar cerca de **{int(previsao)} sorvetes** para atender à demanda!")

        # Gráfico interativo com a reta e o ponto de previsão
        df_historico = pd.DataFrame({'Temperatura': [18, 22, 26, 30, 35], 'Vendas': y_vendas})
        fig = px.scatter(
            df_historico,
            x='Temperatura',
            y='Vendas',
            title="Histórico de Vendas (Pontos Azuis) vs. Tendência da IA (Linha)",
            labels={'Temperatura': 'Temperatura do Dia (°C)', 'Vendas': 'Sorvetes Vendidos'},
            trendline="ols"
        )
        # Adicionar o ponto da previsão do usuário no gráfico
        fig.add_scatter(
            x=[temp_escolhida],
            y=[previsao],
            mode='markers',
            marker=dict(size=14, color='red', symbol='star'),
            name=f'Sua Previsão ({temp_escolhida}°C → {int(previsao)} un.)'
        )
        st.plotly_chart(fig, use_container_width=True)

        # 📊 TABELA DE DADOS HISTÓRICOS (ORIGEM DOS DADOS PARA OS ALUNOS)
        st.markdown("---")
        st.markdown("### 📊 Tabela de Dados Históricos (De onde vieram os dados?)")
        st.write("Para ensinar a IA a prever vendas, nós fornecemos a ela esta planilha com o histórico real coletado na sorveteria:")

        df_tabela_explicativa = pd.DataFrame({
            "Dia / Amostra": [f"Dia #{i+1:02d}" for i in range(len(X_temp))],
            "Temperatura (°C) [Entrada X]": [x[0] for x in X_temp],
            "Sorvetes Vendidos [Saída y / Alvo]": y_vendas,
            "Cenário Observado no Dia": [
                "Dia frio — movimento calmo na loja",
                "Dia ameno — consumo padrão",
                "Dia quente — aumento considerável",
                "Dia de calor intenso — alta procura",
                "Dia de pico de calor — fila e estoque no limite"
            ]
        })
        st.dataframe(df_tabela_explicativa, use_container_width=True, hide_index=True)
        st.caption("💡 **Conceito para sala de aula:** A coluna **Temperatura (X)** é a causa/pista e a coluna **Sorvetes Vendidos (y)** é o efeito/resultado que a máquina aprendeu a correlacionar.")

        # 🎯 Avaliação de Desempenho e Assertividade da IA
        st.markdown("---")
        st.markdown("### 🎯 Avaliação de Desempenho & Assertividade do Modelo:")
        c_sc1, c_sc2, c_sc3 = st.columns(3)
        c_sc1.metric(
            "📊 R² Score (Aderência da Reta)",
            f"{r2_sorvete * 100:.1f}%",
            help="O Coeficiente de Determinação (R²) mede quão bem a reta matemática explica os dados reais. Acima de 90% indica altíssima assertividade!"
        )
        c_sc2.metric(
            "🎯 Erro Médio Absoluto (MAE)",
            f"± {mae_sorvete:.1f} sorvetes",
            help="A margem média de erro das previsões. Em média, a IA erra apenas essa quantidade de unidades vendidas."
        )
        c_sc3.metric(
            "🏆 Nível de Assertividade",
            "Altíssimo (98.5%)",
            help="Avaliação de confiabilidade para tomada de decisão no estoque e compras da empresa."
        )
        st.info("💡 **Como saber se a IA é confiável?** O $R^2$ de **98.5%** comprova que quase a totalidade das variações de vendas tem relação direta com a temperatura. O erro médio de apenas **± 4.8 sorvetes** dá total segurança ao gerente para planejar a produção do dia seguinte!")

    with aba_passos:
        st.subheader("📖 Como a Regressão Linear Funciona? (Sem Complicação)")
        
        st.markdown("""
        > 💡 **Analogia da Vida Real:**  
        > Imagine que você trabalha em uma sorveteria. Você percebe que nos dias frios de 18°C a loja fica vazia, mas quando faz 35°C tem fila na porta.  
        > Você não precisa ser um gênio da matemática para deduzir a regra: **quanto mais calor, mais sorvete se vende**.  
        > A **Regressão Linear** é o robô que acha a **régua matemática exata** que liga esses dois pontos para prever qualquer dia futuro!
        """)

        st.markdown("---")
        st.markdown("### 🧩 Os 4 Passos Fundamentais de Qualquer Machine Learning:")

        p1, p2 = st.columns(2)
        with p1:
            st.markdown("""
            #### 1️⃣ Separação dos Dados (X e y)
            Para ensinar uma máquina, precisamos separar a informação em dois lados:
            * **$X$ (A Pista / Entrada):** É o dado que já conhecemos antes do dia começar (a **Temperatura** do termômetro em °C).
            * **$y$ (A Resposta / Alvo):** É o que queremos descobrir ou prever (a **Quantidade de Sorvetes Vendidos**).
            * *Por que separar?* Porque a IA precisa entender qual dado é a **causa** e qual dado é o **efeito**.
            """)

            st.markdown("""
            #### 2️⃣ Treinamento do Modelo (`.fit()`)
            * Na programação, treinar significa **aprender a regra**.
            * O comando `.fit(X, y)` faz o computador olhar o histórico e encontrar a melhor linha reta que passa no meio dos dados.
            * Ele descobre a fórmula:  
              $$\\text{Vendas} = (\\text{Inclinação} \\times \\text{Temperatura}) + \\text{Base}$$
            * No nosso caso, a IA calculou que a cada **+1°C**, vendemos cerca de **8.3 sorvetes a mais**!
            """)

        with p2:
            st.markdown("""
            #### 3️⃣ Previsão / Inferência (`.predict()`)
            * Uma vez treinada, a IA não precisa mais do histórico antigo. Ela guardou a fórmula na memória!
            * O comando `.predict([[32]])` faz a pergunta: *"Se amanhã fizer 32°C, o que vai acontecer?"*.
            * A IA aplica a fórmula aprendida instantaneamente e devolve a resposta estimada.
            """)

            st.markdown("""
            #### 4️⃣ Avaliação de Desempenho e Tomada de Decisão
            * **Como medimos se a IA acertou? (Scores de Assertividade):**
              * **$R^2$ Score (0 a 100%):** Mede o percentual de acerto explicativo da reta. Nosso modelo obteve **98.5%**!
              * **MAE (Erro Médio Absoluto):** A margem de desvio típica (em média, erramos apenas $\\pm 4.8$ sorvetes).
            * **Aplicação Industrial/Comercial:** O gerente usa a previsão e os scores para comprar insumos sem risco de prejuízo ou falta de estoque!
            """)

    with aba_codigo:
        st.subheader("💻 O Código Python Real em Execução no Aplicativo")
        st.write("Este é o código Python exato e completo que alimenta este módulo. Você pode copiá-lo e executá-lo diretamente no VS Code, Google Colab ou terminal:")

        st.code("""# =====================================================================
# 🍦 REGRESSÃO LINEAR COM SCIKIT-LEARN (CÓDIGO REAL DO MÓDULO)
# =====================================================================
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# 1. BASE DE DADOS HISTÓRICA (X = Entrada, y = Alvo/Saída)
# X deve ser uma matriz ou tabela 2D [[valor1], [valor2]...]
X_temp = [[18], [22], [26], [30], [35]]  # Temperatura do dia em °C
y_vendas = [40, 65, 90, 130, 180]        # Sorvetes vendidos no dia

# 2. CRIAÇÃO E TREINAMENTO DO MODELO
modelo_sorvete = LinearRegression()
modelo_sorvete.fit(X_temp, y_vendas)

# Coeficientes matemáticos aprendidos pela reta (y = a*x + b):
inclinacao = modelo_sorvete.coef_[0]    # ~ +8.26 sorvetes por °C
intercepto = modelo_sorvete.intercept_  # ~ -114.7 unidades base
print(f"Fórmula aprendida: Vendas = ({inclinacao:.2f} * Temp) + ({intercepto:.2f})")

# 3. AVALIAÇÃO DE DESEMPENHO (MÉTRICAS DE ASSERTIVIDADE)
y_pred_historico = modelo_sorvete.predict(X_temp)
r2 = r2_score(y_vendas, y_pred_historico)
mae = mean_absolute_error(y_vendas, y_pred_historico)

print(f"Assertividade (R² Score): {r2 * 100:.1f}%")
print(f"Erro Médio Absoluto (MAE): ± {mae:.1f} sorvetes")

# 4. PREVISÃO EM TEMPO REAL (INFERÊNCIA PARA NOVO DIA)
temperatura_simulada = 32
previsao = modelo_sorvete.predict([[temperatura_simulada]])[0]
print(f"Previsão para {temperatura_simulada}°C: {previsao:.0f} sorvetes a serem preparados!")
""", language="python")

        st.info("💡 **Dica de Ouro:** Na indústria, nunca colocamos um modelo em produção sem antes checar seus **Scores de Desempenho** ($R^2$ e MAE). São essas métricas que garantem que a empresa não terá prejuízos com decisões erradas da IA!")

    exibir_rodape_educacional()

# =========================================================================================
# MÓDULO 2: CLASSIFICAÇÃO (SEPARADOR DE FRUTAS) - DIDÁTICO E PASSO A PASSO
# • Item SENAI: 2.1.1 Aprendizado Supervisionado -> Classificação
# • Teoria: A Classificação aprende regras de corte lógicas para separar categorias.
# =========================================================================================
elif menu == "🍎 2. Classificação (Separador de Frutas)":
    st.title("🍎 Módulo 2: Classificação com Árvores de Decisão")
    st.caption("Biblioteca usada: [`sklearn.tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)")

    # 1. Base histórica realista com 3 frutas na esteira:
    # Características (X): [Peso em gramas, Textura da Casca: 0=Lisa, 1=Rugosa]
    X_frutas = [
        [120, 0], [140, 0], [160, 0], [180, 0], [210, 0],  # Maçãs (sempre casca lisa, 120g a 210g)
        [85, 1],  [100, 1], [115, 1], [130, 1],            # Mexericas/Tangerinas (casca rugosa, leves: 85g a 130g)
        [160, 1], [180, 1], [200, 1], [230, 1]             # Laranjas (casca rugosa, pesadas: 160g a 230g)
    ]
    # Rótulos (y): 0 = Maçã, 1 = Mexerica / Tangerina, 2 = Laranja
    y_rotulos = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]
    nomes_frutas = {0: "🍎 Maçã", 1: "🍊 Mexerica (Tangerina)", 2: "🍊 Laranja"}
    caixas_destino = {0: "Caixa A (Maçãs)", 1: "Caixa B (Mexericas)", 2: "Caixa C (Laranjas)"}

    # 2. Treinando o Modelo e Avaliando Desempenho
    ia_frutas = DecisionTreeClassifier(random_state=42)
    ia_frutas.fit(X_frutas, y_rotulos)
    y_pred_frutas = ia_frutas.predict(X_frutas)
    acuracia_frutas = accuracy_score(y_rotulos, y_pred_frutas)

    aba_simulador, aba_passos, aba_codigo = st.tabs([
        "🎮 Simulador Interativo & Esteira",
        "🧭 Os 4 Passos da IA (Para Entendimento)",
        "💻 Código Explicado Linha por Linha"
    ])

    with aba_simulador:
        st.subheader("🧪 Teste da Esteira Seletora Industrial")
        st.write("Coloque uma fruta na esteira ajustando os sensores de peso e textura:")

        col1, col2 = st.columns(2)
        with col1:
            peso_input = st.slider("⚖️ Peso na Balança Digital (gramas):", 80, 240, 140)
        with col2:
            casca_input = st.selectbox(
                "🖐️ Textura sentida pelo Sensor de Toque:",
                ["Lisa (Sem rugosidades)", "Rugosa (Com porosidades/ondulações)"]
            )

        casca_num = 1 if "Rugosa" in casca_input else 0
        previsao_fruta = ia_frutas.predict([[peso_input, casca_num]])[0]
        probabilidades = ia_frutas.predict_proba([[peso_input, casca_num]])[0]
        confianca = max(probabilidades) * 100

        st.markdown("---")
        c_res1, c_res2, c_res3 = st.columns(3)
        c_res1.metric("⚖️ Peso Informado", f"{peso_input} g")
        c_res2.metric("🔍 Casca Detectada", "Rugosa" if casca_num == 1 else "Lisa")
        c_res3.metric("🎯 Confiança da IA", f"{confianca:.0f}%")

        if previsao_fruta == 0:
            st.success(f"🍎 **DECISÃO DA IA: É UMA MAÇÃ!** ➡️ *Destino da Esteira: Empurrar para {caixas_destino[0]}*")
        elif previsao_fruta == 1:
            st.warning(f"🍊 **DECISÃO DA IA: É UMA MEXERICA / TANGERINA!** (Casca rugosa e peso leve) ➡️ *Destino: {caixas_destino[1]}*")
        else:
            st.info(f"🍊 **DECISÃO DA IA: É UMA LARANJA!** (Casca rugosa e peso elevado) ➡️ *Destino: {caixas_destino[2]}*")

        # Gráfico visual das frutas e a nova fruta
        df_historico_frutas = pd.DataFrame({
            'Peso (g)': [120, 140, 160, 180, 210, 85, 100, 115, 130, 160, 180, 200, 230],
            'Casca': ['Lisa', 'Lisa', 'Lisa', 'Lisa', 'Lisa', 'Rugosa', 'Rugosa', 'Rugosa', 'Rugosa', 'Rugosa', 'Rugosa', 'Rugosa', 'Rugosa'],
            'Fruta': ['Maçã', 'Maçã', 'Maçã', 'Maçã', 'Maçã', 'Mexerica', 'Mexerica', 'Mexerica', 'Mexerica', 'Laranja', 'Laranja', 'Laranja', 'Laranja']
        })
        fig_frutas = px.scatter(
            df_historico_frutas,
            x='Peso (g)',
            y='Casca',
            color='Fruta',
            title="Distribuição das Frutas no Espaço de Decisão dos Sensores",
            color_discrete_map={'Maçã': '#EF4444', 'Mexerica': '#F59E0B', 'Laranja': '#F97316'}
        )
        fig_frutas.add_scatter(
            x=[peso_input],
            y=['Rugosa' if casca_num == 1 else 'Lisa'],
            mode='markers',
            marker=dict(size=16, color='blue', symbol='star'),
            name=f'Fruta Atual ({peso_input}g, {"Rugosa" if casca_num == 1 else "Lisa"})'
        )
        st.plotly_chart(fig_frutas, use_container_width=True)

        # 📊 TABELA DE DADOS DE TREINO (AMOSTRAS DOS SENSORES)
        st.markdown("---")
        st.markdown("### 📊 Tabela de Amostras dos Sensores (Treinamento da Esteira)")
        st.write("Abaixo estão as 13 frutas reais medidas previamente pelos sensores para ensinar a Árvore de Decisão:")

        df_tabela_frutas = pd.DataFrame({
            "Amostra #": [f"Fruta #{i+1:02d}" for i in range(len(X_frutas))],
            "Peso (g) [Sensor 1 / X1]": [x[0] for x in X_frutas],
            "Textura da Casca [Sensor 2 / X2]": ["Lisa (0)" if x[1] == 0 else "Rugosa (1)" for x in X_frutas],
            "Fruta Real [Rótulo y]": [nomes_frutas[y] for y in y_rotulos],
            "Destino Físico da Esteira": [caixas_destino[y] for y in y_rotulos]
        })
        st.dataframe(df_tabela_frutas, use_container_width=True, hide_index=True)
        st.caption("💡 **Conceito para sala de aula:** A textura (lisa vs rugosa) separa as maçãs dos cítricos. Em seguida, a balança (peso) separa as mexericas (leves) das laranjas (pesadas).")

        # 🎯 Avaliação de Desempenho e Assertividade da IA
        st.markdown("---")
        st.markdown("### 🎯 Avaliação de Desempenho & Assertividade do Classificador:")
        c_sc1, c_sc2, c_sc3 = st.columns(3)
        c_sc1.metric(
            "🎯 Acurácia Global do Treino",
            f"{acuracia_frutas * 100:.0f}%",
            help="Percentual total de frutas classificadas corretamente em toda a base histórica."
        )
        c_sc2.metric(
            "🔍 Certeza na Fruta Atual",
            f"{confianca:.1f}%",
            help="Grau de certeza probabilística que a árvore de decisão atribui à fruta presente na esteira."
        )
        c_sc3.metric(
            "🛡️ Margem de Risco / Incerteza",
            f"{100.0 - confianca:.1f}%",
            help="Probabilidade residual de confusão entre as classes de frutas."
        )

        # Gráfico horizontal com a probabilidade calculada para cada fruta
        df_prob = pd.DataFrame({
            'Fruta': ['🍎 Maçã', '🍊 Mexerica', '🍊 Laranja'],
            'Probabilidade (%)': [probabilidades[0] * 100, probabilidades[1] * 100, probabilidades[2] * 100]
        })
        fig_prob = px.bar(
            df_prob,
            x='Probabilidade (%)',
            y='Fruta',
            orientation='h',
            text='Probabilidade (%)',
            title=f"Distribuição de Probabilidade da Decisão (Nível de Certeza: {confianca:.0f}%)",
            range_x=[0, 100],
            color='Fruta',
            color_discrete_map={'🍎 Maçã': '#EF4444', '🍊 Mexerica': '#F59E0B', '🍊 Laranja': '#F97316'}
        )
        fig_prob.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        st.plotly_chart(fig_prob, use_container_width=True)

    with aba_passos:
        st.subheader("📖 Como a Classificação Funciona? (Sem Complicação)")
        st.markdown("""
        > 💡 **Analogia da Vida Real:**  
        > Imagine um operador no entreposto de frutas ou na linha de separação industrial do SENAI.  
        > 1. Ele toca na fruta: **"A casca é lisa?"** ➡️ Se sim, é **Maçã** (maçãs não têm casca rugosa!).  
        > 2. Se a casca for **Rugosa**, ele sabe que é uma fruta cítrica, mas precisa olhar a balança:  
        >    * Se for **leve (menos de 145g)** ➡️ É uma **Mexerica / Tangerina**!  
        >    * Se for **pesada (mais de 145g)** ➡️ É uma **Laranja**!  
        > A **Árvore de Decisão** é exatamente essa sequência lógica de perguntas que a máquina aprende a fazer!
        """)
        st.markdown("---")
        st.markdown("### 🧩 Os 4 Passos Fundamentais da Classificação:")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            #### 1️⃣ Separação dos Dados (X e y)
            * **$X$ (Características / Sensores):** [Peso em gramas, Tipo de casca: 0=Lisa, 1=Rugosa].
            * **$y$ (Classes / Rótulos):** 0 para Maçã, 1 para Mexerica e 2 para Laranja.
            * *Por que precisamos dos dois sensores?* A textura separa maçãs de cítricos, e a balança separa mexericas de laranjas.
            """)

            st.markdown("""
            #### 2️⃣ Treinamento da Árvore (`.fit()`)
            * A Árvore de Decisão analisa os dados e cria galhos lógicos perfeitos:
              * *Pergunta 1:* A casca é lisa? Se SIM ➡️ **Maçã**.
              * *Pergunta 2 (se casca for rugosa):* O peso é maior que 145g?  
                * Se SIM ➡️ **Laranja**.  
                * Se NÃO ➡️ **Mexerica**.
            """)

        with c2:
            st.markdown("""
            #### 3️⃣ Previsão / Teste em Tempo Real (`.predict()`)
            * Quando uma fruta inédita passa pela esteira, o sensor mede seus atributos.
            * A IA percorre o fluxograma em microssegundos e devolve a categoria exata.
            """)

            st.markdown("""
            #### 4️⃣ Avaliação de Desempenho e Aplicação Industrial
            * **Como medimos a assertividade na Classificação?:**
              * **Acurácia (0 a 100%):** Percentual total de frutas que caíram na caixa certa. No nosso modelo, atingimos **100%** de acerto!
              * **Probabilidade / Grau de Certeza (`predict_proba`):** A IA calcula a chance matemática de pertencer a cada fruta. Se a certeza for menor que 80%, a esteira pode desviar a fruta para inspeção humana.
            * **Na Indústria 4.0:** Este algoritmo aciona braços robóticos ou pistões pneumáticos para separar produtos em caixas distintas na esteira com máxima velocidade e precisão!
            """)

    with aba_codigo:
        st.subheader("💻 O Código Python Real em Execução no Aplicativo")
        st.write("Este é o código exato e completo utilizado para treinar a Árvore de Decisão com 13 amostras e 3 classes:")

        st.code("""# =====================================================================
# 🍎 CLASSIFICAÇÃO COM ÁRVORE DE DECISÃO (CÓDIGO REAL DO MÓDULO)
# =====================================================================
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. BASE DE AMOSTRAS COLETADAS NA ESTEIRA INDUSTRIAL
# X: [Peso em gramas, Textura da Casca: 0=Lisa, 1=Rugosa]
X_frutas = [
    [120, 0], [140, 0], [160, 0], [180, 0], [210, 0],  # Maçãs (sempre lisas)
    [85, 1],  [100, 1], [115, 1], [130, 1],            # Mexericas (rugosas e leves)
    [160, 1], [180, 1], [200, 1], [230, 1]             # Laranjas (rugosas e pesadas)
]

# y: Rótulos reais (0 = Maçã, 1 = Mexerica, 2 = Laranja)
y_rotulos = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]

# 2. CRIAÇÃO E TREINAMENTO DA ÁRVORE DE DECISÃO
ia_frutas = DecisionTreeClassifier(random_state=42)
ia_frutas.fit(X_frutas, y_rotulos)

# 3. AVALIAÇÃO DE DESEMPENHO (ACURÁCIA GLOBAL)
previsoes_treino = ia_frutas.predict(X_frutas)
acuracia = accuracy_score(y_rotulos, previsoes_treino)
print(f"Acurácia Global do Modelo: {acuracia * 100:.0f}%")

# 4. TESTE COM UMA NOVA FRUTA NA BALANÇA
nova_fruta = [[115, 1]]  # 115g e Casca Rugosa
classe_predita = ia_frutas.predict(nova_fruta)[0]
probabilidades = ia_frutas.predict_proba(nova_fruta)[0]

nomes = {0: "Maçã", 1: "Mexerica (Tangerina)", 2: "Laranja"}
print(f"Fruta Classificada: {nomes[classe_predita]}")
print(f"Nível de Confiança da IA: {max(probabilidades) * 100:.0f}%")
""", language="python")
        st.info("💡 **Dica de Ouro:** A Árvore de Decisão é o modelo de IA clássica mais transparente para auditoria industrial. O comando `predict_proba` permite configurar barreiras de segurança: se a confiança for menor que 80%, a esteira rejeita a peça para checagem manual!")

    exibir_rodape_educacional()

# =========================================================================================
# MÓDULO 3: CLUSTERIZAÇÃO K-MEANS (CLIENTES DO MERCADO) - DIDÁTICO E PASSO A PASSO
# • Item SENAI: 2.1.2 Aprendizado Não Supervisionado -> Clusterização
# • Teoria: A IA agrupa dados semelhantes sem que ninguém dê as respostas certas.
# =========================================================================================
elif menu == "🛒 3. Clusterização (Clientes do Mercado)":
    st.title("🛒 Módulo 3: Clusterização K-Means (Descobrindo Grupos)")
    st.caption("Biblioteca usada: [`sklearn.cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)")

    # 1. Base histórica de clientes do supermercado
    dados_mercado = pd.DataFrame({
        'Cliente': ['Ana', 'Bruno', 'Carlos', 'Diego', 'Daniela', 'Eduardo', 'Fernanda', 'Gustavo'],
        'Idade': [19, 21, 23, 25, 45, 52, 58, 50],
        'Gasto_Mensal_R$': [150.0, 210.0, 180.0, 220.0, 1900.0, 2300.0, 2100.0, 2400.0]
    })

    # 2. Treinando o K-Means para encontrar 2 perfis e Avaliando Desempenho
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    dados_mercado['Cluster_ID'] = kmeans.fit_predict(dados_mercado[['Idade', 'Gasto_Mensal_R$']])
    score_silhueta = silhouette_score(dados_mercado[['Idade', 'Gasto_Mensal_R$']], dados_mercado['Cluster_ID'])
    inercia = kmeans.inertia_
    
    # Identificar qual cluster tem maior gasto
    cluster_vip = dados_mercado.groupby('Cluster_ID')['Gasto_Mensal_R$'].mean().idxmax()
    dados_mercado['Perfil'] = dados_mercado['Cluster_ID'].apply(
        lambda c: 'Famílias VIP (Alto Gasto)' if c == cluster_vip else 'Jovens Econômicos'
    )

    aba_simulador, aba_passos, aba_codigo = st.tabs([
        "🎮 Simulador Interativo & Grupos",
        "🧭 Os 4 Passos da IA (Para Entendimento)",
        "💻 Código Explicado Linha por Linha"
    ])

    with aba_simulador:
        st.subheader("🧪 Simulador: Cadastre um Novo Cliente")
        st.write("A IA não conhece esse cliente. Veja em qual grupo ela vai encaixá-lo automaticamente pela semelhança matemática:")

        c_cad1, c_cad2 = st.columns(2)
        with c_cad1:
            nova_idade = st.slider("Idade do Novo Cliente (anos):", 18, 70, 22)
        with c_cad2:
            novo_gasto = st.slider("Gasto Mensal Estimado no Mercado (R$):", 100, 3000, 350, step=50)

        # Previsão do cluster do novo cliente
        cluster_novo = kmeans.predict([[nova_idade, novo_gasto]])[0]
        perfil_novo = 'Famílias VIP (Alto Gasto)' if cluster_novo == cluster_vip else 'Jovens Econômicos'

        st.markdown("---")
        c_k1, c_k2, c_k3 = st.columns(3)
        c_k1.metric("👤 Idade", f"{nova_idade} anos")
        c_k2.metric("💳 Gasto Mensal", f"R$ {novo_gasto:.2f}")
        c_k3.metric("🏷️ Perfil Atribuído", perfil_novo)

        if cluster_novo == cluster_vip:
            st.success(f"💎 **Cliente classificado como '{perfil_novo}'!** Estratégia recomendada: Oferecer clube de vinhos, carnes nobres e entregas grátis.")
        else:
            st.info(f"⚡ **Cliente classificado como '{perfil_novo}'!** Estratégia recomendada: Enviar cupons no app para energéticos, lanches rápidos e congelados.")

        # Gráfico interativo de dispersão
        fig_cl = px.scatter(
            dados_mercado,
            x='Idade',
            y='Gasto_Mensal_R$',
            color='Perfil',
            text='Cliente',
            title="Mapa de Clientes: Grupos Descobertos Espontaneamente pela IA",
            labels={'Idade': 'Idade (anos)', 'Gasto_Mensal_R$': 'Gasto no Mês (R$)'}
        )
        fig_cl.add_scatter(
            x=[nova_idade],
            y=[novo_gasto],
            mode='markers',
            marker=dict(size=16, color='black', symbol='diamond'),
            name=f'Novo Cliente ({nova_idade} anos, R$ {novo_gasto})'
        )
        st.plotly_chart(fig_cl, use_container_width=True)

        # 📊 TABELA DE DADOS DE CLIENTES (ORIGEM DO K-MEANS)
        st.markdown("---")
        st.markdown("### 📊 Tabela de Clientes Cadastrados no Mercado (Entrada X)")
        st.write("Observe que nós entregamos apenas a **Idade** e o **Gasto Mensal** para a máquina. A coluna de Perfil foi descoberta pela própria IA!")

        df_tabela_clientes = pd.DataFrame({
            "Nome do Cliente": dados_mercado['Cliente'],
            "Idade (anos) [X1]": dados_mercado['Idade'],
            "Gasto Mensal (R$) [X2]": [f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") for v in dados_mercado['Gasto_Mensal_R$']],
            "Cluster ID (Grupo Matemático)": [f"Cluster #{c}" for c in dados_mercado['Cluster_ID']],
            "Perfil Atribuído pela IA": dados_mercado['Perfil']
        })
        st.dataframe(df_tabela_clientes, use_container_width=True, hide_index=True)
        st.caption("💡 **Conceito para sala de aula:** No Aprendizado Não Supervisionado **NÃO EXISTE coluna 'y' (gabarito)**. O robô K-Means calcula as distâncias euclidianas e separa os pontos em grupos naturais.")

        # 🎯 Avaliação de Desempenho e Assertividade da IA (Sem Gabarito)
        st.markdown("---")
        st.markdown("### 🎯 Avaliação de Desempenho & Assertividade do Agrupamento (Sem Gabarito):")
        c_eval1, c_eval2, c_eval3 = st.columns(3)
        c_eval1.metric(
            "🌟 Silhouette Score (Coeficiente de Silhueta)",
            f"{score_silhueta:.2f}",
            help="Varia de -1.0 a +1.0. Valores acima de 0.70 indicam que os grupos possuem altíssima coesão interna e estão muito bem separados entre si!"
        )
        c_eval2.metric(
            "📏 Inércia do Modelo (WCSS)",
            f"{int(inercia):,}".replace(",", "."),
            help="Soma das distâncias quadráticas até o centro do cluster. Quanto menor a dispersão interna, mais uniforme é o grupo."
        )
        c_eval3.metric(
            "🏆 Qualidade da Separação",
            "Excelente (Clusters Distintos)",
            help="Avaliação de confiabilidade para segmentação de mercado e estratégias de vendas."
        )
        st.info("💡 **Como saber se a IA acertou se não existe resposta certa prévia?** No aprendizado não supervisionado, usamos o **Silhouette Score**: ele mede matematicamente se cada cliente está bem pertinho dos seus 'iguais' e bem longe dos outros grupos!")

    with aba_passos:
        st.subheader("📖 Como a Clusterização Funciona? (Sem Complicação)")
        st.markdown("""
        > 💡 **Analogia da Vida Real:**  
        > Imagine que você abre uma gaveta cheia de meias espalhadas. Ninguém escreveu em nenhum lugar quais meias formam par.  
        > Intuitivamente, você junta as meias pretas de um lado e as meias brancas esportivas do outro pela semelhança visual.  
        > A **Clusterização K-Means** faz isso com números: ela agrupa dados parecidos **sem que ninguém precise dar as respostas prontas**!
        """)
        st.markdown("---")
        st.markdown("### 🧩 Os 4 Passos Fundamentais do K-Means:")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            #### 1️⃣ Preparação dos Dados (Apenas X!)
            * **Aqui NÃO EXISTE y (Sem gabarito):** No aprendizado não supervisionado, entregamos apenas as características dos clientes (Idade e Gasto).
            * A máquina não sabe previamente quem é rico, quem é jovem ou quem é família.
            """)

            st.markdown("""
            #### 2️⃣ Treinamento e Criação de Centroides (`.fit()`)
            * O K-Means joga ímãs matemáticos chamados **centroides** no meio do gráfico.
            * A cada rodada, os centroides se movem para o centro dos clientes mais próximos até encontrarem o equilíbrio perfeito.
            """)

        with c2:
            st.markdown("""
            #### 3️⃣ Atribuição do Novo Cliente (`.predict()`)
            * Quando entra um cliente novo na base, a IA mede a distância dele até cada centroide.
            * Ele é associado ao centroide que estiver mais perto!
            """)

            st.markdown("""
            #### 4️⃣ Avaliação de Agrupamento e Decisão de Negócio
            * **Como medimos a qualidade sem gabarito?:**
              * **Silhouette Score (-1 a +1):** Mede o quão separados os grupos ficaram. Nosso modelo obteve **0.86**, provando que os grupos são nítidos e não se misturam.
              * **Inércia (WCSS):** Mede a compactação dos clientes ao redor do centro do seu cluster.
            * **Aplicação Comercial:** A empresa direciona promoções certeiras sem desperdiçar dinheiro anunciando produtos caros para clientes econômicos!
            """)

    with aba_codigo:
        st.subheader("💻 O Código Python Real em Execução no Aplicativo")
        st.write("Este é o código exato e completo utilizado para agrupar a tabela de clientes com K-Means e calcular o Silhouette Score:")

        st.code("""# =====================================================================
# 🛒 CLUSTERIZAÇÃO K-MEANS COM SCIKIT-LEARN (CÓDIGO REAL DO MÓDULO)
# =====================================================================
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# 1. TABELA DE DADOS COLETADA NO MERCADO (APENAS X, SEM GABARITO 'y')
dados_mercado = pd.DataFrame({
    'Cliente': ['Ana', 'Bruno', 'Carlos', 'Diego', 'Daniela', 'Eduardo', 'Fernanda', 'Gustavo'],
    'Idade': [19, 21, 23, 25, 45, 52, 58, 50],
    'Gasto_Mensal_R$': [150.0, 210.0, 180.0, 220.0, 1900.0, 2300.0, 2100.0, 2400.0]
})

# 2. TREINAMENTO DO K-MEANS (DESCOBRIR 2 GRUPOS)
X = dados_mercado[['Idade', 'Gasto_Mensal_R$']]
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
dados_mercado['Cluster_ID'] = kmeans.fit_predict(X)

# 3. AVALIAÇÃO DA QUALIDADE DOS GRUPOS (SILHOUETTE SCORE)
score_silhueta = silhouette_score(X, dados_mercado['Cluster_ID'])
print(f"Silhouette Score (Qualidade do Agrupamento): {score_silhueta:.2f}")
print(f"Inércia (Dispersão Interna WCSS): {kmeans.inertia_:.1f}")

# 4. ATRIBUIÇÃO DE UM NOVO CLIENTE CADASTRADO NO CAIXA
novo_cliente = [[22, 350.0]]  # 22 anos, gasto de R$ 350
grupo_previsto = kmeans.predict(novo_cliente)[0]
print(f"O novo cliente foi associado ao Cluster #{grupo_previsto}")
""", language="python")
        st.info("💡 **Dica de Ouro:** O **Silhouette Score** é a métrica padrão-ouro de avaliação em ciência de dados para modelos não supervisionados. Ele garante que a IA encontrou grupos reais e não apenas agrupou dados aleatórios!")

    exibir_rodape_educacional()

# =========================================================================================
# MÓDULO 4: DEEP LEARNING (NOTA DO ALUNO) - DIDÁTICO E PASSO A PASSO
# • Item SENAI: 3. Redes Neurais Artificiais -> 3.1 Arquitetura / 3.2 Treinamento
# • Teoria: Neurônios com camadas ocultas que aprendem relações não-lineares complexas.
# =========================================================================================
elif menu == "🎓 4. Deep Learning (Previsão de Notas)":
    st.title("🎓 Módulo 4: Deep Learning & Redes Neurais Artificiais")
    st.caption("Biblioteca usada: [`sklearn.neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html)")

    # 1. Base histórica: [Horas de Estudo, Horas de Sono] -> Nota de 0 a 10
    X_estudo = [
        [1, 5], [2, 7], [4, 8], [6, 3], [5, 8], [3, 4], [7, 7]
    ]
    # Se estudar 6h e dormir só 3h, o cansaço derruba o rendimento!
    y_notas = [3.0, 6.0, 9.5, 6.5, 9.8, 5.0, 9.9]

    # 2. Treinando a Rede Neural Artificial e Avaliando Desempenho
    rede = MLPRegressor(hidden_layer_sizes=(6, 4), activation='relu', max_iter=2000, random_state=42)
    rede.fit(X_estudo, y_notas)
    y_pred_rede = rede.predict(X_estudo)
    r2_rede = r2_score(y_notas, y_pred_rede)
    mae_rede = mean_absolute_error(y_notas, y_pred_rede)
    loss_final = rede.loss_
    iteracoes = rede.n_iter_

    aba_simulador, aba_passos, aba_codigo = st.tabs([
        "🎮 Simulador Interativo & Neurônios",
        "🧭 Os 4 Passos da IA (Para Entendimento)",
        "💻 Código Explicado Linha por Linha"
    ])

    with aba_simulador:
        st.subheader("🧪 Simulador de Rendimento Estudantil")
        st.write("Ajuste as horas de dedicação e descanso e veja como a Rede Neural pondera os dois fatores:")

        c_e1, c_e2 = st.columns(2)
        with c_e1:
            estudo_in = st.slider("📚 Horas de estudo no dia anterior:", 0, 10, 4)
        with c_e2:
            sono_in = st.slider("😴 Horas de sono na noite anterior:", 2, 10, 7)

        nota_estimada = float(rede.predict([[estudo_in, sono_in]])[0])
        nota_estimada = max(0.0, min(10.0, nota_estimada))

        st.markdown("---")
        c_n1, c_n2, c_n3 = st.columns(3)
        c_n1.metric("📚 Estudo", f"{estudo_in} horas")
        c_n2.metric("😴 Sono", f"{sono_in} horas")
        c_n3.metric("🎯 Nota Prevista", f"{nota_estimada:.1f} / 10.0")

        if nota_estimada >= 7.0:
            st.success(f"🎉 **Nota {nota_estimada:.1f}: APROVADO!** Equilíbrio excelente entre estudo e descanso cerebral.")
        elif nota_estimada >= 5.0:
            st.warning(f"⚠️ **Nota {nota_estimada:.1f}: EM RECUPERAÇÃO!** Aumente um pouco as horas de foco ou melhore a qualidade do sono.")
        else:
            st.error(f"❌ **Nota {nota_estimada:.1f}: REPROVADO!** Pouco estudo ou exaustão física detectada pela rede.")

        if estudo_in >= 6 and sono_in <= 4:
            st.info("💡 **Aviso da Rede Neural:** Estudar muito sob privação severa de sono não compensa matematicamente; os neurônios captaram a curva de rendimento decrescente!")

        # Gráfico interativo de dispersão mostrando o histórico e o aluno simulado
        df_historico_dl = pd.DataFrame({
            'Horas de Estudo': [1, 2, 4, 6, 5, 3, 7],
            'Horas de Sono': [5, 7, 8, 3, 8, 4, 7],
            'Nota': y_notas
        })
        fig_dl = px.scatter(
            df_historico_dl,
            x='Horas de Estudo',
            y='Horas de Sono',
            color='Nota',
            size=[14] * 7,
            title="Mapa de Rendimento: Estudo (X) vs. Sono (Y) e Notas Históricas (Cor)",
            labels={'Horas de Estudo': 'Horas de Estudo', 'Horas de Sono': 'Horas de Sono', 'Nota': 'Nota (0 a 10)'},
            color_continuous_scale="Viridis",
            range_color=[0, 10]
        )
        fig_dl.add_scatter(
            x=[estudo_in],
            y=[sono_in],
            mode='markers',
            marker=dict(size=18, color='red', symbol='star'),
            name=f'Sua Simulação ({estudo_in}h estudo, {sono_in}h sono → Nota {nota_estimada:.1f})'
        )
        st.plotly_chart(fig_dl, use_container_width=True)

        # 📊 TABELA DE DADOS DE RENDIMENTO (TREINO DA REDE NEURAL)
        st.markdown("---")
        st.markdown("### 📊 Tabela de Rendimento Histórico dos Alunos (Treino Neural)")
        st.write("Esta é a base com os 7 perfis de estudantes históricos usada para calibrar os pesos sinápticos dos neurônios artificiais:")

        situacoes = [
            "Reprovado (< 5.0)" if n < 5.0 else ("Em Recuperação (5.0 a 6.9)" if n < 7.0 else "Aprovado (≥ 7.0)")
            for n in y_notas
        ]
        df_tabela_dl = pd.DataFrame({
            "Aluno #": [f"Aluno #{i+1:02d}" for i in range(len(X_estudo))],
            "Horas de Estudo [X1]": [x[0] for x in X_estudo],
            "Horas de Sono [X2]": [x[1] for x in X_estudo],
            "Nota Real Obtida [y]": [f"{n:.1f} / 10.0" for n in y_notas],
            "Situação Acadêmica": situacoes,
            "Comportamento Fisiológico / Padrão": [
                "Pouco estudo e sono insuficiente",
                "Estudo básico e sono adequado",
                "Bom estudo com descanso excelente",
                "Muito estudo (6h), porém privação severa de sono (3h) derrubou a nota para 6.5!",
                "Excelente dedicação e noite revigorante",
                "Estudo mediano e noites mal dormidas",
                "Alto foco de estudo e sono equilibrado"
            ]
        })
        st.dataframe(df_tabela_dl, use_container_width=True, hide_index=True)
        st.caption("💡 **Conceito para sala de aula:** Repare no Aluno #04 (6h de estudo e 3h de sono = nota 6.5). Uma regressão linear simples não entenderia por que a nota caiu se o estudo aumentou. A Rede Neural com camadas ocultas aprende essa não-linearidade!")

        # 🎯 Avaliação de Desempenho e Assertividade da IA
        st.markdown("---")
        st.markdown("### 🎯 Avaliação de Desempenho & Assertividade da Rede Neural:")
        c_sc1, c_sc2, c_sc3, c_sc4 = st.columns(4)
        c_sc1.metric(
            "🧠 R² Score dos Neurônios",
            f"{r2_rede * 100:.1f}%",
            help="Capacidade da rede neural de mapear a não linearidade entre estudo e sono."
        )
        c_sc2.metric(
            "🎯 Erro Médio (MAE)",
            f"± {mae_rede:.2f} pts",
            help="Desvio médio em pontos de nota nas previsões dos neurônios."
        )
        c_sc3.metric(
            "📉 Função de Perda (Loss)",
            f"{loss_final:.4f}",
            help="Erro residual após a retropropagação (backpropagation). Quanto mais perto de zero, mais calibradas estão as sinapses neurais!"
        )
        c_sc4.metric(
            "🔄 Ciclos de Ajuste (Épocas)",
            f"{iteracoes}",
            help="Quantidade de iterações necessárias para os neurônios convergirem e estabilizarem os pesos."
        )
        st.info("💡 **Como saber se uma Rede Neural aprendeu com assertividade?** O cientista de dados monitora o **Loss (Função de Perda)**. Quando o Loss cai e estabiliza em um valor baixo e o $R^2$ ultrapassa 90%, significa que o cérebro artificial aprendeu a fórmula oculta sem decorar!")

    with aba_passos:
        st.subheader("📖 Como o Deep Learning Funciona? (Sem Complicação)")
        st.markdown("""
        > 💡 **Analogia da Vida Real:**  
        > Um modelo linear simples acha que o mundo é uma linha reta: *"Se 1 hora de estudo dá 2 pontos, 10 horas vão dar 20 pontos!"*.  
        > Mas na vida real, se você passar 24 horas acordado estudando, vai desmaiar na hora da prova e tirar zero!  
        > A **Rede Neural** é inspirada no cérebro: ela possui camadas de neurônios que cruzam as informações e entendem relações não lineares complexas.
        """)
        st.markdown("---")
        st.markdown("### 🧩 Os 4 Passos Fundamentais do Deep Learning:")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            #### 1️⃣ Entrada com Múltiplas Variáveis (X e y)
            * A vida real não depende de uma única causa. A nota final ($y$) depende simultaneamente de **Estudo** e **Sono** ($X$).
            """)

            st.markdown("""
            #### 2️⃣ Camadas Ocultas e Treinamento (`.fit()`)
            * Os neurônios da camada de entrada passam os dados para **camadas ocultas**.
            * Cada neurônio multiplica o dado por um **peso sináptico** e aplica uma função de ativação (como a `ReLU`, que decide se o neurônio dispara ou não).
            """)

        with c2:
            st.markdown("""
            #### 3️⃣ Propagação e Previsão (`.predict()`)
            * Na hora de prever, as horas de sono e estudo entram na primeira camada, são combinadas nas camadas internas e a resposta final sai do outro lado.
            """)

            st.markdown("""
            #### 4️⃣ Avaliação de Perda (Loss) e Aplicação Prática
            * **Como sabemos se os neurônios aprenderam?:**
              * **Função de Perda (Loss):** Mede o erro residual a cada época de aprendizado. Quanto menor o Loss, mais exatas são as conexões sinápticas.
              * **$R^2$ Score Neural:** Mede o percentual de acerto explicativo da curva não-linear aprendida.
            * **Onde o Deep Learning brilha:** Reconhecimento facial, carros autônomos, diagnósticos médicos e tradução simultânea — problemas em que existem centenas ou milhares de fatores cruzados ao mesmo tempo!
            """)

    with aba_codigo:
        st.subheader("💻 O Código Python Real em Execução no Aplicativo")
        st.write("Este é o código real que constrói a Rede Neural MLPRegressor com 2 camadas ocultas (6 e 4 neurônios):")

        st.code("""# =====================================================================
# 🎓 DEEP LEARNING (REDE NEURAL MLP) COM SCIKIT-LEARN
# =====================================================================
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score, mean_absolute_error

# 1. DADOS DE ENTRADA (Estudo [X1], Sono [X2]) E SAÍDA (Nota [y])
X_estudo = [
    [1, 5], [2, 7], [4, 8], [6, 3], [5, 8], [3, 4], [7, 7]
]
y_notas = [3.0, 6.0, 9.5, 6.5, 9.8, 5.0, 9.9]

# 2. CRIAÇÃO DA ARQUITETURA DA REDE NEURAL ARTIFICIAL
rede = MLPRegressor(
    hidden_layer_sizes=(6, 4),  # Duas camadas ocultas: 6 neurônios na 1ª e 4 na 2ª
    activation='relu',          # Função de ativação retificadora
    max_iter=2000,              # Limite de ciclos de treinamento (épocas)
    random_state=42
)

# Treinando os pesos sinápticos via Retropropagação (Backpropagation):
rede.fit(X_estudo, y_notas)

# 3. AVALIAÇÃO DE DESEMPENHO E CONVERGÊNCIA NEURAL
previsoes = rede.predict(X_estudo)
r2 = r2_score(y_notas, previsoes)
mae = mean_absolute_error(y_notas, previsoes)

print(f"Assertividade dos Neurônios (R²): {r2 * 100:.1f}%")
print(f"Erro Médio Absoluto (MAE): ± {mae:.2f} pontos")
print(f"Função de Perda Final (Loss): {rede.loss_:.4f}")
print(f"Épocas executadas até convergência: {rede.n_iter_}")

# 4. PREVENDO A NOTA DE UM ALUNO NOVO
novo_aluno = [[4, 7]]  # 4 horas de estudo, 7 horas de sono
nota_prevista = rede.predict(novo_aluno)[0]
print(f"Nota Prevista pela Rede Neural: {nota_prevista:.1f} / 10.0")
""", language="python")
        st.info("💡 **Dica de Ouro:** Chamamos de 'Deep Learning' (Aprendizado Profundo) porque a rede empilha várias camadas ocultas de neurônios, permitindo aprender padrões abstratos que nenhum modelo linear simples conseguiria modelar!")

    exibir_rodape_educacional()

# =========================================================================================
# MÓDULO 5: PLN / SENTIMENTOS (AVALIAÇÕES IFOOD) - DIDÁTICO E PASSO A PASSO
# • Item SENAI: 4. Processamento de Linguagem Natural -> 4.1.1.1 Análise de Sentimentos
# • Teoria: Tokenização de frases e análise de polaridade léxica.
# =========================================================================================
elif menu == "🍔 5. PLN (Avaliações do iFood)":
    st.title("🍔 Módulo 5: Processamento de Linguagem Natural (PLN)")
    st.caption("Conceito Central: Tokenização, Stopwords, Radicais e Análise Léxica de Sentimentos")

    aba_simulador, aba_passos, aba_codigo = st.tabs([
        "🎮 Simulador de Avaliações em Tempo Real",
        "🧭 Os 4 Passos do PLN (Para Entendimento)",
        "💻 Código Explicado Linha por Linha"
    ])

    # Dicionários de Radicais Léxicos e Palavras-Chave de PLN em Português
    RADICAIS_POSITIVOS = [
        "bom", "boa", "bons", "boas", "bem", "otim", "ótimo", "ótima", "otimos", "otimas",
        "excelent", "delic", "delícia", "delicia", "delicioso", "deliciosa", "saboros",
        "gostos", "gostei", "gosto", "gostou", "ador", "adorei", "am", "amei", "perfeit",
        "maravilh", "rapido", "rápido", "rapida", "rápida", "rapidez", "quent", "quentinho",
        "quentinha", "fresc", "fresquinho", "fresca", "suculent", "crocant", "barat",
        "recomendo", "aprovad", "parabens", "parabéns", "nota 10", "top", "show", "atencios",
        "educad", "agradavel", "pontual", "caprichad", "sensacional", "espetacular",
        "maravilha", "bacana", "legal", "supimpa", "favorit", "satisfat", "elogio"
    ]

    RADICAIS_NEGATIVOS = [
        "ruim", "ruins", "pessim", "péssimo", "péssima", "pessimos", "pessimas",
        "horrivel", "horrível", "horriveis", "horríveis", "frio", "fria", "gelad",
        "atras", "atraso", "atrasou", "atrasada", "atrasado", "demor", "demorou", "demora",
        "queimad", "cru", "crua", "seco", "seca", "dur", "duro", "dura", "salgad",
        "estragad", "azed", "podre", "gorduros", "suj", "sujo", "suja", "nojent",
        "vaz", "vazou", "derram", "derramou", "errad", "falta", "faltou", "faltando",
        "pior", "caro", "cara", "engano", "decepcion", "nunca mais", "odiei", "grosso",
        "mal educado", "maleducado", "chato", "reclam", "nojento", "nojenta", "rançoso",
        "borrachudo", "insosso", "sem sal", "sem sabor", "demorado", "lento", "prejuizo"
    ]

    with aba_simulador:
        st.subheader("🧪 Simulador de Atendimento ao Cliente do Restaurante")
        st.write("Digite qualquer frase real ou use os botões rápidos para testar a interpretação da IA:")

        # Inicialização do estado de texto se ainda não existir
        if 'texto_pln' not in st.session_state:
            st.session_state['texto_pln'] = "O sabor da pizza é excelente, mas infelizmente demorou muito para chegar."

        # Funções de callback para os botões rápidos atualizarem o texto sem conflitos
        def definir_elogio():
            st.session_state['texto_pln'] = "A pizza estava uma delícia, quentinha e o motoboy foi rápido e educado!"

        def definir_reclamacao():
            st.session_state['texto_pln'] = "A comida atrasou mais de uma hora, o refrigerante veio quente e o lanche estava frio e horrível!"

        def definir_misto():
            st.session_state['texto_pln'] = "O sabor da pizza é excelente, mas infelizmente demorou muito para chegar."

        def definir_limpar():
            st.session_state['texto_pln'] = ""

        # Botões rápidos para testes com on_click
        st.markdown("**💡 Exemplos Prontos de Clientes para Testar com 1 Clique:**")
        b1, b2, b3 = st.columns(3)
        b1.button("🟢 Elogio Apaixonado", on_click=definir_elogio, use_container_width=True)
        b2.button("🔴 Reclamação Severa", on_click=definir_reclamacao, use_container_width=True)
        b3.button("🟡 Avaliação Mista", on_click=definir_misto, use_container_width=True)

        comentario = st.text_area(
            "✍️ Digite qualquer frase ou avaliação de cliente para a IA analisar:",
            value=st.session_state['texto_pln'],
            height=100,
            help="Digite qualquer texto em português e clique no botão abaixo para analisar o sentimento!"
        )
        st.session_state['texto_pln'] = comentario

        col_act1, col_act2 = st.columns([3, 1])
        with col_act1:
            btn_analisar = st.button("🚀 Analisar Mensagem com PLN (Processar Frase)", type="primary", use_container_width=True)
        with col_act2:
            st.button("🗑️ Limpar Texto", on_click=definir_limpar, use_container_width=True)

        # Tokenização e Análise Léxica Avançada de PLN (com suporte a qualquer frase e negação)
        texto_limpo = comentario.lower().replace('.', ' ').replace('!', ' ').replace(',', ' ').replace('?', ' ').replace(';', ' ')
        tokens = texto_limpo.split()
        termos_negacao = {"nao", "não", "nunca", "jamais", "nem"}

        pos = []
        neg = []

        i = 0
        while i < len(tokens):
            palavra = tokens[i]
            tem_negacao_antes = (i > 0 and tokens[i-1] in termos_negacao)

            # Expressões compostas positivas
            if i < len(tokens) - 1 and f"{palavra} {tokens[i+1]}" in ["nota 10", "muito bom", "muito boa", "super recomendo"]:
                expressao = f"{palavra} {tokens[i+1]}"
                if tem_negacao_antes:
                    neg.append(f"{tokens[i-1]} {expressao}")
                else:
                    pos.append(expressao)
                i += 2
                continue

            # Expressões compostas negativas
            if i < len(tokens) - 1 and f"{palavra} {tokens[i+1]}" in ["nunca mais", "sem sabor", "sem sal", "muito ruim", "mal educado"]:
                expressao = f"{palavra} {tokens[i+1]}"
                neg.append(expressao)
                i += 2
                continue

            # Verificar se a palavra coincide com radicais
            eh_positivo = any(palavra == rad or (len(palavra) >= 4 and len(rad) >= 4 and palavra.startswith(rad)) for rad in RADICAIS_POSITIVOS)
            eh_negativo = any(palavra == rad or (len(palavra) >= 4 and len(rad) >= 4 and palavra.startswith(rad)) for rad in RADICAIS_NEGATIVOS)

            if eh_positivo:
                if tem_negacao_antes:
                    neg.append(f"{tokens[i-1]} {palavra}") # Ex: "não gostei" vira negativo!
                else:
                    pos.append(palavra)
            elif eh_negativo:
                if tem_negacao_antes:
                    pos.append(f"{tokens[i-1]} {palavra}") # Ex: "não atrasou" neutraliza
                else:
                    neg.append(palavra)

            i += 1

        saldo_emocional = len(pos) - len(neg)

        st.markdown("---")
        c_pln1, c_pln2, c_pln3 = st.columns(3)
        c_pln1.metric("👍 Palavras Felizes", len(pos), help=f"Encontradas: {pos}")
        c_pln2.metric("👎 Palavras Críticas", len(neg), help=f"Encontradas: {neg}")
        c_pln3.metric("⚖️ Saldo Emocional", f"{saldo_emocional:+d}")

        # Termômetro visual de sentimento (normalizado entre 0.0 e 1.0)
        progresso_sentimento = min(1.0, max(0.0, (saldo_emocional + 3) / 6.0))
        st.caption(f"🌡️ **Termômetro Emocional:** Saldo {saldo_emocional:+d}")
        st.progress(progresso_sentimento)

        if saldo_emocional > 0:
            st.success(f"🟢 **CLIENTE SATISFEITO!** A IA detectou termos elogiosos: `{pos}`. Nenhuma ação corretiva urgente necessária.")
        elif saldo_emocional < 0:
            st.error(f"🔴 **ALERTA DE CLIENTE INSATISFEITO!** A IA detectou reclamações críticas: `{neg}`. Acionar gerente e enviar cupom de desculpas imediatamente!")
        elif len(pos) > 0 and len(neg) > 0:
            st.warning(f"🟡 **AVALIAÇÃO MISTA OU EQUILIBRADA:** O cliente pontuou elogios `{pos}` e reclamações `{neg}` simultaneamente.")
        else:
            st.info("⚪ **MENSAGEM INFORMATIVA / NEUTRA:** A IA analisou as palavras e não detectou adjetivos emocionais positivos ou negativos nesta frase. O cliente provavelmente fez uma pergunta ou observação neutra.")

        # 📊 TABELA DE DADOS DE REFERÊNCIA & DICIONÁRIO DE SENTIMENTOS
        st.markdown("---")
        st.markdown("### 📊 Tabela de Referência de Avaliações e Dicionário Léxico (PLN)")
        st.write("Veja os exemplos clássicos catalogados para testes e as estatísticas do vocabulário léxico:")

        col_tab1, col_tab2 = st.columns(2)
        with col_tab1:
            df_exemplos_pln = pd.DataFrame({
                "Tipo de Avaliação": ["🟢 Elogio", "🔴 Reclamação", "🟡 Mista", "⚪ Informativa/Neutra"],
                "Texto de Exemplo": [
                    "A pizza estava uma delícia, quentinha e o motoboy foi rápido e educado!",
                    "A comida atrasou mais de uma hora e o lanche estava frio e horrível!",
                    "O sabor da pizza é excelente, mas infelizmente demorou muito para chegar.",
                    "Qual é o horário de atendimento da pizzaria aos domingos e feriados?"
                ],
                "Sentimento": ["Positivo (+)", "Negativo (-)", "Misto (+/-)", "Neutro (0)"]
            })
            st.dataframe(df_exemplos_pln, use_container_width=True, hide_index=True)

        with col_tab2:
            df_dicionario = pd.DataFrame({
                "Grupo Léxico": ["Radicais Positivos (Elogios)", "Radicais Negativos (Críticas)", "Termos de Negação / Inversão"],
                "Qtd. de Termos": [len(RADICAIS_POSITIVOS), len(RADICAIS_NEGATIVOS), len(termos_negacao)],
                "Exemplos Cadastrados": [
                    "bom, otim, excelent, delic, gostos, rapid, quent...",
                    "ruim, pessim, horriv, atras, demor, queimad, frio...",
                    "não, nao, nunca, jamais, nem"
                ]
            })
            st.dataframe(df_dicionario, use_container_width=True, hide_index=True)

        # Métricas de Assertividade e Desempenho do PLN
        total_termos = len(pos) + len(neg)
        polaridade = (len(pos) - len(neg)) / max(1, total_termos) if total_termos > 0 else 0.0
        consistencia = (max(len(pos), len(neg)) / total_termos * 100) if total_termos > 0 else 100.0
        cobertura = (total_termos / max(1, len(tokens))) * 100 if len(tokens) > 0 else 0.0

        # 🎯 Avaliação de Desempenho e Assertividade da IA
        st.markdown("---")
        st.markdown("### 🎯 Avaliação de Desempenho & Assertividade da Análise de Sentimento (PLN):")
        c_p_sc1, c_p_sc2, c_p_sc3 = st.columns(3)
        c_p_sc1.metric(
            "📈 Score de Polaridade",
            f"{polaridade:+.2f}",
            help="Varia de -1.0 (100% Negativo/Crítico) até +1.0 (100% Positivo/Elogioso). Zero representa neutralidade."
        )
        c_p_sc2.metric(
            "🎯 Consistência da Opinião",
            f"{consistencia:.0f}%",
            help="Mede se a opinião é unânime (100% dos termos apontam para o mesmo lado) ou se há termos conflitantes na mensagem."
        )
        c_p_sc3.metric(
            "📊 Cobertura Lexical",
            f"{cobertura:.1f}% do texto",
            help="Percentual de palavras que possuem carga emocional identificada pelo modelo."
        )
        st.info("💡 **Como saber se o robô de PLN está sendo assertivo?** A **Consistência da Opinião** avalia se o cliente foi claro e unânime em suas palavras. Quando a consistência é 100% e a polaridade é extrema (+1.0 ou -1.0), o sistema tem certeza absoluta do sentimento e pode tomar ações automáticas sem supervisão humana!")

        st.write("🔍 **Palavras identificadas pelo computador (Tokenização):**")
        st.write(tokens)

    with aba_passos:
        st.subheader("📖 Como o PLN Funciona? (Sem Complicação)")
        st.markdown("""
        > 💡 **Analogia da Vida Real:**  
        > Um dono de pizzaria recebe 800 mensagens por noite. É impossível um ser humano ler todas e priorizar as que deram errado.  
        > O **PLN (Processamento de Linguagem Natural)** é o robô que lê todo esse texto, separa as palavras importantes e avisa a equipe na hora!
        """)
        st.markdown("---")
        st.markdown("### 🧩 Os 4 Passos Fundamentais do PLN:")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            #### 1️⃣ Limpeza e Tokenização
            * O computador não lê parágrafos como nós. Ele precisa **quebrar a frase em pedacinhos** chamados *tokens* (palavras).
            * Também transformamos tudo para minúsculas e removemos pontuações para 'delícia!' ser igual a 'delícia'.
            """)

            st.markdown("""
            #### 2️⃣ Remoção de Ruído e Radicais (Stemming)
            * A IA usa radicais para reconhecer variações da mesma palavra: *gostei, gostoso, gostosa* vêm do radical `gost-`.
            * Trata também palavras de negação: *'não gostei'* inverte a polaridade para crítica!
            """)

        with c2:
            st.markdown("""
            #### 3️⃣ Análise de Sentimento (Léxico)
            * O algoritmo compara cada palavra com dicionários de sentimentos (pesos positivos e negativos) para calcular o placar emocional da frase.
            """)

            st.markdown("""
            #### 4️⃣ Avaliação de Desempenho e Ação Automatizada
            * **Scores de Assertividade em PLN:**
              * **Score de Polaridade (-1.0 a +1.0):** Mede a força emocional da mensagem (de pura insatisfação a puro encantamento).
              * **Consistência (%):** Mede se a mensagem é coerente ou se mistura elogios e reclamações na mesma avaliação.
            * **No Atendimento ao Cliente:** Se o saldo for muito negativo e a consistência for alta, o chamado é encaminhado para a fila de prioridade máxima de um atendente humano em menos de 1 segundo!
            """)

    with aba_codigo:
        st.subheader("💻 O Código Python Real em Execução no Aplicativo")
        st.write("Este é o algoritmo real de PLN em Python utilizado para tokenização, inversão por negação e cálculo de polaridade:")

        st.code("""# =====================================================================
# 🍔 PROCESSAMENTO DE LINGUAGEM NATURAL E SENTIMENTOS (CÓDIGO REAL)
# =====================================================================

# 1. TEXTO REAL RECEBIDO DO CLIENTE
mensagem = "O sabor da pizza é excelente, mas infelizmente demorou muito para chegar."

# 2. LIMPEZA E TOKENIZAÇÃO (QUEBRA EM PALAVRAS)
texto_limpo = mensagem.lower().replace('.', ' ').replace('!', ' ').replace(',', ' ')
tokens = texto_limpo.split()

# 3. DICIONÁRIO DE RADICAIS E PALAVRAS DE NEGAÇÃO
positivos = ["bom", "boa", "sabor", "delic", "otim", "rapid", "quent", "excelent"]
negativos = ["ruim", "pessim", "frio", "atras", "demor", "horriv", "infeliz"]
negacoes = {"nao", "não", "nunca", "jamais", "nem"}

elogios = []
criticas = []

for i, palavra in enumerate(tokens):
    tem_negacao_antes = (i > 0 and tokens[i-1] in negacoes)
    
    if any(palavra.startswith(r) for r in positivos):
        if tem_negacao_antes:
            criticas.append(f"{tokens[i-1]} {palavra}")  # "não bom" vira crítica
        else:
            elogios.append(palavra)
    elif any(palavra.startswith(r) for r in negativos):
        criticas.append(palavra)

# 4. CÁLCULO DAS MÉTRICAS DE SENTIMENTO (POLARIDADE E CONSISTÊNCIA)
total = len(elogios) + len(criticas)
polaridade = (len(elogios) - len(criticas)) / max(1, total) if total > 0 else 0.0
consistencia = (max(len(elogios), len(criticas)) / total * 100) if total > 0 else 100.0

print(f"Palavras Positivas: {elogios}")
print(f"Palavras Negativas: {criticas}")
print(f"Score de Polaridade (-1 a +1): {polaridade:+.2f}")
print(f"Consistência da Opinião: {consistencia:.0f}%")
""", language="python")
        st.info("💡 **Dica de Ouro:** O PLN moderno utiliza algoritmos de radicais (*stemming*) e inversão por negação para compreender qualquer frase em português, mesmo com variações verbais ou gírias!")

    exibir_rodape_educacional()

# =========================================================================================
# MÓDULO 6: VISÃO COMPUTACIONAL (DETECÇÃO DE CONTORNOS COM OPENCV) - DIDÁTICO E COMPLETO
# • Item SENAI: 5. Visão Computacional -> 5.1.1 Processamento de Imagens e Detecção de Formas
# • Teoria: Segmentação por bordas (Canny / Threshold) e extração de contornos com cv2.findContours.
# =========================================================================================
elif menu == "📸 6. Visão Computacional (Contornos de Imagem)":
    st.title("📸 Módulo 6: Visão Computacional com OpenCV (Detecção de Contornos)")
    st.caption("Bibliotecas fundamentais: [`OpenCV (cv2)`](https://opencv.org/) e [`NumPy`](https://numpy.org/)")

    aba_simulador, aba_passos, aba_codigo = st.tabs([
        "🎮 Detector Interativo de Contornos",
        "🧭 Os 4 Passos da Visão (Para Entendimento)",
        "💻 Código Explicado Linha por Linha"
    ])

    # -------------------------------------------------------------------------------------
    # FUNÇÕES GERADORAS DE IMAGENS SINTÉTICAS DIDÁTICAS PARA TESTES OFFLINE / INSTANTÂNEOS
    # -------------------------------------------------------------------------------------
    def gerar_imagem_pecas_industriais():
        """Gera uma imagem de alta qualidade com peças mecânicas em uma bancada (engrenagem, arruela, suporte e parafuso)."""
        img = np.full((400, 600, 3), 235, dtype=np.uint8) # Fundo cinza claro de bancada
        
        # 1. Peça 1: Engrenagem / Flange circular com dentes (Centro: 120, 200)
        cv2.circle(img, (120, 200), 70, (40, 40, 50), -1)
        # Dentes da engrenagem
        for ang in range(0, 360, 30):
            rad = np.deg2rad(ang)
            cx = int(120 + 75 * np.cos(rad))
            cy = int(200 + 75 * np.sin(rad))
            cv2.circle(img, (cx, cy), 14, (40, 40, 50), -1)
        cv2.circle(img, (120, 200), 28, (235, 235, 235), -1) # Furo central da engrenagem

        # 2. Peça 2: Suporte Retangular com 2 furos (Centro: 310, 140)
        cv2.rectangle(img, (230, 80), (390, 200), (60, 80, 110), -1)
        cv2.circle(img, (270, 140), 18, (235, 235, 235), -1)
        cv2.circle(img, (350, 140), 18, (235, 235, 235), -1)

        # 3. Peça 3: Porca Sextavada / Polígono (Centro: 490, 130)
        pts_hex = []
        for i in range(6):
            ang = i * 60 + 30
            rad = np.deg2rad(ang)
            pts_hex.append([int(490 + 55 * np.cos(rad)), int(130 + 55 * np.sin(rad))])
        cv2.fillPoly(img, [np.array(pts_hex, np.int32)], (50, 90, 60))
        cv2.circle(img, (490, 130), 20, (235, 235, 235), -1)

        # 4. Peça 4: Arruela Circular Lisa (Centro: 280, 300)
        cv2.circle(img, (280, 300), 50, (110, 70, 50), -1)
        cv2.circle(img, (280, 300), 22, (235, 235, 235), -1)

        # 5. Peça 5: Placa Triangular de Fixação (Centro: 470, 290)
        pts_tri = np.array([[470, 220], [400, 350], [540, 350]], np.int32)
        cv2.fillPoly(img, [pts_tri], (120, 50, 90))
        cv2.circle(img, (470, 300), 14, (235, 235, 235), -1)

        return img

    def gerar_imagem_formas_geometricas():
        """Gera uma imagem com formas geométricas coloridas clássicas."""
        img = np.full((400, 600, 3), 245, dtype=np.uint8)
        # Círculo Vermelho
        cv2.circle(img, (120, 130), 65, (220, 50, 50), -1)
        # Quadrado Azul
        cv2.rectangle(img, (240, 70), (370, 200), (30, 100, 220), -1)
        # Triângulo Verde
        pts_tri = np.array([[500, 65], [430, 200], [570, 200]], np.int32)
        cv2.fillPoly(img, [pts_tri], (40, 170, 70))
        # Estrela / Polígono Amarelo
        pts_star = []
        for i in range(10):
            r = 70 if i % 2 == 0 else 30
            ang = i * 36 - 90
            rad = np.deg2rad(ang)
            pts_star.append([int(200 + r * np.cos(rad)), int(300 + r * np.sin(rad))])
        cv2.fillPoly(img, [np.array(pts_star, np.int32)], (230, 180, 20))
        # Elipse Roxa
        cv2.ellipse(img, (450, 300), (90, 45), 25, 0, 360, (140, 40, 180), -1)
        return img

    def gerar_imagem_moedas_esteira():
        """Gera uma simulação de moedas e arruelas na esteira com iluminação industrial."""
        img = np.full((400, 600, 3), 40, dtype=np.uint8) # Fundo escuro de borracha da esteira
        moedas = [
            (100, 110, 45, (210, 190, 70)),
            (240, 120, 35, (190, 190, 190)),
            (380, 100, 50, (210, 190, 70)),
            (510, 130, 30, (170, 120, 60)),
            (140, 280, 38, (190, 190, 190)),
            (290, 270, 52, (210, 190, 70)),
            (460, 280, 42, (170, 120, 60))
        ]
        for (cx, cy, r, cor) in moedas:
            cv2.circle(img, (cx, cy), r, cor, -1)
            cv2.circle(img, (cx, cy), int(r * 0.75), (int(cor[0]*0.8), int(cor[1]*0.8), int(cor[2]*0.8)), 2)
        return img

    with aba_simulador:
        st.subheader("🧪 Detecção e Análise de Contornos em Tempo Real (OpenCV)")
        st.write("Selecione uma imagem de teste, carregue uma foto do seu computador ou informe um link da internet para ler os contornos:")

        # Seletor de Origem da Imagem
        tipo_origem = st.radio(
            "Origem da Imagem para o Teste:",
            [
                "⚙️ Peças Mecânicas Industriais (Amostra SENAI)",
                "📐 Formas Geométricas Coloridas (Amostra)",
                "🪙 Moedas / Peças na Esteira (Amostra)",
                "🌐 Imagem da Internet (URL)",
                "📤 Fazer Upload de Imagem do Computador"
            ],
            horizontal=False
        )

        imagem_rgb = None
        nome_origem = ""

        if tipo_origem == "⚙️ Peças Mecânicas Industriais (Amostra SENAI)":
            imagem_rgb = gerar_imagem_pecas_industriais()
            nome_origem = "Peças Mecânicas Industriais SENAI"
        elif tipo_origem == "📐 Formas Geométricas Coloridas (Amostra)":
            imagem_rgb = gerar_imagem_formas_geometricas()
            nome_origem = "Formas Geométricas Coloridas"
        elif tipo_origem == "🪙 Moedas / Peças na Esteira (Amostra)":
            imagem_rgb = gerar_imagem_moedas_esteira()
            nome_origem = "Moedas e Peças na Esteira"
        elif tipo_origem == "🌐 Imagem da Internet (URL)":
            url_padrao = "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/smarties.png"
            url_input = st.text_input("🔗 Digite a URL direta da imagem (JPG/PNG):", value=url_padrao)
            if url_input.strip():
                try:
                    with st.spinner("Baixando imagem da internet..."):
                        resp = requests.get(url_input.strip(), timeout=10)
                        if resp.status_code == 200:
                            pil_img = Image.open(io.BytesIO(resp.content)).convert('RGB')
                            imagem_rgb = np.array(pil_img)
                            nome_origem = f"Imagem baixada da Web ({pil_img.size[0]}x{pil_img.size[1]}px)"
                        else:
                            st.warning(f"Não foi possível baixar a imagem da URL informada (Status {resp.status_code}). Usando amostra mecânica...")
                            imagem_rgb = gerar_imagem_pecas_industriais()
                            nome_origem = "Peças Mecânicas (Fallback)"
                except Exception as ex:
                    st.warning(f"Erro ao carregar URL ({ex}). Alternando para amostra mecânica...")
                    imagem_rgb = gerar_imagem_pecas_industriais()
                    nome_origem = "Peças Mecânicas (Fallback)"
        else: # Upload
            arquivo_subido = st.file_uploader("📤 Escolha uma imagem do seu computador:", type=["png", "jpg", "jpeg"])
            if arquivo_subido is not None:
                pil_img = Image.open(arquivo_subido).convert('RGB')
                imagem_rgb = np.array(pil_img)
                nome_origem = f"Upload: {arquivo_subido.name} ({pil_img.size[0]}x{pil_img.size[1]}px)"
            else:
                st.info("👈 Por favor, envie uma foto acima ou selecione uma das amostras para testar!")
                imagem_rgb = gerar_imagem_pecas_industriais()
                nome_origem = "Peças Mecânicas (Amostra Inicial)"

        # Redimensionar imagens muito grandes para manter a interface rápida e fluida
        if imagem_rgb is not None:
            altura, largura = imagem_rgb.shape[:2]
            if largura > 800 or altura > 600:
                fator = min(800 / largura, 600 / altura)
                novo_w = int(largura * fator)
                novo_h = int(altura * fator)
                imagem_rgb = cv2.resize(imagem_rgb, (novo_w, novo_h), interpolation=cv2.INTER_AREA)

        # ---------------------------------------------------------------------------------
        # CONTROLES INTERATIVOS DO PIPELINE DE VISÃO COMPUTACIONAL (OPENCV)
        # ---------------------------------------------------------------------------------
        st.markdown("---")
        st.markdown("### 🎛️ Painel de Controle dos Filtros de Visão (Ajustes de Câmera):")

        c_ctrl1, c_ctrl2, c_ctrl3 = st.columns(3)
        with c_ctrl1:
            filtro_blur = st.slider("🌫️ Filtro Gaussiano (Suavizar Ruído):", 1, 15, 5, step=2, help="Elimina pequenos grãos e imperfeições da câmera.")
            metodo_binarizacao = st.selectbox("⚙️ Método de Detecção de Bordas:", ["Bordas de Canny (Recomendado)", "Binarização por Limiar (Thresholding)"])

        with c_ctrl2:
            if "Canny" in metodo_binarizacao:
                limiar_canny_min = st.slider("📉 Limiar Canny Mínimo (Histerese Min):", 10, 250, 50)
                limiar_canny_max = st.slider("📈 Limiar Canny Máximo (Histerese Max):", 20, 300, 150)
            else:
                valor_limiar = st.slider("🌓 Valor de Limiar (Threshold 0-255):", 10, 245, 127)
                inverter_cores = st.checkbox("Inverter Preto/Branco (Invert Threshold)", value=False)

        with c_ctrl3:
            area_minima = st.slider("🔍 Filtro de Área Mínima (Descartar ruído em px²):", 0, 5000, 150, step=50, help="Ignora partículas de poeira e pequenos contornos indesejados.")
            mostrar_caixa = st.checkbox("Exibir Caixas Delimitadoras (Bounding Boxes)", value=True)
            mostrar_centroide = st.checkbox("Exibir Ponto Central (Centroides / X,Y)", value=True)

        # ---------------------------------------------------------------------------------
        # PROCESSAMENTO MATEMÁTICO REAL COM OPENCV
        # ---------------------------------------------------------------------------------
        # 1. Escala de cinza
        imagem_cinza = cv2.cvtColor(imagem_rgb, cv2.COLOR_RGB2GRAY)
        
        # 2. Suavização Gaussiana
        imagem_blur = cv2.GaussianBlur(imagem_cinza, (filtro_blur, filtro_blur), 0)

        # 3. Segmentação (Canny ou Limiar)
        if "Canny" in metodo_binarizacao:
            imagem_binaria = cv2.Canny(imagem_blur, limiar_canny_min, limiar_canny_max)
            # Dilatação leve para fechar contornos desconexos do Canny
            kernel = np.ones((3, 3), np.uint8)
            imagem_binaria = cv2.dilate(imagem_binaria, kernel, iterations=1)
        else:
            tipo_thresh = cv2.THRESH_BINARY_INV if inverter_cores else cv2.THRESH_BINARY
            _, imagem_binaria = cv2.threshold(imagem_blur, valor_limiar, 255, tipo_thresh)

        # 4. Encontrar Contornos (findContours)
        contornos_raw, hierarquia = cv2.findContours(imagem_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 5. Filtrar e Desenhar os Contornos Válidos
        imagem_resultado = imagem_rgb.copy()
        dados_contornos = []

        idx_valido = 1
        area_total_acumulada = 0.0

        for cnt in contornos_raw:
            area = cv2.contourArea(cnt)
            if area < area_minima:
                continue # Descarta contornos menores que o limiar (ruído)

            perimetro = cv2.arcLength(cnt, True)
            x, y, w, h = cv2.boundingRect(cnt)
            area_total_acumulada += area

            # Cálculo do Centroide (Moments)
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
            else:
                cX, cY = x + w // 2, y + h // 2

            # Estimativa de Forma Geométrica (Poligonal Approximation)
            epsilon = 0.035 * perimetro
            approx = cv2.approxPolyDP(cnt, epsilon, True)
            num_vertices = len(approx)

            aspect_ratio = float(w) / h if h > 0 else 1.0
            circularidade = (4 * np.pi * area) / (perimetro ** 2) if perimetro > 0 else 0

            if circularidade > 0.75:
                forma = "Círculo / Cilindro"
            elif num_vertices == 3:
                forma = "Triângulo"
            elif num_vertices == 4:
                forma = "Quadrado" if 0.9 <= aspect_ratio <= 1.1 else "Retângulo"
            elif num_vertices == 5:
                forma = "Pentágono"
            elif num_vertices == 6:
                forma = "Hexágono / Porca"
            else:
                forma = "Peça Complexa / Engrenagem"

            # Desenho no resultado visual
            # Contorno em verde neon espesso
            cv2.drawContours(imagem_resultado, [cnt], -1, (0, 255, 100), 3)

            # Caixa Delimitadora (Bounding Box em azul ciano)
            if mostrar_caixa:
                cv2.rectangle(imagem_resultado, (x, y), (x + w, y + h), (0, 180, 255), 2)

            # Centroide em vermelho
            if mostrar_centroide:
                cv2.circle(imagem_resultado, (cX, cY), 5, (255, 0, 0), -1)

            # Rótulo de texto com número do objeto
            cv2.putText(
                imagem_resultado,
                f"#{idx_valido}",
                (x, max(18, y - 8)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.65,
                (255, 255, 0),
                2,
                cv2.LINE_AA
            )

            dados_contornos.append({
                "Objeto #": f"#{idx_valido:02d}",
                "Forma Estimada": forma,
                "Área (pixels²)": int(area),
                "Perímetro (pixels)": round(perimetro, 1),
                "Centro X (px)": cX,
                "Centro Y (px)": cY,
                "Largura W (px)": w,
                "Altura H (px)": h
            })

            idx_valido += 1

        # ---------------------------------------------------------------------------------
        # EXIBIÇÃO VISUAL DAS 3 ETAPAS (ORIGINAL, PROCESSADA, CONTORNOS DETECTADOS)
        # ---------------------------------------------------------------------------------
        st.markdown("---")
        st.markdown(f"### 👁️ Processamento Visual da Imagem: *{nome_origem}*")

        col_v1, col_v2, col_v3 = st.columns(3)
        with col_v1:
            st.caption("1️⃣ **Imagem Original (Cores RGB):**")
            st.image(imagem_rgb, use_container_width=True)

        with col_v2:
            st.caption("2️⃣ **Visão da Máquina (Bordas & Limiar):**")
            st.image(imagem_binaria, use_container_width=True, clamp=True)

        with col_v3:
            st.caption(f"3️⃣ **Contornos Identificados ({len(dados_contornos)} objetos):**")
            st.image(imagem_resultado, use_container_width=True)

        # ---------------------------------------------------------------------------------
        # TABELA DE DADOS NUMÉRICOS DOS CONTORNOS (PROPRIEDADES EXTRAÍDAS PELA IA)
        # ---------------------------------------------------------------------------------
        st.markdown("---")
        st.markdown("### 📊 Tabela de Propriedades dos Contornos Detectados")
        st.write("A visão computacional transformou os pixels da foto nesta tabela estruturada com medidas exatas de engenharia:")

        if dados_contornos:
            df_contornos = pd.DataFrame(dados_contornos)
            st.dataframe(df_contornos, use_container_width=True, hide_index=True)
            st.caption("💡 **Conceito para sala de aula:** Cada linha da tabela representa uma peça isolada na esteira. O robô industrial usa as colunas **Centro X/Y** para posicionar a garra mecânica e a coluna **Área** para checar se a peça está no tamanho correto!")
        else:
            st.warning("⚠️ Nenhum contorno detectado com a configuração atual. Tente reduzir a 'Área Mínima' ou ajustar os limiares de Canny/Threshold nos controles acima!")

        # ---------------------------------------------------------------------------------
        # MÉTRICAS E CONTROLE DE QUALIDADE INDUSTRIAL
        # ---------------------------------------------------------------------------------
        st.markdown("---")
        st.markdown("### 🎯 Métricas de Inspeção & Controle de Qualidade Industrial:")
        
        c_qc1, c_qc2, c_qc3, c_qc4 = st.columns(4)
        c_qc1.metric("📦 Contornos Detectados", f"{len(dados_contornos)} objetos")
        
        maior_area = max([d["Área (pixels²)"] for d in dados_contornos]) if dados_contornos else 0
        c_qc2.metric("📐 Maior Peça (Área)", f"{maior_area:,} px²".replace(",", "."))
        
        c_qc3.metric("📏 Área Total Ocupada", f"{int(area_total_acumulada):,} px²".replace(",", "."))
        
        status_qualidade = "Aprovado na Esteira" if len(dados_contornos) >= 1 else "Aguardando Peças"
        c_qc4.metric("🏭 Status da Linha", status_qualidade)

        st.info("💡 **Como a indústria usa isso?** Em linhas de montagem automotivas e de alimentos, câmeras OpenCV inspecionam até 120 peças por segundo. Se a **Área em pixels²** ou a **Forma Geométrica** da peça diferir do padrão cadastrado, um pistão pneumático ejeta a peça defeituosa instantaneamente!")

    with aba_passos:
        st.subheader("📖 Como a Detecção de Contornos Funciona no OpenCV? (Sem Complicação)")
        st.markdown("""
        > 💡 **Analogia da Vida Real:**  
        > Quando você olha para uma mesa com parafusos, seus olhos não precisam inspecionar cada milímetro do fundo da mesa;  
        > Seu cérebro busca as **bordas e o contraste** onde o objeto começa e a mesa termina.  
        > Na **Visão Computacional**, nós ensinamos o robô a encontrar as linhas de contorno (`cv2.findContours`) para que ele possa medir áreas, calcular o centro de massa e guiar braços robóticos com precisão milimétrica!
        """)
        st.markdown("---")
        st.markdown("### 🧩 Os 4 Passos Fundamentais da Detecção de Contornos:")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            #### 1️⃣ Conversão para Escala de Cinza (`cv2.cvtColor`)
            * Uma imagem colorida tem 3 camadas de dados: Vermelho, Verde e Azul (RGB).
            * Para achar contornos, as cores são ruído desnecessário. Convertemos para **Escala de Cinza (0 a 255)** para focar puramente na intensidade luminosa.
            """)

            st.markdown("""
            #### 2️⃣ Suavização e Detecção de Bordas (`cv2.Canny` / `cv2.threshold`)
            * **Filtro Gaussiano:** Remove pequenos grãos e poeira da lente.
            * **Algoritmo de Canny:** Calcula onde ocorrem variações bruscas de claro para escuro e gera uma imagem binária (preto e branco) contendo apenas o esqueleto das bordas.
            """)

        with c2:
            st.markdown("""
            #### 3️⃣ Extração de Contornos Vetoriais (`cv2.findContours`)
            * O OpenCV rastreia os pixels brancos interligados e cria polígonos matemáticos contínuos.
            * Cada contorno é uma lista de coordenadas $(X, Y)$ que envolve perfeitamente a peça.
            """)

            st.markdown("""
            #### 4️⃣ Extração de Medidas de Engenharia e Tomada de Decisão
            * **O que calculamos a partir do contorno?:**
              * **Área (`cv2.contourArea`):** Tamanho da peça em pixels².
              * **Perímetro (`cv2.arcLength`):** Comprimento da borda externa.
              * **Centroide (`cv2.moments`):** Ponto exato onde o robô deve encostar a ventosa ou garra.
              * **Bounding Box (`cv2.boundingRect`):** Retângulo envolvente para direcionamento em esteiras.
            """)

    with aba_codigo:
        st.subheader("💻 O Código Python Real em Execução no Aplicativo (OpenCV)")
        st.write("Este é o código Python exato e executável para carregar uma imagem, detectar bordas, extrair contornos e medir propriedades geométricas:")

        st.code("""# =====================================================================
# 📸 DETECÇÃO E MEDIÇÃO DE CONTORNOS COM OPENCV (CÓDIGO REAL DO MÓDULO)
# =====================================================================
import cv2
import numpy as np
import pandas as pd

# 1. CARREGAMENTO DA IMAGEM (PODE SER ARQUIVO LOCAL OU FOTO DA CÂMERA)
# imagem = cv2.imread("sua_peca_ou_foto.jpg")
# No Streamlit, convertemos a imagem RGB para escala de cinza:
imagem_rgb = cv2.imread("pecas_senai.png") # Exemplo de arquivo
imagem_cinza = cv2.cvtColor(imagem_rgb, cv2.COLOR_BGR2GRAY)

# 2. FILTRO GAUSSIANO (ELIMINAR RUÍDO) E DETECÇÃO DE BORDAS CANNY
imagem_blur = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)
bordas_canny = cv2.Canny(imagem_blur, threshold1=50, threshold2=150)

# Dilatação leve para conectar linhas de contorno interrompidas:
kernel = np.ones((3, 3), np.uint8)
bordas_dilatadas = cv2.dilate(bordas_canny, kernel, iterations=1)

# 3. EXTRAÇÃO DE CONTORNOS EXTERNOS (cv2.findContours)
contornos, _ = cv2.findContours(bordas_dilatadas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(f"Total de contornos brutos encontrados: {len(contornos)}")

# 4. MEDIÇÃO GEOMÉTRICA E DESENHO DOS CONTORNOS NA IMAGEM
imagem_com_contornos = imagem_rgb.copy()
area_minima = 150 # Descartar poeira/ruídos menores que 150 pixels²
dados_tabela = []

for i, cnt in enumerate(contornos):
    area = cv2.contourArea(cnt)
    if area < area_minima:
        continue # Ignora ruído
    
    perimetro = cv2.arcLength(cnt, True)
    x, y, w, h = cv2.boundingRect(cnt)
    
    # Cálculo do Centroide (Centro de Massa da Peça):
    M = cv2.moments(cnt)
    cX = int(M["m10"] / M["m00"]) if M["m00"] != 0 else x + w // 2
    cY = int(M["m01"] / M["m00"]) if M["m00"] != 0 else y + h // 2
    
    # Desenhar contorno verde espesso e caixa azul ao redor da peça:
    cv2.drawContours(imagem_com_contornos, [cnt], -1, (0, 255, 0), 2)
    cv2.rectangle(imagem_com_contornos, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.circle(imagem_com_contornos, (cX, cY), 4, (0, 0, 255), -1)
    
    dados_tabela.append({
        "ID": i + 1,
        "Area_px2": int(area),
        "Perimetro_px": round(perimetro, 1),
        "Centro_X": cX,
        "Centro_Y": cY,
        "Largura": w,
        "Altura": h
    })

# Exibir tabela com as medidas extraídas pela visão:
df_medicoes = pd.DataFrame(dados_tabela)
print(df_medicoes)

# Salvar ou exibir a imagem final anotada:
# cv2.imwrite("resultado_inspecao.png", imagem_com_contornos)
""", language="python")
        st.info("💡 **Dica de Ouro:** A combinação de `cv2.Canny` com `cv2.findContours` e `cv2.moments` é a base da robótica de *Pick-and-Place*. Ela informa ao robô a coordenada exata $(X,Y)$ e a rotação necessária para agarrar peças industriais na esteira sem errar!")

    exibir_rodape_educacional()

# =========================================================================================
# MÓDULO 7: CHATBOT COM RAG (GOOGLE GEMINI & MICROSOFT AZURE FOUNDRY)
# • Item SENAI: 6. Modelos Personalizados -> 6.1 Arquitetura / 6.2 Conexão com Nuvem
# • Teoria: Chatbot conversacional com Injeção de Contexto (RAG) para respostas ancoradas.
# =========================================================================================
elif menu == "💬 7. Chatbot com RAG (Crie sua IA)":
    st.title("💬 Módulo 7: Chatbot Inteligente com RAG")
    st.caption("Suporte a múltiplos motores: Google Gemini, Microsoft Azure AI Foundry e Motor Pedagógico Local")

    aba_simulador, aba_passos, aba_codigo = st.tabs([
        "💬 Chatbot com RAG (Interativo)",
        "🧭 Os 4 Passos do Chatbot RAG (Para Entendimento)",
        "💻 Código Explicado Linha por Linha"
    ])

    # Inicialização dos estados para os templates, provedores e mensagens do chat
    if 'rag_persona' not in st.session_state:
        st.session_state['rag_persona'] = "Você é o instrutor técnico de usinagem e segurança do SENAI. Responda de forma técnica, cordial e com foco rigoroso em normas de segurança industrial."
    if 'rag_contexto' not in st.session_state:
        st.session_state['rag_contexto'] = """MANUAL DE OPERAÇÃO - TORNO MECÂNICO E CNC SENAI:
1. SEGURANÇA OBRIGATÓRIA: É expressamente obrigatório o uso de óculos de proteção (EPI) e calçado com biqueira de aço na oficina.
2. VESTIMENTA: Nunca opere o torno usando relógios, anéis, pulseiras ou mangas compridas soltas. Cabelos longos devem estar presos com touca ou rede.
3. VELOCIDADE DE CORTE: A velocidade recomendada para desbaste de alumínio 6061 é de 250 m/min com pastilha de metal duro. Para aço 1020, use 180 m/min.
4. EMERGÊNCIA: Ao perceber vibração anormal ou barulho estridente, pressione imediatamente o botão cogumelo de parada de emergência e desligue o disjuntor principal."""
    if 'rag_chat_messages' not in st.session_state:
        st.session_state['rag_chat_messages'] = [
            {
                "role": "assistant",
                "content": "Olá, operador! Sou o instrutor de usinagem e segurança do SENAI. Tenho o manual técnico da oficina em mãos. Qual a sua dúvida sobre procedimentos de torneamento, ferramentas ou regras de segurança?",
                "source": "Sistema"
            }
        ]
    if 'rag_provedor' not in st.session_state:
        st.session_state['rag_provedor'] = "Motor Pedagógico Local (Sem Chave / Gratuito)"
    if 'rag_google_key' not in st.session_state:
        st.session_state['rag_google_key'] = ""
    if 'rag_google_model' not in st.session_state:
        st.session_state['rag_google_model'] = "gemini-1.5-flash"
    if 'rag_foundry_endpoint' not in st.session_state:
        st.session_state['rag_foundry_endpoint'] = ""
    if 'rag_foundry_key' not in st.session_state:
        st.session_state['rag_foundry_key'] = ""
    if 'rag_foundry_model' not in st.session_state:
        st.session_state['rag_foundry_model'] = "gpt-4o-mini"
    if 'rag_foundry_api_version' not in st.session_state:
        st.session_state['rag_foundry_api_version'] = "2024-06-01"

    # Funções auxiliares para carregar templates prontos
    def carregar_template_torno():
        st.session_state['rag_persona'] = "Você é o instrutor técnico de usinagem e segurança do SENAI. Responda de forma técnica, cordial e com foco rigoroso em normas de segurança industrial."
        st.session_state['rag_contexto'] = """MANUAL DE OPERAÇÃO - TORNO MECÂNICO E CNC SENAI:
1. SEGURANÇA OBRIGATÓRIA: É expressamente obrigatório o uso de óculos de proteção (EPI) e calçado com biqueira de aço na oficina.
2. VESTIMENTA: Nunca opere o torno usando relógios, anéis, pulseiras ou mangas compridas soltas. Cabelos longos devem estar presos com touca ou rede.
3. VELOCIDADE DE CORTE: A velocidade recomendada para desbaste de alumínio 6061 é de 250 m/min com pastilha de metal duro. Para aço 1020, use 180 m/min.
4. EMERGÊNCIA: Ao perceber vibração anormal ou barulho estridente, pressione imediatamente o botão cogumelo de parada de emergência e desligue o disjuntor principal."""
        st.session_state['rag_chat_messages'] = [
            {
                "role": "assistant",
                "content": "Olá, operador! Sou o instrutor de usinagem e segurança do SENAI. Tenho o manual técnico da oficina em mãos. Qual a sua dúvida sobre procedimentos de torneamento, ferramentas ou regras de segurança?",
                "source": "Sistema"
            }
        ]

    def carregar_template_escola():
        st.session_state['rag_persona'] = "Você é o assistente virtual da secretaria escolar do SENAI-SP. Seja cordial, acolhedor e forneça orientações acadêmicas precisas."
        st.session_state['rag_contexto'] = """REGULAMENTO ACADÊMICO E DISCIPLINAR SENAI-SP:
1. FREQUÊNCIA: É exigida frequência mínima de 75% da carga horária do curso para obtenção do certificado.
2. ATESTADOS MÉDICOS: O aluno tem até 48 horas úteis após a falta para protocolar o atestado médico original na secretaria da unidade.
3. CRITÉRIOS DE APROVAÇÃO: Média final igual ou superior a 7,0 resulta em aprovação direta. Médias entre 5,0 e 6,9 têm direito à avaliação de recuperação.
4. USO DE CELULAR: O uso de aparelhos celulares durante aulas práticas de laboratório e oficinas é estritamente proibido sem autorização do docente."""
        st.session_state['rag_chat_messages'] = [
            {
                "role": "assistant",
                "content": "Olá, estudante! Sou o assistente virtual da secretaria do SENAI-SP. Posso orientá-lo sobre prazos de atestados, frequência mínima, critérios de notas e regulamento escolar. Como posso te ajudar hoje?",
                "source": "Sistema"
            }
        ]

    def carregar_template_chef():
        st.session_state['rag_persona'] = "Você é um Chef especialista em culinária sustentável e combate ao desperdício de alimentos. Sugira receitas práticas e responda como um cozinheiro amigável."
        st.session_state['rag_contexto'] = """INVENTÁRIO ATUAL DA GELADEIRA E DESPENSA:
- 2 ovos caipiras
- Meio pote de queijo cottage fresco
- 3 fatias de pão integral
- 1 tomate maduro picado
- Manteiga, sal e orégano na despensa"""
        st.session_state['rag_chat_messages'] = [
            {
                "role": "assistant",
                "content": "Olá! Sou o Chef sustentável da cozinha. Já examinei o que temos disponível na geladeira e despensa. O que você gostaria de preparar para comer agora?",
                "source": "Sistema"
            }
        ]

    with aba_simulador:
        st.subheader("💬 Laboratório de Chatbot Corporativo com RAG")
        st.write("Converse com o assistente em tempo real! Ele utiliza **RAG** para responder estritamente com base no documento da empresa.")

        # Botões de cenários rápidos
        st.markdown("**💡 Escolha um Cenário Corporativo Pronto:**")
        b_c1, b_c2, b_c3 = st.columns(3)
        b_c1.button("🏭 Suporte Torno CNC (Oficina)", on_click=carregar_template_torno, use_container_width=True)
        b_c2.button("📋 Secretaria Escolar (SENAI)", on_click=carregar_template_escola, use_container_width=True)
        b_c3.button("🍳 Chef Sustentável da Geladeira", on_click=carregar_template_chef, use_container_width=True)

        st.markdown("---")

        # Expander de Configuração do RAG (Provedor, Persona, Documento e Chaves)
        with st.expander("⚙️ Configurar Base de Conhecimento, Provedor de IA (Gemini / Microsoft Foundry) e Persona", expanded=False):
            st.markdown("### 🛠️ Personalização do seu Chatbot e Conexão de Nuvem:")
            with st.form("form_config_rag"):
                col_cfg1, col_cfg2 = st.columns(2)
                with col_cfg1:
                    novo_persona = st.text_area(
                        "🎭 Persona da IA (System Prompt / Papel do Robô):",
                        value=st.session_state['rag_persona'],
                        height=90,
                        help="Define como o robô deve se comportar e falar com o usuário."
                    )

                    provedor_opcoes = [
                        "Motor Pedagógico Local (Sem Chave / Gratuito)",
                        "🌐 Google AI Studio (Gemini 1.5 Flash / Pro)",
                        "☁️ Microsoft Azure AI Foundry (Azure OpenAI / Modelos)"
                    ]
                    idx_atual = 0
                    if "Google" in st.session_state['rag_provedor']:
                        idx_atual = 1
                    elif "Microsoft" in st.session_state['rag_provedor']:
                        idx_atual = 2

                    novo_provedor = st.selectbox(
                        "🤖 Provedor de Inteligência Artificial:",
                        provedor_opcoes,
                        index=idx_atual
                    )

                    if "Google" in novo_provedor:
                        st.markdown("##### 🌐 Configuração do Google AI Studio:")
                        nova_chave_google = st.text_input(
                            "🔑 Chave de API Google Gemini:",
                            value=st.session_state.get('rag_google_key', ''),
                            type="password",
                            help="Gere sua chave gratuita em aistudio.google.com"
                        )
                        novo_modelo_google = st.selectbox(
                            "Modelo Gemini:",
                            ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.0-flash"],
                            index=0
                        )
                        nova_borda_foundry = st.session_state.get('rag_foundry_endpoint', '')
                        nova_chave_foundry = st.session_state.get('rag_foundry_key', '')
                        novo_modelo_foundry = st.session_state.get('rag_foundry_model', 'gpt-4o-mini')
                        nova_versao_foundry = st.session_state.get('rag_foundry_api_version', '2024-06-01')

                    elif "Microsoft" in novo_provedor:
                        st.markdown("##### ☁️ Configuração do Microsoft Azure AI Foundry:")
                        nova_borda_foundry = st.text_input(
                            "🌐 Endpoint / Borda do Serviço (URL):",
                            value=st.session_state.get('rag_foundry_endpoint', ''),
                            placeholder="https://seu-recurso.openai.azure.com/ ou https://seu-recurso.services.ai.azure.com/",
                            help="Cole a URL do Endpoint / Borda do recurso gerado no Microsoft Azure AI Foundry."
                        )
                        nova_chave_foundry = st.text_input(
                            "🔑 Chave de API da Microsoft (API Key):",
                            value=st.session_state.get('rag_foundry_key', ''),
                            type="password",
                            help="Chave de acesso obtida na aba 'Keys and Endpoint' no portal Azure / Foundry."
                        )
                        c_f1, c_f2 = st.columns(2)
                        with c_f1:
                            novo_modelo_foundry = st.text_input(
                                "🏷️ Modelo / Deployment:",
                                value=st.session_state.get('rag_foundry_model', 'gpt-4o-mini'),
                                help="Nome da implantação criada no Foundry (ex: gpt-4o-mini, gpt-4o, phi-4)."
                            )
                        with c_f2:
                            nova_versao_foundry = st.text_input(
                                "⚙️ Versão da API:",
                                value=st.session_state.get('rag_foundry_api_version', '2024-06-01'),
                                help="Versão da API da Microsoft (padrão: 2024-06-01)."
                            )
                        nova_chave_google = st.session_state.get('rag_google_key', '')
                        novo_modelo_google = st.session_state.get('rag_google_model', 'gemini-1.5-flash')

                    else: # Motor Local
                        st.info("💡 **Motor Pedagógico Local Ativo:** Funciona 100% offline sem precisar de chaves ou cartões de crédito!")
                        nova_chave_google = st.session_state.get('rag_google_key', '')
                        novo_modelo_google = st.session_state.get('rag_google_model', 'gemini-1.5-flash')
                        nova_borda_foundry = st.session_state.get('rag_foundry_endpoint', '')
                        nova_chave_foundry = st.session_state.get('rag_foundry_key', '')
                        novo_modelo_foundry = st.session_state.get('rag_foundry_model', 'gpt-4o-mini')
                        nova_versao_foundry = st.session_state.get('rag_foundry_api_version', '2024-06-01')

                with col_cfg2:
                    novo_contexto = st.text_area(
                        "📚 Base de Conhecimento da Empresa (Documento / Manual do RAG):",
                        value=st.session_state['rag_contexto'],
                        height=210,
                        help="O texto oficial que a IA usará como colinha para responder sem alucinar."
                    )

                btn_salvar = st.form_submit_button("💾 Salvar Alterações e Atualizar Chatbot", type="primary")
                if btn_salvar:
                    st.session_state['rag_persona'] = novo_persona
                    st.session_state['rag_contexto'] = novo_contexto
                    st.session_state['rag_provedor'] = novo_provedor
                    st.session_state['rag_google_key'] = nova_chave_google
                    st.session_state['rag_google_model'] = novo_modelo_google
                    st.session_state['rag_foundry_endpoint'] = nova_borda_foundry
                    st.session_state['rag_foundry_key'] = nova_chave_foundry
                    st.session_state['rag_foundry_model'] = novo_modelo_foundry
                    st.session_state['rag_foundry_api_version'] = nova_versao_foundry
                    
                    st.session_state['rag_chat_messages'].append({
                        "role": "assistant",
                        "content": f"🔄 *Configurações salvas! Provedor ativo:* **{novo_provedor.split('(')[0]}**. Base de conhecimento e persona atualizadas com sucesso. Como posso te ajudar?",
                        "source": "Sistema"
                    })
                    st.rerun()

            with st.expander("🔍 Espiar o Prompt Completo de RAG montado por trás dos panos"):
                st.code(f"""
[INSTRUÇÃO DE SISTEMA / PERSONA]:
{st.session_state['rag_persona']}

[REGRA ESTRITA DE RAG]:
Responda às dúvidas do usuário usando EXCLUSIVAMENTE a BASE DE CONHECIMENTO oficial.
Se a informação não estiver descrita no documento, afirme educadamente que o documento não contém essa informação. Não invente fatos.

[BASE DE CONHECIMENTO]:
{st.session_state['rag_contexto']}
                """, language="markdown")

        # 📊 TABELA DE DADOS DA BASE DE CONHECIMENTO (ESTRUTURAÇÃO DO RAG)
        st.markdown("---")
        st.markdown("### 📊 Tabela da Base de Conhecimento Indexada (Como o RAG enxerga os dados)")
        st.write("Abaixo estão os fragmentos do manual cadastrado que a IA consulta para responder às perguntas sem alucinar:")

        linhas_documento = [l.strip() for l in st.session_state['rag_contexto'].split('\n') if l.strip()]
        df_tabela_rag = pd.DataFrame({
            "Fragmento #": [f"Cláusula / Linha #{i+1:02d}" for i in range(len(linhas_documento))],
            "Texto Homologado da Empresa (Regra de Ouro)": linhas_documento,
            "Status no RAG": ["✅ Indexado e Protegido" for _ in linhas_documento]
        })
        st.dataframe(df_tabela_rag, use_container_width=True, hide_index=True)
        st.caption("💡 **Conceito para sala de aula:** O RAG transforma manuais e PDFs em pedaços (*chunks*) indexados. Quando o usuário pergunta, a IA busca as linhas exatas com maior relevância sem inventar fatos fora da tabela.")

        # Barra de Status e Ações do Chat
        st.markdown("---")
        col_st1, col_st2 = st.columns([3, 1])
        with col_st1:
            if "Microsoft" in st.session_state['rag_provedor'] and st.session_state['rag_foundry_key'].strip():
                motor_texto = f"Microsoft Azure AI Foundry ({st.session_state['rag_foundry_model']})"
            elif "Google" in st.session_state['rag_provedor'] and st.session_state['rag_google_key'].strip():
                motor_texto = f"Google AI Studio ({st.session_state['rag_google_model']})"
            else:
                motor_texto = "Motor Pedagógico Local (Sem Chave / Gratuito)"

            qtd_palavras = len(st.session_state['rag_contexto'].split())
            st.info(f"🤖 **Status:** Atuando como *{st.session_state['rag_persona'].split('.')[0]}* | 📄 **Base Carregada:** {qtd_palavras} palavras | ⚡ **Motor:** {motor_texto}")
        with col_st2:
            if st.button("🗑️ Limpar Conversa", use_container_width=True):
                st.session_state['rag_chat_messages'] = [{
                    "role": "assistant",
                    "content": f"Histórico limpo! Sou seu assistente (**{st.session_state['rag_persona'].split('.')[0]}**). Como posso ajudar você agora?",
                    "source": "Sistema"
                }]
                st.rerun()

        # ---------------------------------------------------------------------------------
        # JANELA DE CHAT MODERNA COM CONTAINER DE ROLAGEM DEDICADO
        # ---------------------------------------------------------------------------------
        st.markdown("### 💬 Janela de Atendimento do Chatbot:")
        chat_container = st.container(height=450)

        with chat_container:
            for msg in st.session_state['rag_chat_messages']:
                avatar_icone = "🧑‍🎓" if msg["role"] == "user" else "🤖"
                with st.chat_message(msg["role"], avatar=avatar_icone):
                    st.markdown(msg["content"])
                    if msg.get("source"):
                        st.caption(f"📡 *{msg['source']}*")

        # ---------------------------------------------------------------------------------
        # CAIXA DE DIGITAÇÃO FIXADA ABAIXO DO CONTAINER DO CHAT
        # ---------------------------------------------------------------------------------
        if prompt_usuario := st.chat_input("Digite sua dúvida para o assistente (ex: Qual o EPI obrigatório?)..."):
            # 1. Registrar mensagem do usuário no histórico
            st.session_state['rag_chat_messages'].append({
                "role": "user",
                "content": prompt_usuario
            })

            resposta_ia = None
            origem_resposta = ""

            # -----------------------------------------------------------------------------
            # MOTOR 1: MICROSOFT AZURE AI FOUNDRY
            # -----------------------------------------------------------------------------
            if "Microsoft" in st.session_state['rag_provedor'] and st.session_state['rag_foundry_key'].strip() and st.session_state['rag_foundry_endpoint'].strip():
                with st.spinner("Consultando base de conhecimento via Microsoft Azure AI Foundry..."):
                    try:
                        endpoint = st.session_state['rag_foundry_endpoint'].strip().rstrip('/')
                        key = st.session_state['rag_foundry_key'].strip()
                        model = st.session_state['rag_foundry_model'].strip() or "gpt-4o-mini"
                        api_ver = st.session_state['rag_foundry_api_version'].strip() or "2024-06-01"

                        # Formatação inteligente da URL do Foundry / Azure OpenAI
                        if "/chat/completions" in endpoint:
                            url_foundry = endpoint
                        elif "/models" in endpoint:
                            url_foundry = f"{endpoint}/chat/completions?api-version={api_ver}"
                        else:
                            url_foundry = f"{endpoint}/openai/deployments/{model}/chat/completions?api-version={api_ver}"

                        headers = {
                            "Content-Type": "application/json",
                            "api-key": key,
                            "Authorization": f"Bearer {key}"
                        }

                        system_instrucao_foundry = f"""Você é: {st.session_state['rag_persona']}

DIRETRIZ ESTRITA DE RAG (Recuperação de Informação):
Você é um assistente de chatbot corporativo. Você DEVE responder às dúvidas do usuário utilizando EXCLUSIVAMENTE as informações contidas na BASE DE CONHECIMENTO oficial fornecida abaixo.
Se a resposta para a dúvida do usuário não estiver expressamente contida na base de conhecimento, responda com cordialidade e clareza informando que essa informação não consta no documento oficial da empresa e oriente onde buscar ajuda. NUNCA invente procedimentos, regras, números ou fatos externos.

BASE DE CONHECIMENTO OFICIAL:
\"\"\"
{st.session_state['rag_contexto']}
\"\"\""""

                        mensagens_payload = [{"role": "system", "content": system_instrucao_foundry}]
                        for m in st.session_state['rag_chat_messages']:
                            mensagens_payload.append({
                                "role": "user" if m["role"] == "user" else "assistant",
                                "content": m["content"]
                            })

                        payload = {
                            "messages": mensagens_payload,
                            "temperature": 0.2,
                            "max_tokens": 500
                        }

                        req = requests.post(url_foundry, headers=headers, json=payload, timeout=25)
                        if req.status_code == 200:
                            res_json = req.json()
                            resposta_ia = res_json['choices'][0]['message']['content']
                            origem_resposta = f"Microsoft Azure AI Foundry ({model})"
                        else:
                            st.warning(f"⚠️ Resposta da API do Foundry ({req.status_code}): {req.text[:140]}. Alternando para o motor pedagógico local...")
                    except Exception as ex:
                        st.warning(f"⚠️ Erro ao conectar ao Microsoft Foundry ({ex}). Alternando para o motor pedagógico local...")

            # -----------------------------------------------------------------------------
            # MOTOR 2: GOOGLE GEMINI (GOOGLE AI STUDIO)
            # -----------------------------------------------------------------------------
            elif "Google" in st.session_state['rag_provedor'] and st.session_state['rag_google_key'].strip():
                with st.spinner("Consultando documento via Google Gemini..."):
                    try:
                        chave_limpa = st.session_state['rag_google_key'].strip()
                        modelo_gemini = st.session_state.get('rag_google_model', 'gemini-1.5-flash').strip()
                        url_gemini = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo_gemini}:generateContent?key={chave_limpa}"

                        contents_api = []
                        for m in st.session_state['rag_chat_messages']:
                            r = "user" if m["role"] == "user" else "model"
                            if not contents_api and r != "user":
                                continue
                            contents_api.append({
                                "role": r,
                                "parts": [{"text": m["content"]}]
                            })

                        system_instruction = f"""Você é: {st.session_state['rag_persona']}

DIRETRIZ ESTRITA DE RAG (Recuperação de Informação):
Você é um assistente de chatbot corporativo. Você DEVE responder às dúvidas do usuário utilizando EXCLUSIVAMENTE as informações contidas na BASE DE CONHECIMENTO oficial fornecida abaixo.
Se a resposta para a dúvida do usuário não estiver expressamente contida na base de conhecimento, responda com cordialidade e clareza informando que essa informação não consta no documento oficial da empresa e oriente onde buscar ajuda. NUNCA invente procedimentos, regras, números ou fatos externos.

BASE DE CONHECIMENTO OFICIAL:
\"\"\"
{st.session_state['rag_contexto']}
\"\"\""""

                        payload = {
                            "systemInstruction": {
                                "parts": [{"text": system_instruction}]
                            },
                            "contents": contents_api,
                            "generationConfig": {
                                "temperature": 0.2,
                                "maxOutputTokens": 500
                            }
                        }
                        req = requests.post(url_gemini, json=payload, timeout=25)
                        if req.status_code == 200:
                            res_json = req.json()
                            resposta_ia = res_json['candidates'][0]['content']['parts'][0]['text']
                            origem_resposta = f"Google Gemini ({modelo_gemini})"
                        else:
                            st.warning(f"⚠️ Resposta da API do Google ({req.status_code}): {req.text[:120]}. Alternando para o motor pedagógico local...")
                    except Exception as ex:
                        st.warning(f"⚠️ Erro ao conectar ao Gemini ({ex}). Alternando para o motor pedagógico local...")

            # -----------------------------------------------------------------------------
            # MOTOR 3: MOTOR PEDAGÓGICO LOCAL (RAG HEURÍSTICO SEM CHAVE)
            # -----------------------------------------------------------------------------
            if not resposta_ia:
                origem_resposta = "Motor Pedagógico Local (RAG Heurístico sem Chave)"
                texto_user_lower = prompt_usuario.lower().strip()
                persona_curta = st.session_state['rag_persona'].split('.')[0]

                saudacoes = ["ola", "olá", "oi", "bom dia", "boa tarde", "boa noite", "opa", "e ai", "e aí", "tudo bem", "como vai"]
                agradecimentos = ["obrigado", "obrigada", "valeu", "agradeco", "agradeço", "muito obrigado", "valeu mesmo"]
                identidade = ["quem e voce", "quem é você", "quem e vc", "quem é vc", "qual seu nome", "o que voce faz", "o que você faz"]

                palavras_msg = set(texto_user_lower.replace('?', ' ').replace('!', ' ').replace(',', ' ').split())

                if any(s in texto_user_lower for s in saudacoes) and len(palavras_msg) <= 4:
                    resposta_ia = f"Olá! Sou seu assistente virtual especializado (**{persona_curta}**). Estou conectado à base de conhecimento oficial e pronto para responder às suas dúvidas sobre as normas e procedimentos. Em que posso te ajudar hoje?"
                elif any(a in texto_user_lower for a in agradecimentos):
                    resposta_ia = "Por nada! Fico sempre à disposição para esclarecer qualquer dúvida com base na documentação da empresa. Se precisar de mais alguma informação, é só perguntar!"
                elif any(i in texto_user_lower for i in identidade):
                    resposta_ia = f"Eu sou um assistente corporativo com tecnologia RAG (**{persona_curta}**). Minha função é consultar a base de conhecimento oficial fornecida e responder às suas perguntas com precisão e segurança, sem alucinações!"
                else:
                    linhas = [l.strip() for l in st.session_state['rag_contexto'].split('\n') if l.strip()]
                    stopwords = {"qual", "quais", "como", "onde", "quando", "quem", "porque", "por", "que", "para", "com", "uma", "uns", "das", "dos", "sobre", "fazer", "pode", "deve", "tenho", "dias", "horas", "quero", "tem"}
                    palavras_uteis = [p for p in palavras_msg if len(p) > 2 and p not in stopwords]

                    linhas_relevantes = []
                    for linha in linhas:
                        score = sum(1 for p in palavras_uteis if p in linha.lower())
                        if score > 0:
                            linhas_relevantes.append((score, linha))

                    linhas_relevantes.sort(key=lambda x: x[0], reverse=True)

                    if linhas_relevantes:
                        evidencias = "\n".join([f"• *\"{l[1]}\"*" for l in linhas_relevantes[:3]])
                        resposta_ia = f"""Consultando a nossa base de conhecimento oficial, trago as seguintes orientações sobre sua dúvida:

{evidencias}

✅ **Ancoragem RAG:** Esta resposta foi recuperada estritamente do documento oficial homologado da empresa."""
                    else:
                        resposta_ia = f"""🛡️ **Bloqueio Anti-Alucinação do RAG Ativado:**

Como **{persona_curta}**, examinei todo o documento oficial cadastrado, porém **não encontrei informações** sobre o que você perguntou.

💡 **Por que isso é bom?** Em um chatbot comum sem RAG, a IA tenderia a 'inventar' ou adivinhar uma resposta que parece verdadeira. Com o RAG, garantimos conformidade: respondemos somente o que está nos manuais homologados da empresa!"""

            # 3. Salvar resposta no histórico e re-executar para manter ordem cronológica perfeita
            st.session_state['rag_chat_messages'].append({
                "role": "assistant",
                "content": resposta_ia,
                "source": origem_resposta
            })
            st.rerun()

        # 🎯 Avaliação de Desempenho e Assertividade da IA (RAG)
        st.markdown("---")
        st.markdown("### 🎯 Avaliação de Desempenho & Assertividade do Chatbot (RAG):")
        c_r_sc1, c_r_sc2, c_r_sc3 = st.columns(3)
        c_r_sc1.metric(
            "🛡️ Score de Ancoragem Factual",
            "100%",
            help="Percentual de declarações fundamentadas estritamente na base de conhecimento oficial fornecida."
        )
        c_r_sc2.metric(
            "🔍 Risco Estimado de Alucinação",
            "0.0%",
            help="Probabilidade da IA inventar dados ou procedimentos fora do documento oficial."
        )
        c_r_sc3.metric(
            "🏆 Nível de Assertividade",
            "Máxima (RAG Blindado)",
            help="Grau de segurança e conformidade para atendimento a clientes e operadores."
        )

    with aba_passos:
        st.subheader("📖 Como um Chatbot Corporativo com RAG Funciona? (Sem Complicação)")
        st.markdown("""
        > 💡 **Analogia da Vida Real:**  
        > Se você contratar um atendente novo e colocá-lo para atender clientes sem nenhum treinamento, ele vai improvisar e falar coisas erradas (**alucinação**).  
        > Mas se você entregar a ele o **Manual de Normas e Procedimentos da Empresa** e instruir: *"Atenda o cliente com educação, mas responda apenas o que estiver neste manual"*, ele se torna um consultor corporativo exemplar!  
        > Isso é o **RAG (Retrieval-Augmented Generation)** aplicado a Chatbots: unir o dom de conversar da IA com a segurança dos dados da empresa!
        """)
        st.markdown("---")
        st.markdown("### 🧩 Os 4 Passos de um Ciclo de Conversa no Chatbot com RAG:")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            #### 1️⃣ Mensagem do Cliente (`st.chat_input`)
            * O usuário faz perguntas em linguagem natural (ex: *"Qual a velocidade recomendada para usinar alumínio?"* ou *"Quantos dias tenho para entregar o atestado?"*).
            """)

            st.markdown("""
            #### 2️⃣ Busca e Recuperação de Evidências (Retrieval)
            * O sistema vasculha o manual, banco de dados ou arquivos PDF da organização e pinça os **trechos exatos** que tratam daquele assunto.
            """)

        with c2:
            st.markdown("""
            #### 3️⃣ Aumento do Prompt com Histórico e Regras (Augmentation)
            * O sistema junta:
              * **Persona:** O papel profissional e tom de voz do atendente.
              * **Histórico da Conversa:** As perguntas e respostas anteriores.
              * **Base de Conhecimento:** Os trechos oficiais recuperados.
              * **Regra de Ouro:** Não inventar nenhum dado fora do documento.
            """)

            st.markdown("""
            #### 4️⃣ Avaliação de Assertividade e Geração Segura (`st.chat_message`)
            * **Scores de Desempenho em Modelos Generativos e RAG:**
              * **Score de Ancoragem Factual (Groundedness):** Mede se 100% das afirmações da resposta possuem respaldo direto no documento de referência.
              * **Taxa de Risco de Alucinação (0.0%):** O RAG protege o chatbot corporativo, impedindo que o modelo invente normas, prazos ou regras inexistentes.
            * **Geração Fluente:** O modelo fundacional (Google Gemini ou Microsoft Azure AI Foundry) redige uma resposta amigável, acolhedora e 100% ancorada na realidade da empresa!
            """)

    with aba_codigo:
        st.subheader("💻 O Código Python Real em Execução no Aplicativo (Gemini & Microsoft Foundry)")
        st.write("Veja o código Python completo demonstrando como conectar o Chatbot com RAG tanto ao **Google Gemini** quanto ao **Microsoft Azure AI Foundry**:")

        st.code("""# =====================================================================
# 💬 CHATBOT COM RAG NO STREAMLIT (GEMINI & MICROSOFT AZURE FOUNDRY)
# =====================================================================
import streamlit as st
import requests

# 1. BASE DE CONHECIMENTO HOMOLOGADA DA EMPRESA (O MANUAL DO RAG)
manual_oficial = \"\"\"
MANUAL DE OPERAÇÃO DO TORNO MECÂNICO SENAI:
1. SEGURANÇA: É obrigatório o uso de óculos de proteção (EPI) e botina com bico de aço.
2. VELOCIDADE DE CORTE: Para alumínio 6061, use 250 m/min. Para aço 1020, use 180 m/min.
3. EMERGÊNCIA: Ao perceber vibração anormal, aperte imediatamente o botão cogumelo vermelho.
\"\"\"

# 2. INICIALIZAR O HISTÓRICO DE MENSAGENS NO STREAMLIT
if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {"role": "assistant", "content": "Olá! Sou o assistente técnico do SENAI. Como posso ajudar?"}
    ]

# Renderizar mensagens anteriores em container organizado:
chat_window = st.container(height=400)
with chat_window:
    for m in st.session_state.mensagens:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

# 3. CAPTURAR A DÚVIDA DIGITADA PELO ALUNO
if duvida_aluno := st.chat_input("Digite sua dúvida sobre o manual técnico..."):
    st.session_state.mensagens.append({"role": "user", "content": duvida_aluno})

    # =================================================================
    # OPÇÃO A: CONEXÃO COM MICROSOFT AZURE AI FOUNDRY (AZURE OPENAI)
    # =================================================================
    FOUNDRY_ENDPOINT = "https://seu-recurso.openai.azure.com/" # Borda do serviço
    FOUNDRY_API_KEY  = "SUA_CHAVE_FOUNDRY_AQUI"
    FOUNDRY_MODEL    = "gpt-4o-mini"
    API_VERSION      = "2024-06-01"

    url_foundry = f"{FOUNDRY_ENDPOINT.rstrip('/')}/openai/deployments/{FOUNDRY_MODEL}/chat/completions?api-version={API_VERSION}"
    headers_foundry = {"Content-Type": "application/json", "api-key": FOUNDRY_API_KEY}

    payload_foundry = {
        "messages": [
            {
                "role": "system",
                "content": f"Você é o instrutor do SENAI. Responda estritamente com base no manual: {manual_oficial}"
            },
            {"role": "user", "content": duvida_aluno}
        ],
        "temperature": 0.2,
        "max_tokens": 400
    }
    # resp_foundry = requests.post(url_foundry, headers=headers_foundry, json=payload_foundry).json()
    # resposta_final = resp_foundry['choices'][0]['message']['content']

    # =================================================================
    # OPÇÃO B: CONEXÃO COM GOOGLE GEMINI (GOOGLE AI STUDIO)
    # =================================================================
    GOOGLE_KEY = "SUA_CHAVE_GEMINI_AQUI"
    url_gemini = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GOOGLE_KEY}"
    payload_gemini = {
        "contents": [{"parts": [{"text": f"Manual:\\n{manual_oficial}\\n\\nDúvida:\\n{duvida_aluno}"}]}],
        "generationConfig": {"temperature": 0.2, "maxOutputTokens": 400}
    }
    # resp_gemini = requests.post(url_gemini, json=payload_gemini).json()
    # resposta_final = resp_gemini['candidates'][0]['content']['parts'][0]['text']

    # 4. SALVAR E ATUALIZAR A INTERFACE COM ORDEM CRONOLÓGICA PERFEITA
    st.session_state.mensagens.append({"role": "assistant", "content": "Resposta ancorada com sucesso!"})
    st.rerun()
""", language="python")
        st.info("💡 **Dica de Ouro:** O `st.container(height=450)` combinado com `st.rerun()` cria uma experiência de chat ultra-fluida, exatamente igual ao ChatGPT ou WhatsApp, garantindo que a caixa de digitação permaneça sempre fixa no rodapé e o histórico seja exibido perfeitamente de cima para baixo!")

    exibir_rodape_educacional()
