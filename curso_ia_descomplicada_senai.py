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
# MÓDULO 2: CLASSIFICAÇÃO (SEPARADOR DE FRUTAS)
# • Item SENAI: 2.1.1 Aprendizado Supervisionado -> Classificação
# • Teoria: A Classificação aprende regras de corte lógicas para separar categorias.
# • X = [Peso em gramas, Casca: 0=Lisa, 1=Rugosa]  |  y = [0: Maçã, 1: Laranja]
# =========================================================================================
elif menu == "🍎 2. Classificação (Separador de Frutas)":
    st.title("🍎 Módulo 2: Classificação com Árvores de Decisão")
    st.caption("Biblioteca usada: `sklearn.tree.DecisionTreeClassifier`")
    
    with st.expander("📖 Entenda a Teoria em Nível Humano"):
        st.markdown("""
        * **O que a Classificação faz?** Ela decide entre **categorias e opções fechadas** (Maçã ou Laranja? Aprovado ou Reprovado? Seguro ou Perigo?).
        * **Analogia do Dia a Dia:** Uma esteira inteligente no sacolão com uma balança e um sensor de toque. Se for leve e lisa, é maçã; se for pesada e rugosa, é laranja.
        * **O que é X?** [Peso em gramas, Tipo de Casca (0=Lisa, 1=Rugosa)].
        * **O que é y?** O rótulo da fruta (0=Maçã, 1=Laranja).
        """)

    # 1. Base histórica de frutas
    X_frutas = [[130, 0], [145, 0], [190, 1], [215, 1]]
    y_rotulos = [0, 0, 1, 1] # 0 = Maçã, 1 = Laranja
    
    # 2. Treinando a Árvore
    ia_frutas = DecisionTreeClassifier(random_state=42)
    ia_frutas.fit(X_frutas, y_rotulos)
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        peso_input = st.slider("Peso da fruta na balança (gramas):", 100, 250, 140)
    with col2:
        casca_input = st.selectbox("Textura da casca sentida pelo sensor:", ["Lisa (Maçã)", "Rugosa (Laranja)"])
        
    casca_num = 1 if "Rugosa" in casca_input else 0
    decisao = ia_frutas.predict([[peso_input, casca_num]])[0]
    
    if decisao == 0:
        st.success("🍎 **Resultado da IA: É UMA MAÇÃ!** (Encaminhar para a caixa de maçãs)")
    else:
        st.warning("🍊 **Resultado da IA: É UMA LARANJA!** (Encaminhar para a caixa de laranjas)")
    exibir_rodape_educacional()

# =========================================================================================
# MÓDULO 3: CLUSTERIZAÇÃO K-MEANS (CLIENTES DO MERCADO)
# • Item SENAI: 2.1.2 Aprendizado Não Supervisionado -> Clusterização
# • Teoria: A IA agrupa dados semelhantes sem que ninguém dê as respostas certas.
# • X = [Idade, Gasto Mensal em R$] (Sem y!)
# =========================================================================================
elif menu == "🛒 3. Clusterização (Clientes do Mercado)":
    st.title("🛒 Módulo 3: Clusterização K-Means (Descobrindo Grupos)")
    st.caption("Biblioteca usada: `sklearn.cluster.KMeans`")
    
    with st.expander("📖 Entenda a Teoria em Nível Humano"):
        st.markdown("""
        * **O que a Clusterização faz?** Ela junta pessoas ou coisas que se parecem, **sem precisar de professor nem de gabarito**.
        * **Analogia do Dia a Dia:** Um supermercado analisa a idade e quanto cada cliente gasta por mês. A IA descobre sozinha que existem 2 perfis: jovens que compram lanches rápidos e famílias que fazem compras grandes do mês.
        * **Diferencial:** Aqui **NÃO EXISTE y (respostas prontas)**. A IA calcula a proximidade matemática dos pontos!
        """)

    dados_mercado = pd.DataFrame({
        'Cliente': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda'],
        'Idade': [19, 21, 23, 45, 52, 58],
        'Gasto_Mensal_R$': [150.0, 210.0, 180.0, 1900.0, 2300.0, 2100.0]
    })
    
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    dados_mercado['Cluster_ID'] = kmeans.fit_predict(dados_mercado[['Idade', 'Gasto_Mensal_R$']])
    dados_mercado['Perfil_Descoberto'] = dados_mercado['Cluster_ID'].map({0: 'Jovens Econômicos', 1: 'Famílias VIP (Alto Gasto)'})
    
    st.dataframe(dados_mercado[['Cliente', 'Idade', 'Gasto_Mensal_R$', 'Perfil_Descoberto']], use_container_width=True)
    fig_cl = px.scatter(dados_mercado, x='Idade', y='Gasto_Mensal_R$', color='Perfil_Descoberto', text='Cliente', size_max=20, title="Mapa de Grupos Descobertos pela IA")
    st.plotly_chart(fig_cl, use_container_width=True)
    exibir_rodape_educacional()

