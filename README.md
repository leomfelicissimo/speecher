# Speecher

Criei esta API com o intuito de preservar uma ideia que tenho há algum tempo. A ideia basicamente é pesquisar imagens relacionadas com um tipo de texto.

## BackEnd

### Instale o python3 e faça clone do repo e crie um ambiente virtual:

```
$ python3 -m venv ./venv
```

### Instale as dependências
```
$ pip install -r requirements.txt
```

### Instale o modelo de português do spaCy
```
$ python -m spacy download pt
```

### Execute a aplicação
```
$ FLASK_APP=server.py flask run
```

## FrontEnd

### Instale as dependências

A partir do diretório web. Execute um npm install
```
$ npm install
```

### Inicie a aplicação

Uma vez que o server esteja iniciado e em execução. Inicie o frontend
```
$ npm start
```

## Criado com:
- [Python](https://www.python.org/): Python is a programming language that lets you work quickly and integrate systems more effectively.
- [spaCy](https://spacy.io/): Industrial-Strength Natural Language Processing in Python
- [Flask](http://flask.pocoo.org/): Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions
- [React](https://reactjs.org/): A JavaScript library for building user interfaces
- [Pixabay](https://pixabay.com/pt/): Imagens grátis impressionantes

## Autor
- Leonardo Felicissimo