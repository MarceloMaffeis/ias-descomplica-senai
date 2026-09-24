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
   • O que é em nível humano: São os "olhos e óculos da Inteligência Artificial".
   • Para que serve: Converte fotos e vídeos em matrizes de números e aplica filtros para 
     achar bordas, trincas, rostos e objetos em tempo real.

6. 🧠 OPENAI SDK (`from openai import OpenAI`):
   • O que é em nível humano: É o "telefone que liga para o cérebro gigante do ChatGPT na nuvem".
   • Para que serve: Envia perguntas e manuais para servidores potentes da Microsoft Azure / OpenAI 
     e recebe a resposta em texto inteligente em segundos.

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

# Algoritmos do Scikit-Learn
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.neural_network import MLPRegressor
from openai import OpenAI

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
        "📸 6. Visão Computacional (Matriz de Imagem)",
        "🍳 7. IA Generativa (Chef da Geladeira)"
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
          *O que faz:* Os olhos da Inteligência Artificial. Transforma fotos e vídeos em matrizes numéricas para detectar objetos e rostos.
        
        * 🧠 [**OpenAI API Docs** (platform.openai.com/docs)](https://platform.openai.com/docs/)  
          *O que faz:* O cabo de conexão com grandes modelos generativos na nuvem (como o ChatGPT) para criar assistentes inteligentes.
        
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

    # 3. Informações extraídas do modelo treinado
    inclinacao = modelo_sorvete.coef_[0]
    intercepto = modelo_sorvete.intercept_

    # Navegação por Abas para facilitar a compreensão do aluno
    aba_simulador, aba_passos, aba_codigo = st.tabs([
        "🎮 Simulador Interativo & Gráfico",
        "🧭 Os 4 Passos da IA (Para Leigos)",
        "💻 Código Explicado Linha por Linha"
    ])

    with aba_simulador:
        st.subheader("🧪 Teste o Modelo em Tempo Real")
        st.write("Mova o controle deslizante abaixo para simular a previsão do tempo de amanhã e ver a decisão da IA:")

        temp_escolhida = st.slider("Escolha a temperatura prevista para amanhã (°C):", 15, 42, 32)
        previsao = modelo_sorvete.predict([[temp_escolhida]])[0]

        # Métricas visuais
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
            * No nosso caso, a IA calculou que a cada **+1°C**, vendemos cerca de **8 sorvetes a mais**!
            """)

        with p2:
            st.markdown("""
            #### 3️⃣ Previsão / Inferência (`.predict()`)
            * Uma vez treinada, a IA não precisa mais do histórico antigo. Ela guardou a fórmula na memória!
            * O comando `.predict([[32]])` faz a pergunta: *"Se amanhã fizer 32°C, o que vai acontecer?"*.
            * A IA aplica a fórmula aprendida instantaneamente e devolve a resposta estimada.
            """)

            st.markdown("""
            #### 4️⃣ Análise e Tomada de Decisão
            * **O que fazemos com o número previsto?** O gerente da sorveteria pode planejar as compras de leite, frutas e a escala de funcionários para não faltar produto nem haver desperdício!
            * **Validação:** Olhamos o gráfico para verificar se os pontos reais estão próximos da linha reta calculada.
            """)

    with aba_codigo:
        st.subheader("💻 O Código Python Linha por Linha")
        st.write("Veja como cada etapa explicada acima é escrita de forma simples em Python:")

        st.code("""
# ETAPA 1: SEPARAÇÃO DOS DADOS
# X são as pistas (temperatura) em formato de tabela [[linha1], [linha2]...]
X = [[18], [22], [26], [30], [35]]

# y são os resultados reais que aconteceram (sorvetes vendidos)
y = [40, 65, 90, 130, 180]

# ETAPA 2: ESCOLHA DO MODELO E TREINAMENTO
from sklearn.linear_model import LinearRegression

# Criamos uma folha em branco com o cérebro da Regressão Linear
modelo = LinearRegression()

# O comando .fit() é o TREINAMENTO (a IA analisa X e y e descobre a regra)
modelo.fit(X, y)

# ETAPA 3: PREVISÃO (INFERÊNCIA)
# Perguntamos para a IA o resultado de um dia novo que ela nunca viu:
dia_quente = [[32]]
previsao = modelo.predict(dia_quente)

# ETAPA 4: ANÁLISE DO RESULTADO
print(f"Com 32°C, a previsão é vender {previsao[0]:.0f} sorvetes!")
        """, language="python")

        st.info("💡 **Dica de Ouro:** O segredo do Scikit-Learn é que quase todos os modelos funcionam sempre no mesmo trio: **Criar o modelo** ➡️ **`.fit()` para treinar** ➡️ **`.predict()` para prever**!")

    exibir_rodape_educacional()

# =========================================================================================
# MÓDULO 2: CLASSIFICAÇÃO (SEPARADOR DE FRUTAS) - DIDÁTICO E PASSO A PASSO
# • Item SENAI: 2.1.1 Aprendizado Supervisionado -> Classificação
# • Teoria: A Classificação aprende regras de corte lógicas para separar categorias.
# =========================================================================================
elif menu == "🍎 2. Classificação (Separador de Frutas)":
    st.title("🍎 Módulo 2: Classificação com Árvores de Decisão")
    st.caption("Biblioteca usada: [`sklearn.tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)")

    # 1. Base histórica de frutas (X = [Peso em gramas, Textura da Casca: 0=Lisa, 1=Rugosa])
    X_frutas = [
        [130, 0], [140, 0], [145, 0], [150, 0],  # Maçãs (leves e lisas)
        [185, 1], [195, 1], [210, 1], [225, 1]   # Laranjas (mais pesadas e rugosas)
    ]
    y_rotulos = [0, 0, 0, 0, 1, 1, 1, 1] # 0 = Maçã, 1 = Laranja

    # 2. Treinando o Modelo
    ia_frutas = DecisionTreeClassifier(random_state=42)
    ia_frutas.fit(X_frutas, y_rotulos)

    aba_simulador, aba_passos, aba_codigo = st.tabs([
        "🎮 Simulador Interativo & Esteira",
        "🧭 Os 4 Passos da IA (Para Leigos)",
        "💻 Código Explicado Linha por Linha"
    ])

    with aba_simulador:
        st.subheader("🧪 Teste da Esteira Seletora Industrial")
        st.write("Coloque uma fruta na esteira ajustando os sensores de peso e textura:")

        col1, col2 = st.columns(2)
        with col1:
            peso_input = st.slider("⚖️ Peso na Balança Digital (gramas):", 110, 240, 140)
        with col2:
            casca_input = st.selectbox("🖐️ Textura sentida pelo Sensor de Toque:", ["Lisa (Casca de Maçã)", "Rugosa (Casca de Laranja)"])

        casca_num = 1 if "Rugosa" in casca_input else 0
        previsao_fruta = ia_frutas.predict([[peso_input, casca_num]])[0]
        probabilidades = ia_frutas.predict_proba([[peso_input, casca_num]])[0]

        st.markdown("---")
        c_res1, c_res2, c_res3 = st.columns(3)
        c_res1.metric("⚖️ Peso Informado", f"{peso_input} g")
        c_res2.metric("🔍 Casca Detectada", "Rugosa" if casca_num == 1 else "Lisa")
        confianca = max(probabilidades) * 100
        c_res3.metric("🎯 Confiança da IA", f"{confianca:.0f}%")

        if previsao_fruta == 0:
            st.success("🍎 **DECISÃO DA IA: É UMA MAÇÃ!** ➡️ *Comando enviado para a esteira: Empurrar para a Caixa A (Maçãs)*")
        else:
            st.warning("🍊 **DECISÃO DA IA: É UMA LARANJA!** ➡️ *Comando enviado para a esteira: Empurrar para a Caixa B (Laranjas)*")

        # Gráfico visual das frutas e a nova fruta
        df_historico_frutas = pd.DataFrame({
            'Peso (g)': [130, 140, 145, 150, 185, 195, 210, 225],
            'Casca': ['Lisa', 'Lisa', 'Lisa', 'Lisa', 'Rugosa', 'Rugosa', 'Rugosa', 'Rugosa'],
            'Fruta': ['Maçã', 'Maçã', 'Maçã', 'Maçã', 'Laranja', 'Laranja', 'Laranja', 'Laranja']
        })
        fig_frutas = px.scatter(
            df_historico_frutas,
            x='Peso (g)',
            y='Casca',
            color='Fruta',
            title="Distribuição das Frutas no Espaço de Decisão",
            color_discrete_map={'Maçã': '#EF4444', 'Laranja': '#F97316'}
        )
        fig_frutas.add_scatter(
            x=[peso_input],
            y=['Rugosa' if casca_num == 1 else 'Lisa'],
            mode='markers',
            marker=dict(size=16, color='blue', symbol='star'),
            name=f'Fruta Atual ({peso_input}g)'
        )
        st.plotly_chart(fig_frutas, use_container_width=True)

    with aba_passos:
        st.subheader("📖 Como a Classificação Funciona? (Sem Complicação)")
        st.markdown("""
        > 💡 **Analogia da Vida Real:**  
        > Imagine um funcionário novo no sacolão ou na linha de fábrica do SENAI. No primeiro dia, ele aprende:  
        > *"Se a fruta for levinha e a casca for lisa como cera, é maçã. Se for pesada e cheia de furinhos/rugosa, é laranja"*.  
        > A **Classificação** é quando o computador aprende a fazer **perguntas de 'SE... ENTÃO'** para separar coisas em gavetas fechadas!
        """)
        st.markdown("---")
        st.markdown("### 🧩 Os 4 Passos Fundamentais da Classificação:")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            #### 1️⃣ Separação dos Dados (X e y)
            * **$X$ (Características / Features):** Informações medidas pelos sensores (Peso em gramas e Tipo de casca 0 ou 1).
            * **$y$ (Classes / Rótulos):** O nome da gaveta onde o item deve cair (0 para Maçã ou 1 para Laranja).
            * *Diferença para a Regressão:* Na Regressão prevemos um **número contínuo** (ex: 148 sorvetes). Na Classificação, escolhemos uma **categoria** (Maçã ou Laranja).
            """)

            st.markdown("""
            #### 2️⃣ Treinamento da Árvore (`.fit()`)
            * A Árvore de Decisão analisa todos os exemplos e descobre o melhor ponto de corte:
              * *Exemplo de regra aprendida:* **"O peso é maior que 165g?"**
                * Se SIM ➡️ Provavelmente Laranja.
                * Se NÃO ➡️ Provavelmente Maçã.
            """)

        with c2:
            st.markdown("""
            #### 3️⃣ Previsão / Teste em Tempo Real (`.predict()`)
            * Quando uma fruta inédita passa pela esteira, o sensor mede seus atributos.
            * A IA percorre os galhos da árvore de decisão e devolve a resposta instantânea.
            """)

            st.markdown("""
            #### 4️⃣ Análise e Aplicação na Automação
            * **Na Indústria 4.0:** Este algoritmo aciona braços robóticos ou pistões pneumáticos para separar peças com defeito de peças aprovadas sem intervenção humana!
            * **Métrica:** Avaliamos a *Acurácia* (quantas frutas a máquina acertou em 100 tentativas).
            """)

    with aba_codigo:
        st.subheader("💻 O Código Python Linha por Linha")
        st.code("""
# ETAPA 1: SEPARAÇÃO DOS DADOS DE TREINO
# X: [Peso em gramas, Textura: 0=Lisa, 1=Rugosa]
X = [[130, 0], [145, 0], [190, 1], [215, 1]]

# y: Categorias (0 = Maçã, 1 = Laranja)
y = [0, 0, 1, 1]

# ETAPA 2: CRIAÇÃO E TREINAMENTO DA ÁRVORE DE DECISÃO
from sklearn.tree import DecisionTreeClassifier

# Criamos o modelo
classificador = DecisionTreeClassifier()

# Mandamos o modelo aprender as regras com os dados (.fit)
classificador.fit(X, y)

# ETAPA 3: PREVENDO UMA NOVA FRUTA NA ESTEIRA
# Chegou uma fruta de 142 gramas com casca lisa (0)
nova_fruta = [[142, 0]]
resultado = classificador.predict(nova_fruta)

# ETAPA 4: ANÁLISE E DECISÃO
if resultado[0] == 0:
    print("Resultado: Maçã (Encaminhar para a Caixa A)")
else:
    print("Resultado: Laranja (Encaminhar para a Caixa B)")
        """, language="python")
        st.info("💡 **Dica de Ouro:** A Árvore de Decisão é um dos modelos mais fáceis de explicar para leigos porque ela funciona exatamente como um fluxograma humano de perguntas!")

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

    # 2. Treinando o K-Means para encontrar 2 perfis
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    dados_mercado['Cluster_ID'] = kmeans.fit_predict(dados_mercado[['Idade', 'Gasto_Mensal_R$']])
    
    # Identificar qual cluster tem maior gasto
    cluster_vip = dados_mercado.groupby('Cluster_ID')['Gasto_Mensal_R$'].mean().idxmax()
    dados_mercado['Perfil'] = dados_mercado['Cluster_ID'].apply(
        lambda c: 'Famílias VIP (Alto Gasto)' if c == cluster_vip else 'Jovens Econômicos'
    )

    aba_simulador, aba_passos, aba_codigo = st.tabs([
        "🎮 Simulador Interativo & Grupos",
        "🧭 Os 4 Passos da IA (Para Leigos)",
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
            #### 4️⃣ Ação e Tomada de Decisão de Negócio
            * **Segmentação de Marketing:** Em vez de mandar a mesma propaganda para todo mundo, o supermercado cria campanhas personalizadas que aumentam as vendas e evitam desperdício de anúncios.
            """)

    with aba_codigo:
        st.subheader("💻 O Código Python Linha por Linha")
        st.code("""
# ETAPA 1: PREPARAÇÃO DOS DADOS (APENAS X, SEM y!)
import pandas as pd
dados = pd.DataFrame({
    'Idade': [19, 21, 23, 45, 52, 58],
    'Gasto_Mensal': [150, 210, 180, 1900, 2300, 2100]
})

# ETAPA 2: CRIAÇÃO DO K-MEANS E TREINAMENTO
from sklearn.cluster import KMeans

# Queremos que a IA descubra 2 grupos (n_clusters=2)
kmeans = KMeans(n_clusters=2, random_state=42)

# O fit_predict() descobre os grupos e já rotula cada cliente (0 ou 1)
dados['Grupo'] = kmeans.fit_predict(dados[['Idade', 'Gasto_Mensal']])

# ETAPA 3: ATRIBUINDO UM CLIENTE INÉDITO
novo_cliente = [[22, 200]] # 22 anos, gasto de R$ 200
grupo_novo = kmeans.predict(novo_cliente)

# ETAPA 4: ANÁLISE DO RESULTADO
print(f"O novo cliente foi associado ao Grupo {grupo_novo[0]}")
        """, language="python")
        st.info("💡 **Dica de Ouro:** O K-Means é chamado de 'Não Supervisionado' porque você não precisa gastar milhares de horas rotulando os dados manualmente; o robô descobre os grupos sozinho!")

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

    # 2. Treinando a Rede Neural Artificial
    rede = MLPRegressor(hidden_layer_sizes=(6, 4), activation='relu', max_iter=2000, random_state=42)
    rede.fit(X_estudo, y_notas)

    aba_simulador, aba_passos, aba_codigo = st.tabs([
        "🎮 Simulador Interativo & Neurônios",
        "🧭 Os 4 Passos da IA (Para Leigos)",
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
            #### 4️⃣ Aplicação Prática
            * **Onde o Deep Learning brilha:** Reconhecimento facial, carros autônomos, diagnósticos médicos e tradução simultânea — problemas em que existem centenas ou milhares de fatores cruzados ao mesmo tempo!
            """)

    with aba_codigo:
        st.subheader("💻 O Código Python Linha por Linha")
        st.code("""
# ETAPA 1: DADOS COM DUAS VARIÁVEIS DE ENTRADA
# X = [Horas de Estudo, Horas de Sono]
X = [[1, 5], [2, 7], [4, 8], [6, 3]]
# y = Nota obtida na prova
y = [3.0, 6.0, 9.5, 6.5]

# ETAPA 2: CRIAÇÃO DA REDE NEURAL (MLP = Multi-Layer Perceptron)
from sklearn.neural_network import MLPRegressor

# Criamos uma rede com camadas ocultas de neurônios
rede = MLPRegressor(
    hidden_layer_sizes=(6, 4), # 2 camadas: uma com 6 e outra com 4 neurônios
    activation='relu',         # Função que decide o disparo do neurônio
    max_iter=2000,             # Quantas vezes a rede repassa os dados para aprender
    random_state=42
)

# Treinamos a rede para calibrar os pesos das sinapses
rede.fit(X, y)

# ETAPA 3: TESTANDO UM ALUNO NOVO
novo_aluno = [[5, 8]] # 5 horas de estudo, 8 horas de sono
nota_prevista = rede.predict(novo_aluno)

# ETAPA 4: ANÁLISE DO RESULTADO
print(f"Nota estimada pela Rede Neural: {nota_prevista[0]:.1f}")
        """, language="python")
        st.info("💡 **Dica de Ouro:** Chamamos de 'Deep Learning' (Aprendizado Profundo) porque a rede empilha várias camadas ocultas de neurônios, permitindo aprender padrões abstratos que nenhum humano conseguiria programar na mão!")

    exibir_rodape_educacional()

# =========================================================================================
# MÓDULO 5: PLN / SENTIMENTOS (AVALIAÇÕES IFOOD) - DIDÁTICO E PASSO A PASSO
# • Item SENAI: 4. Processamento de Linguagem Natural -> 4.1.1.1 Análise de Sentimentos
# • Teoria: Tokenização de frases e análise de polaridade léxica.
# =========================================================================================
elif menu == "🍔 5. PLN (Avaliações do iFood)":
    st.title("🍔 Módulo 5: Processamento de Linguagem Natural (PLN)")
    st.caption("Conceito Central: Tokenização, Stopwords e Análise Léxica de Sentimentos")

    aba_simulador, aba_passos, aba_codigo = st.tabs([
        "🎮 Simulador de Avaliações em Tempo Real",
        "🧭 Os 4 Passos do PLN (Para Leigos)",
        "💻 Código Explicado Linha por Linha"
    ])

    palavras_positivas = ["delícia", "rápido", "quentinho", "excelente", "maravilhosa", "ótimo", "amei", "bom", "perfeito", "saboroso"]
    palavras_negativas = ["frio", "atrasou", "ruim", "horrível", "vazou", "estragado", "péssimo", "demorou", "seco", "cru", "errado"]

    with aba_simulador:
        st.subheader("🧪 Simulador de Atendimento ao Cliente do Restaurante")
        st.write("Digite uma mensagem real ou use os botões rápidos para testar a interpretação da IA:")

        # Botões rápidos para testes
        b1, b2, b3 = st.columns(3)
        msg_exemplo = "A pizza estava uma delícia, quentinha e a entrega foi muito rápida!"
        if b1.button("🟢 Testar Elogio Apaixonado"):
            st.session_state['texto_pln'] = "A pizza estava uma delícia, muito saborosa e o motoboy foi rápido!"
        if b2.button("🔴 Testar Reclamação Severa"):
            st.session_state['texto_pln'] = "A comida atrasou mais de uma hora, o refrigerante veio quente e o lanche estava frio e horrível!"
        if b3.button("🟡 Testar Avaliação Mista"):
            st.session_state['texto_pln'] = "O sabor da pizza é excelente, mas infelizmente demorou muito para chegar."

        texto_atual = st.session_state.get('texto_pln', msg_exemplo)
        comentario = st.text_area("Mensagem enviada pelo cliente no app:", texto_atual, height=100)

        # Processamento simples em linguagem natural
        tokens = comentario.lower().replace('.', ' ').replace('!', ' ').replace(',', ' ').replace('?', ' ').split()
        pos = [p for p in tokens if p in palavras_positivas]
        neg = [p for p in tokens if p in palavras_negativas]
        saldo_emocional = len(pos) - len(neg)

        st.markdown("---")
        c_pln1, c_pln2, c_pln3 = st.columns(3)
        c_pln1.metric("👍 Palavras Felizes", len(pos), help=f"Encontradas: {pos}")
        c_pln2.metric("👎 Palavras Críticas", len(neg), help=f"Encontradas: {neg}")
        c_pln3.metric("⚖️ Saldo Emocional", f"{saldo_emocional:+d}")

        if saldo_emocional > 0:
            st.success(f"🟢 **CLIENTE SATISFEITO!** A IA detectou termos elogiosos: `{pos}`. Nenhuma ação corretiva urgente necessária.")
        elif saldo_emocional < 0:
            st.error(f"🔴 **ALERTA DE CLIENTE INSATISFEITO!** A IA detectou reclamações críticas: `{neg}`. Acionar gerente e enviar cupom de desculpas imediatamente!")
        else:
            st.warning("🟡 **AVALIAÇÃO NEUTRA OU EQUILIBRADA:** O cliente pontuou aspectos positivos e negativos em proporções parecidas.")

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
            #### 2️⃣ Remoção de Ruído (Stopwords)
            * Palavras como *de, para, com, o, a* não têm sentimento próprio. A IA aprende a ignorar essas palavras neutras e focar no que importa.
            """)

        with c2:
            st.markdown("""
            #### 3️⃣ Análise de Sentimento (Léxico)
            * O algoritmo compara cada palavra com dicionários de sentimentos (pesos positivos e negativos) para calcular o placar emocional da frase.
            """)

            st.markdown("""
            #### 4️⃣ Ação Automatizada
            * **No Atendimento ao Cliente:** Se o saldo for muito negativo, o chamado é encaminhado para a fila de prioridade máxima de um atendente humano em menos de 1 segundo!
            """)

    with aba_codigo:
        st.subheader("💻 O Código Python Linha por Linha")
        st.code("""
# ETAPA 1: O TEXTO BRUTO DO CLIENTE
mensagem = "A entrega atrasou e a pizza chegou fria, péssimo atendimento!"

# ETAPA 2: LIMPEZA E TOKENIZAÇÃO (Quebrar em palavras)
palavras = mensagem.lower().replace(',', ' ').replace('!', ' ').split()

# ETAPA 3: DICIONÁRIO DE SENTIMENTOS
termos_positivos = ["delícia", "quentinho", "rápido", "excelente"]
termos_negativos = ["frio", "atrasou", "péssimo", "horrível"]

# Identificamos as palavras-chave encontradas
elogios = [p for p in palavras if p in termos_positivos]
criticas = [p for p in palavras if p in termos_negativos]

# ETAPA 4: DECISÃO BASEADA NO SALDO
saldo = len(elogios) - len(criticas)

if saldo < 0:
    print(f"Alerta: Cliente insatisfeito! Palavras de alerta: {criticas}")
else:
    print("Cliente satisfeito ou neutro.")
        """, language="python")
        st.info("💡 **Dica de Ouro:** O PLN moderno evoluiu dessa análise por palavras para modelos de Linguagem Gigantes (LLMs como o GPT e Gemini), que entendem até ironia e sarcasmo contextual!")

    exibir_rodape_educacional()

# =========================================================================================
# MÓDULO 6: VISÃO COMPUTACIONAL (MATRIZ DE PIXELS) - DIDÁTICO E PASSO A PASSO
# • Item SENAI: 5. Visão Computacional -> 5.1.1 Representação de Imagens e Matrizes
# • Teoria: Imagens digitais são matrizes numéricas com valores de 0 (preto) a 255 (branco).
# =========================================================================================
elif menu == "📸 6. Visão Computacional (Matriz de Imagem)":
    st.title("📸 Módulo 6: Visão Computacional (Como a IA Vê Imagens)")
    st.caption("Bibliotecas fundamentais: [`NumPy`](https://numpy.org/) e [`OpenCV`](https://opencv.org/)")

    aba_simulador, aba_passos, aba_codigo = st.tabs([
        "🎮 Simulador de Pixels e Filtros",
        "🧭 Os 4 Passos da Visão (Para Leigos)",
        "💻 Código Explicado Linha por Linha"
    ])

    with aba_simulador:
        st.subheader("🧪 Como a Câmera Transforma o Mundo em Números")
        st.write("Escolha um desenho geométrico simples de 5x5 pixels e aplique filtros para ver a matemática acontecendo:")

        padrao = st.radio(
            "Selecione um Padrão Visual:",
            ["Quadrado no Centro", "Cruz / Letra X", "Degradê de Iluminação"],
            horizontal=True
        )

        if padrao == "Quadrado no Centro":
            matriz_original = np.array([
                [0,   0,   0,   0,   0],
                [0, 255, 255, 255,   0],
                [0, 255, 255, 255,   0],
                [0, 255, 255, 255,   0],
                [0,   0,   0,   0,   0]
            ])
        elif padrao == "Cruz / Letra X":
            matriz_original = np.array([
                [255,   0,   0,   0, 255],
                [  0, 255,   0, 255,   0],
                [  0,   0, 255,   0,   0],
                [  0, 255,   0, 255,   0],
                [255,   0,   0,   0, 255]
            ])
        else: # Degradê
            matriz_original = np.array([
                [ 20,  40,  60,  80, 100],
                [ 50,  70,  90, 110, 130],
                [ 80, 100, 120, 140, 160],
                [110, 130, 150, 170, 200],
                [140, 170, 200, 230, 255]
            ])

        # Controle interativo de brilho
        ajuste_brilho = st.slider("💡 Ajuste de Brilho dos Pixels (+/- valores):", -100, 100, 0)
        matriz_processada = np.clip(matriz_original.astype(int) + ajuste_brilho, 0, 255)

        c_v1, c_v2 = st.columns(2)
        with c_v1:
            st.write("👀 **Como o SER HUMANO enxerga a imagem:**")
            fig_vc = px.imshow(
                matriz_processada,
                color_continuous_scale="gray",
                title="Visualização Gráfica (Preto = 0 | Branco = 255)",
                range_color=[0, 255]
            )
            st.plotly_chart(fig_vc, use_container_width=True)

        with c_v2:
            st.write("🔢 **Como a INTELIGÊNCIA ARTIFICIAL enxerga a mesma foto:**")
            df_pixels = pd.DataFrame(matriz_processada, columns=[f"P{i}" for i in range(5)])
            st.dataframe(df_pixels, use_container_width=True)
            st.info(f"📊 Brilho médio dos 25 pixels: **{matriz_processada.mean():.1f} / 255.0**")

    with aba_passos:
        st.subheader("📖 Como a Visão Computacional Funciona? (Sem Complicação)")
        st.markdown("""
        > 💡 **Analogia da Vida Real:**  
        > Um computador não tem olhos biológicos nem retina. Para ele, uma foto não é uma pessoa ou um carro;  
        > Uma foto é uma **tabela de números**, exatamente como uma planilha do Excel, onde cada quadradinho (pixel) tem um valor de **0 (escuridão total)** até **255 (luz branca pura)**!
        """)
        st.markdown("---")
        st.markdown("### 🧩 Os 4 Passos Fundamentais da Visão Computacional:")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            #### 1️⃣ Captura e Digitalização
            * A lente da câmera capta a luz e converte fótons em eletricidade em cada sensor minúsculo, gerando números inteiros entre 0 e 255.
            """)

            st.markdown("""
            #### 2️⃣ Armazenamento em Matrizes (`NumPy`)
            * Uma imagem preta e branca de 1920x1080 é uma matriz com mais de **2 milhões de números**.
            * Se a imagem for colorida, ela tem 3 matrizes sobrepostas: **R** (Vermelho), **G** (Verde) e **B** (Azul).
            """)

        with c2:
            st.markdown("""
            #### 3️⃣ Filtros e Detecção de Bordas
            * O computador calcula a diferença brusca de números vizinhos.
            * Se um pixel vale **0** e o do lado vale **255**, ali existe uma **borda nítida** (o contorno de uma peça, um rosto ou uma placa de trânsito).
            """)

            st.markdown("""
            #### 4️⃣ Aplicação na Indústria SENAI
            * **Controle de Qualidade em Linhas de Montagem:** Câmeras inteligentes inspecionam garrafas, tampas e circuitos eletrônicos a 60 fotos por segundo, descartando peças trincadas sem cansar a vista humana!
            """)

    with aba_codigo:
        st.subheader("💻 O Código Python Linha por Linha")
        st.code("""
# ETAPA 1: UMA FOTO É UMA MATRIZ NUMÉRICA (0 a 255)
import numpy as np

foto_matriz = np.array([
    [0,   0,   0,   0,   0],
    [0, 255, 255, 255,   0], # Pixels 255 são brancos
    [0, 255, 255, 255,   0],
    [0, 255, 255, 255,   0],
    [0,   0,   0,   0,   0]
])

# ETAPA 2: APLICAR UM FILTRO DE BRILHO (Adição simples de matriz)
foto_mais_clara = np.clip(foto_matriz + 50, 0, 255)

# ETAPA 3: CALCULAR MÉTRICAS DA IMAGEM
brilho_medio = foto_matriz.mean()
print(f"Brilho médio: {brilho_medio}")

# ETAPA 4: DETECÇÃO DE PEÇA DEFEITUOSA NA INDÚSTRIA
# Se tiver mais de 5 pixels brancos no centro, a peça foi aprovada
pixels_acesos = (foto_matriz == 255).sum()
if pixels_acesos >= 5:
    print("Peça aprovada pelo controle de qualidade!")
else:
    print("Defeito detectado: peça incompleta.")
        """, language="python")
        st.info("💡 **Dica de Ouro:** Todas as Redes Neurais Convolucionais (CNNs) e IAs de visão que reconhecem rostos ou placas de trânsito nada mais fazem do que continhas de multiplicação e soma com essas matrizes de pixels!")

    exibir_rodape_educacional()