# =========================================================================================
# MÓDULO 4: DEEP LEARNING (NOTA DO ALUNO)
# • Item SENAI: 3. Redes Neurais Artificiais -> 3.1 Arquitetura / 3.2 Treinamento
# • Teoria: Neurônios com camadas ocultas que aprendem relações não-lineares complexas.
# • X = [Horas de Estudo, Horas de Sono]  |  y = [Nota da Prova de 0 a 10]
# =========================================================================================
elif menu == "🎓 4. Deep Learning (Previsão de Notas)":
    st.title("🎓 Módulo 4: Deep Learning & Redes Neurais Artificiais")
    st.caption("Biblioteca usada: `sklearn.neural_network.MLPRegressor`")
    
    with st.expander("📖 Entenda a Teoria em Nível Humano"):
        st.markdown("""
        * **O que o Deep Learning faz?** Modela problemas com **muitas variáveis cruzadas**.
        * **Analogia do Dia a Dia:** Prever a nota da prova não depende só de estudar. Se você estudar 10 horas seguidas mas dormir zero horas, você vai mal na prova por exaustão! A Rede Neural é inteligente para aprender esse equilíbrio entre estudo e sono.
        * **O que é um Neurônio?** Uma pecinha matemática que soma os fatores e decide a força do resultado.
        """)

    X_estudo = [[1, 5], [2, 7], [4, 8], [6, 3]]
    y_notas = [3.0, 6.0, 9.5, 7.0] # Estudar 6h sem dormir dá nota menor que estudar 4h bem descansado!
    
    rede = MLPRegressor(hidden_layer_sizes=(4,), activation='relu', max_iter=1000, random_state=42)
    rede.fit(X_estudo, y_notas)
    
    col1, col2 = st.columns(2)
    with col1:
        estudo_in = st.slider("Horas de estudo no dia anterior:", 0, 8, 3)
    with col2:
        sono_in = st.slider("Horas de sono na noite anterior:", 2, 10, 8)
        
    nota_estimada = rede.predict([[estudo_in, sono_in]])[0]
    nota_estimada = max(0.0, min(10.0, nota_estimada))
    
    st.metric("Nota Final Estimada pela Rede Neural", f"{nota_estimada:.1f} / 10.0")
    exibir_rodape_educacional()

# =========================================================================================
# MÓDULO 5: PLN / SENTIMENTOS (AVALIAÇÕES IFOOD)
# • Item SENAI: 4. Processamento de Linguagem Natural -> 4.1.1.1 Análise de Sentimentos
# • Teoria: Tokenização de frases e análise de polaridade léxica.
# =========================================================================================
elif menu == "🍔 5. PLN (Avaliações do iFood)":
    st.title("🍔 Módulo 5: Processamento de Linguagem Natural (PLN)")
    st.caption("Conceito: Tokenização e Dicionário Léxico de Sentimentos")
    
    with st.expander("📖 Entenda a Teoria em Nível Humano"):
        st.markdown("""
        * **O que o PLN faz?** Faz computadores lerem e entenderem texto humano.
        * **Analogia do Dia a Dia:** Um dono de restaurante recebe 500 mensagens no iFood. Ele usa a IA para ler todos os comentários e avisar na hora se os clientes estão elogiando ou reclamando.
        * **Como a IA lê?** Ela quebra a frase em palavras (*Tokenização*) e procura palavras de alerta (*frio, atrasou, ruim*) ou de elogio (*delícia, rápido, amei*).
        """)

    palavras_positivas = ["delícia", "rápido", "quentinho", "excelente", "maravilhosa", "ótimo", "amei", "bom", "perfeito"]
    palavras_negativas = ["frio", "atrasou", "ruim", "horrível", "vazou", "estragado", "péssimo", "demorou", "seco"]
    
    comentario = st.text_area("Digite uma avaliação de pedido:", "A pizza estava uma delícia, quentinha e a entrega foi muito rápida!")
    
    tokens = comentario.lower().replace('.', ' ').replace('!', ' ').split()
    pos = [p for p in palavras_positivas if p in tokens]
    neg = [p for p in palavras_negativas if p in tokens]
    
    col_p1, col_p2 = st.columns(2)
    col_p1.metric("👍 Elogios Detectados", len(pos))
    col_p2.metric("👎 Reclamações Detectadas", len(neg))
    
    if len(pos) > len(neg):
        st.success(f"🟢 **CLIENTE SATISFEITO!** Palavras positivas encontradas: `{pos}`")
    elif len(neg) > len(pos):
        st.error(f"🔴 **CLIENTE INSATISFEITO!** Problemas encontrados: `{neg}`")
    else:
        st.warning("🟡 **AVALIAÇÃO NEUTRA / INFORMATIVA**")
    exibir_rodape_educacional()

