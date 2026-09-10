# =========================================================================================
# 🎓 SENAI-SP — APERFEIÇOAMENTO PROFISSIONAL: PROGRAMAÇÃO EM IA GENERATIVA (40H)
# 📖 GUIA PRÁTICO & APLICATIVO DIDÁTICO UNIFICADO: DA TEORIA AO STREAMLIT
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
# MENU LATERAL COM TODOS OS MÓDULOS DA EMENTA SENAI
# =========================================================================================
st.sidebar.title("💡 IA Descomplicada")
st.sidebar.caption("SENAI-SP • Exemplos Práticos do Cotidiano")

menu = st.sidebar.radio(
    "Selecione a Tecnologia de IA:",
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
st.sidebar.caption("📜 Material Didático Aberto — Licença MIT")

# =========================================================================================
# MÓDULO 0: APRESENTAÇÃO DAS BIBLIOTECAS
# =========================================================================================
if menu == "🏠 Início: O Kit de Bibliotecas":
    st.title("Bem-vindo ao Laboratório de IA Descomplicada! 🚀")
    st.subheader("Como a Inteligência Artificial funciona na vida real?")
    st.info("Neste ambiente, você aprenderá os 7 pilares da Inteligência Artificial usando exemplos simples do dia a dia.")
    
    st.markdown("""
    ### 🧰 As 7 Ferramentas que Usamos em Python:
    * **NumPy:** A calculadora super rápida que faz contas com matrizes.
    * **Pandas:** O organizador de tabelas (o Excel do programador).
    * **Scikit-Learn:** Onde moram os robôs inteligentes de Machine Learning.
    * **NLTK:** A ferramenta que ensina o computador a ler textos e sentimentos.
    * **OpenCV:** A ferramenta que faz o computador enxergar imagens.
    * **OpenAI API:** O cabo de conexão com grandes modelos generativos na nuvem.
    * **Streamlit:** A mágica que transforma nosso código neste painel interativo!
    """)
    st.success("👈 Escolha qualquer exemplo no menu lateral para ver o código e testar a IA ao vivo!")

# =========================================================================================
# MÓDULO 1: REGRESSÃO LINEAR (SORVETERIA)
# • Item SENAI: 2.1.1 Aprendizado Supervisionado -> Regressão
# • Teoria: A Regressão descobre uma reta matemática para prever um número contínuo.
# • X = [Temperatura do dia em °C]  |  y = [Quantidade de Sorvetes Vendidos]
# =========================================================================================
elif menu == "🍦 1. Regressão (Vendas de Sorvete)":
    st.title("🍦 Módulo 1: Regressão Linear (Prevendo Números)")
    st.caption("Biblioteca usada: `sklearn.linear_model.LinearRegression`")
    
    with st.expander("📖 Entenda a Teoria em Nível Humano (Clique para abrir)"):
        st.markdown("""
        * **O que a Regressão faz?** Ela prevê **quantidades numéricas** (preços, vendas, temperaturas).
        * **Analogia do Dia a Dia:** Todo mundo sabe que quanto mais quente o dia, mais picolés a sorveteria vende. A IA apenas encontra a fórmula matemática exata dessa relação.
        * **O que é X?** A Temperatura prevista (°C).
        * **O que é y?** A quantidade de sorvetes que serão vendidos.
        """)

    # 1. Base em listas simples
    X_temp = [[18], [22], [26], [30], [35]] # Dias frios a muito quentes
    y_vendas = [40,  65,  90, 130, 180]    # Sorvetes vendidos
    
    # 2. Treinando a IA
    modelo_sorvete = LinearRegression()
    modelo_sorvete.fit(X_temp, y_vendas)
    
    st.markdown("---")
    st.markdown("### 🧪 Teste Prático do Modelo:")
    temp_escolhida = st.slider("Escolha a temperatura prevista para amanhã (°C):", 15, 42, 32)
    
    # 3. Fazendo a previsão
    previsao = modelo_sorvete.predict([[temp_escolhida]])[0]
    st.success(f"📈 Previsão da IA: Com **{temp_escolhida}°C**, a sorveteria deve vender aproximadamente **{int(previsao)} sorvetes**!")
    
    # Gráfico simples
    df_graf = pd.DataFrame({'Temperatura': [18, 22, 26, 30, 35], 'Vendas': y_vendas})
    fig = px.scatter(df_graf, x='Temperatura', y='Vendas', title="Relação Matemática: Calor x Vendas", trendline="ols")
    st.plotly_chart(fig, use_container_width=True)

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
    pos = [p for p in tokens if p in palavras_positivas]
    neg = [p for p in tokens if p in palavras_negativas]
    
    col_p1, col_p2 = st.columns(2)
    col_p1.metric("👍 Elogios Detectados", len(pos))
    col_p2.metric("👎 Reclamações Detectadas", len(neg))
    
    if len(pos) > len(neg):
        st.success(f"🟢 **CLIENTE SATISFEITO!** Palavras positivas encontradas: `{pos}`")
    elif len(neg) > len(pos):
        st.error(f"🔴 **CLIENTE INSATISFEITO!** Problemas encontrados: `{neg}`")
    else:
        st.warning("🟡 **AVALIAÇÃO NEUTRA / INFORMATIVA**")

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