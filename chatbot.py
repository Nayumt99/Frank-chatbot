import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from textblob import TextBlob

# Carregar modelo do spaCy para português
nlp = spacy.load("pt_core_news_sm")

# Dados de treino para classificação de intenção
dados_treino = [
    ("Como está o tempo hoje?", "clima"),
    ("Onde fica a estação de trem?", "localização"),
    ("Quanto custa um café?", "preço"),
    ("Você pode me ajudar com um problema técnico?", "suporte"),
    ("Qual é o horário de funcionamento?", "horário"),
    ("Olá", "saudacao"),
    ("Tudo bem?", "saudacao"),
    ("Qual é a capital do Brasil?", "capital"),
]

# Extrair características do texto usando vetorização de palavras
vetorizador = CountVectorizer()
X = vetorizador.fit_transform([texto for texto, _ in dados_treino])
y = [intencao for _, intencao in dados_treino]

# Treinar modelo de classificação de intenção
modelo = LogisticRegression()
modelo.fit(X, y)

# Função para identificar a intenção da mensagem usando machine learning
def identificar_intencao_ml(mensagem):
    vetorizado = vetorizador.transform([mensagem])
    intencao = modelo.predict(vetorizado)[0]
    return intencao

# Função para identificar entidades nomeadas usando spaCy NER
def identificar_entidades(mensagem):
    doc = nlp(mensagem)
    entidades = [entidade.text for entidade in doc.ents]
    return entidades

# Função para processar a mensagem e retornar uma resposta
def processar_mensagem(mensagem):
    intencao_ml = identificar_intencao_ml(mensagem)
    entidades = identificar_entidades(mensagem)
    
    if intencao_ml == "clima":
        return "A previsão do tempo é ensolarada hoje."
    elif intencao_ml == "localização":
        return "A estação de trem fica no centro da cidade."
    elif intencao_ml == "preço":
        return "Um café custa R$ 5,00."
    elif intencao_ml == "suporte":
        return "Claro, posso ajudar. Qual é o problema técnico?"
    elif intencao_ml == "horário":
        return "Estamos abertos das 9h às 18h, de segunda a sexta-feira."
    elif intencao_ml == "saudacao":
        return "Olá! Como posso ajudar?"
    elif intencao_ml == "capital":
        return "A capital do Brasil é Brasília."
    else:
        # Verificar se há entidades nomeadas e fornecer resposta com base nelas
        if entidades:
            return f"Você mencionou: {', '.join(entidades)}. Como posso ajudar com isso?"
        else:
            # Verificar o sentimento da mensagem para respostas mais personalizadas
            sentimento = TextBlob(mensagem).sentiment
            if sentimento.polarity > 0:
                return "Desculpe, não entendi sua pergunta, mas estou feliz em ajudar!"
            elif sentimento.polarity < 0:
                return "Desculpe, não consegui entender sua pergunta. Se precisar de ajuda, estou aqui para você."
            else:
                return "Desculpe, não consegui entender sua pergunta."

# Função para interagir com o usuário
def interagir():
    print("Olá! Eu sou o Frank. Como posso ajudar você hoje?")
    while True:
        try:
            mensagem = input("Você: ")
            resposta = processar_mensagem(mensagem)
            print("Frank:", resposta)
        except KeyboardInterrupt:
            print("Até mais!")
            break

# Iniciar a interação
if __name__ == "__main__":
    interagir()