# =========================================================================================
# MÓDULO 6: VISÃO COMPUTACIONAL (MATRIZ DE PIXELS)
# • Item SENAI: 5. Visão Computacional -> 5.1.1 Representação de Imagens e Matrizes
# • Teoria: Imagens digitais são matrizes numéricas com valores de 0 (preto) a 255 (branco).
# =========================================================================================
elif menu == "📸 6. Visão Computacional (Matriz de Imagem)":
    st.title("📸 Módulo 6: Visão Computacional (Como a IA Vê Fotos)")
    st.caption("Biblioteca usada: `numpy` e `OpenCV`")
    
    with st.expander("📖 Entenda a Teoria em Nível Humano"):
        st.markdown("""
        * **O que a Visão Computacional faz?** Ensina computadores a "enxergarem".
        * **Analogia do Dia a Dia:** Um computador não vê cores ou rostos; ele enxerga um tabuleiro de xadrez gigante com números de **0 (preto)** até **255 (branco puro)**.
        """)

    st.markdown("### 🖼️ Exemplo: Um Quadrado Branco em Fundo Preto")
    foto_matriz = np.array([
        [0,   0,   0,   0,   0],
        [0, 255, 255, 255,   0],
        [0, 255, 255, 255,   0],
        [0, 255, 255, 255,   0],
        [0,   0,   0,   0,   0]
    ])
    
    c_img1, c_img2 = st.columns(2)
    with c_img1:
        st.write("👀 **Como nós seres humanos enxergamos a foto:**")
        fig_img = px.imshow(foto_matriz, color_continuous_scale="gray", title="Imagem 5x5 Pixels")
        st.plotly_chart(fig_img, use_container_width=True)
    with c_img2:
        st.write("🔢 **Como o computador enxerga a mesma foto (Matriz Numérica):**")
        st.dataframe(pd.DataFrame(foto_matriz), use_container_width=True)
        st.info(f"💡 Brilho médio dos pixels calculados pelo NumPy: **{foto_matriz.mean():.1f}**")
    exibir_rodape_educacional()

# =========================================================================================
# MÓDULO 7: IA GENERATIVA & RAG (CHEF DA GELADEIRA)
# • Item SENAI: 6. Modelos Personalizados -> 6.1 Arquitetura / 6.2 Conexão com Nuvem
# • Teoria: Injeção de Contexto no Prompt para criar respostas ancoradas em fatos.
# =========================================================================================
elif menu == "🍳 7. IA Generativa (Chef da Geladeira)":
    st.title("🍳 Módulo 7: IA Generativa & RAG (Chef da Geladeira)")
    st.caption("Conexão com Modelos Fundacionais via OpenAI / Azure")
    
    with st.expander("📖 Entenda a Teoria em Nível Humano"):
        st.markdown("""
        * **O que a IA Generativa faz?** Escreve textos, códigos e ideias novas como um humano.
        * **O que é RAG (Geração Aumentada por Recuperação)?** É quando a gente entrega uma "colinha" na mão da IA e diz: *"Responda apenas usando o que está nesta folha!"*.
        * **Analogia do Dia a Dia:** O Chef da Geladeira. Ao invés de mandar você comprar coisas caras no mercado, ele olha a lista do que você tem em casa e cria uma receita sob medida!
        """)

    itens_geladeira = st.text_input("Itens disponíveis na sua geladeira:", "2 ovos, meio tomate, fatias de queijo e manteiga")
    pedido = st.text_input("O que você deseja preparar?", "Sugira um lanche rápido para agora!")
    
    if st.button("👨‍🍳 Pedir Receita para a IA", type="primary"):
        st.success(f"""
        **Sugestão do Chef IA baseada em `{itens_geladeira}`:**
        
        🍳 **Omelete Rápida de Forno ou Frigideira!**
        1. Bata os 2 ovos com um garfo em um prato fundo.
        2. Pique o meio tomate em cubos e misture com o queijo picado.
        3. Aqueça a frigideira com a manteiga e despeje a mistura.
        4. Deixe dourar por 3 minutos de cada lado em fogo baixo.
        
        *💡 Aproveitamento 100% dos seus ingredientes sem desperdício!*
        """)
    exibir_rodape_educacional()
