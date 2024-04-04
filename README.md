# Chatbot Frank

O Chatbot Frank é um assistente virtual desenvolvido em Python que utiliza técnicas de processamento de linguagem natural (PLN) e aprendizado de máquina para interagir com os usuários e responder às suas perguntas de forma automatizada.

## Funcionalidades

- Responde a perguntas sobre o clima, localização, preço, suporte técnico, horário de funcionamento e outros tópicos.
- Reconhece saudações e responde adequadamente.
- Identifica entidades nomeadas nas mensagens dos usuários.
- Utiliza um modelo de classificação de intenções treinado para entender as necessidades do usuário.

## Pré-requisitos

- Python 3.x instalado.
- As bibliotecas spacy, scikit-learn e textblob instaladas. Você pode instalá-las executando o seguinte comando:
````
pip install spacy scikit-learn textblob
````

- Modelo do spaCy para português instalado. Você pode instalá-lo executando o seguinte comando:
  ````
  python -m spacy download pt_core_news_sm
  ``````
## Como usar

1. Clone este repositório:
  ````
  git clone https://github.com/Nayumt99/Frank-chatbot.git
  ````

2. Navegue até o diretório do projeto:
````
cd Frank-chatbot
````

3. Execute o script Python:
````
python chatbot.py
````

4. Interaja com o chatbot digitando mensagens e pressionando Enter.

## Como contribuir

Se desejar contribuir para o desenvolvimento do Chatbot Frank, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma branch para a sua feature (git checkout -b feature/nova-feature).
3. Faça commit das suas alterações (git commit -am 'Adiciona nova feature').
4. Faça push para a branch (git push origin feature/nova-feature).
5. Crie um novo Pull Request.

## Autor

Chatbot Frank foi desenvolvido por Nayum Teixeira