# =========================================================================================
# MÓDULO 7: IA GENERATIVA & RAG (CHEF DA GELADEIRA) - DIDÁTICO E PASSO A PASSO
# • Item SENAI: 6. Modelos Personalizados -> 6.1 Arquitetura / 6.2 Conexão com Nuvem
# • Teoria: Injeção de Contexto no Prompt (RAG) para criar respostas ancoradas em fatos.
# =========================================================================================
elif menu == "🍳 7. IA Generativa (Chef da Geladeira)":
    st.title("🍳 Módulo 7: IA Generativa & RAG (Chef da Geladeira)")
    st.caption("Conceito Central: Modelos de Linguagem (LLMs), Engenharia de Prompt e RAG (Geração Aumentada por Recuperação)")

    aba_simulador, aba_passos, aba_codigo = st.tabs([
        "🎮 Simulador do Chef IA & RAG",
        "🧭 Os 4 Passos do RAG (Para Leigos)",
        "💻 Código Explicado Linha por Linha"
    ])

    with aba_simulador:
        st.subheader("🧪 Simulador: Geração Ancorada em Dados Reais")
        st.write("Veja como a IA Generativa responde sem 'alucinar' quando você entrega os dados corretos no contexto:")

        c_g1, c_g2 = st.columns(2)
        with c_g1:
            itens_geladeira = st.text_input(
                "🧊 Itens disponíveis na sua geladeira (Base de Conhecimento / RAG):",
                "2 ovos, meio tomate, fatias de queijo e manteiga"
            )
        with c_g2:
            estilo = st.selectbox(
                "⏱️ Tipo de refeição desejada:",
                ["Lanche Rápido de 5 minutos", "Refeição Fitness de Forno", "Prato Econômico de Frigideira"]
            )

        pedido = st.text_input("💬 Pedido do Usuário:", f"Sugira um {estilo} aproveitando tudo o que tenho!")

        # Exibir o prompt que é montado por trás dos panos
        with st.expander("🔍 Espiar o Prompt Interno montado pelo RAG (Clique para ver a engenharia)"):
            st.code(f"""
[SISTEMA]: Você é um Chef especialista em culinária sustentável e economia doméstica.
[CONTEXTO CONFIÁVEL / GELADEIRA]: {itens_geladeira}
[REGRA DE OURO]: Não invente ingredientes que não constam na lista acima.
[PERGUNTA DO USUÁRIO]: {pedido}
            """, language="markdown")

        if st.button("👨‍🍳 Gerar Receita com IA Generativa", type="primary"):
            st.success(f"""
            ### 🍽️ Sugestão Personalizada do Chef IA:
            
            🍳 **Omelete Cremosa de Frigideira com Queijo e Tomate Fresco**
            
            * **Tempo de Preparo:** 5 a 7 minutos
            * **Ingredientes Utilizados:** Exatamente os informados (`{itens_geladeira}`).
            
            **Passo a Passo:**
            1. Em um prato, quebre os **2 ovos** e bata ligeiramente com um garfo até formar uma mistura homogênea.
            2. Pique o **meio tomate** em cubinhos pequenos e corte as **fatias de queijo** em tiras.
            3. Derreta uma colher de **manteiga** na frigideira antiaderente em fogo médio.
            4. Despeje os ovos batidos, distribua os cubos de tomate e cubra com o queijo.
            5. Dobre a omelete ao meio quando a base estiver firme e deixe o queijo derreter por 1 minuto.
            
            *✅ Desperdício Zero: 100% dos seus ingredientes foram aproveitados sem precisar ir ao mercado!*
            """)

    with aba_passos:
        st.subheader("📖 Como a IA Generativa e o RAG Funcionam? (Sem Complicação)")
        st.markdown("""
        > 💡 **Analogia da Vida Real:**  
        > Se você perguntar para o ChatGPT: *"Como montar a peça X da minha fábrica?"*, ele pode inventar peças que não existem na sua empresa (isso é a famosa **alucinação**).  
        > Mas se você entregar o manual oficial da sua empresa junto com a pergunta e disser: *"Responda APENAS usando este manual"*, ele vira um assistente infalível!  
        > Isso é o **RAG (Geração Aumentada por Recuperação)**: entregar a folha de respostas na mão da IA antes de ela começar a falar!
        """)
        st.markdown("---")
        st.markdown("### 🧩 Os 4 Passos Fundamentais do RAG:")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            #### 1️⃣ A Pergunta do Usuário (Query)
            * O usuário faz uma pergunta em português comum (ex: *"O que posso cozinhar agora?"*).
            """)

            st.markdown("""
            #### 2️⃣ Recuperação do Contexto (Retrieval)
            * O sistema busca no banco de dados, arquivos PDF da empresa ou na lista da geladeira as informações exatas relacionadas àquela pergunta.
            """)

        with c2:
            st.markdown("""
            #### 3️⃣ Engenharia de Prompt (Augmentation)
            * Juntamos tudo em uma instrução blindada:
              * *Papel do robô:* Especialista.
              * *Colinha:* Os dados recuperados.
              * *Regra:* Não invente nada fora desse contexto.
            """)

            st.markdown("""
            #### 4️⃣ Geração da Resposta (Generation)
            * O modelo generativo (como GPT ou Gemini) escreve um texto fluente, útil e 100% ancorado na realidade da sua empresa!
            """)

    with aba_codigo:
        st.subheader("💻 O Código Python Linha por Linha")
        st.code("""
# ETAPA 1: O CONTEXTO RECUPERADO (A COLINHA DO RAG)
ingredientes_geladeira = "2 ovos, meio tomate, fatias de queijo e manteiga"
pergunta_usuario = "Sugira um lanche rápido para agora!"

# ETAPA 2: MONTAGEM DO PROMPT ENRIQUECIDO COM RAG
prompt_final = f'''
Você é um assistente de cozinha sustentável.
Contexto de ingredientes disponíveis: {ingredientes_geladeira}
Regra estrita: Crie uma receita usando APENAS o que está disponível.

Pergunta: {pergunta_usuario}
'''

# ETAPA 3: CHAMADA À API DO MODELO GENERATIVO (Exemplo OpenAI / Azure)
from openai import OpenAI

# cliente = OpenAI(api_key="SUA_CHAVE_AQUI")
# resposta = cliente.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "Você é um chef sustentável."},
#         {"role": "user", "content": prompt_final}
#     ]
# )

# ETAPA 4: EXIBIÇÃO DA RESPOSTA SEGURA E ANCORADA
print("Receita gerada com sucesso sem inventar ingredientes externos!")
        """, language="python")
        st.info("💡 **Dica de Ouro:** O RAG é a tecnologia mais valorizada do mercado hoje porque permite que empresas usem o poder dos grandes modelos de IA dentro de seus próprios manuais, normas e bancos de dados privados sem risco de vazamento ou invenções!")

    exibir_rodape_educacional()
