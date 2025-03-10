# Um jogo sobre a história de Portugal
# 2025-02-24 jcr
#
from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from flask_cors import CORS
import random
import requests
import re

app = Flask(__name__)
app.secret_key = 'História de Portugal'
CORS(app)

# Retrieve info from GraphDB
def query_graphdb(endpoint_url, sparql_query):
    headers = {
        'Accept': 'application/json', 
    }
    response = requests.get(endpoint_url, params={'query': sparql_query}, headers=headers)
    if response.status_code == 200:
        return response.json() 
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

endpoint = "http://localhost:7200/repositories/historia"
sparql_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT ?n ?o
    WHERE {
        ?s a :Rei.
    	?s :nome ?n .
    	?s :nascimento ?o.
    }
"""
result = query_graphdb(endpoint, sparql_query)
listaReis = []
for r in result['results']['bindings']:
    t = {
            'nome': r['n']['value'].split('#')[-1], 
            'dataNasc': r['o']['value'].split('#')[-1]
    }
    listaReis.append(t)

sparql_query1 = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT ?nomebatalha ?data
    WHERE {
        ?batalha a :Batalha.
        ?batalha :data ?data.
    	?batalha :nome ?nomebatalha .
    }
"""
result1 = query_graphdb(endpoint, sparql_query1)
batalhaData = []

for r in result1['results']['bindings']:
    
    year_match = re.search(r"\d{4}$", r['data']['value'].split('#')[-1])
    year = year_match.group(0) if year_match else None
    
    t = {
            'batalha': r['nomebatalha']['value'].split('#')[-1], 
            'data': year
    }
    batalhaData.append(t)

def generate_question1():
    batalhas = random.choices(batalhaData,k=4)
    batalhaSel = batalhas[random.randrange(0,4)]
    question = {
        "question": f"Em que ano é que ocorreu a batalha {batalhaSel['batalha']}?",
        "options": [batalhas[0]['data'], batalhas[1]['data'], batalhas[2]['data'], batalhas[3]['data']],
        "answer": batalhaSel['data']
    }
    return question


sparql_query2 = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT ?nomerei ?nomedinastia
    WHERE {
        ?reinado a :Reinado.
    	?reinado :temMonarca ?rei .
        ?rei :nome ?nomerei.
    	?reinado :dinastia ?dinastia.
        ?dinastia :nome ?nomedinastia.
    }
"""
result2 = query_graphdb(endpoint, sparql_query2)
dinastiaRei = []
for r in result2['results']['bindings']:
    t = {
            'rei': r['nomerei']['value'].split('#')[-1], 
            'dinastia': r['nomedinastia']['value'].split('#')[-1]
    }
    dinastiaRei.append(t)

def selecionar_opt(lista, elemDiferente):
    elems = [e for e in lista if e != elemDiferente] 
    return random.sample(elems, min(3, len(elems)))  
    
    
def generate_question2():
    dinastia = random.choice(dinastiaRei)
    diff_dinastias = list({entrada['dinastia'] for entrada in dinastiaRei})
    
    options = selecionar_opt(diff_dinastias,dinastia['dinastia'])
    options.append(dinastia['dinastia'])
    random.shuffle(options)
    
    question = {
        "question": f"Em que dinastia é que pertence o rei {dinastia['rei']}?",
        "options": [options[0], options[1], options[2], options[3]],
        "answer": dinastia['rei']
    }
    return question
    
sparql_query3 = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT ?nome ?data
    WHERE {
        ?conquista a :Conquista.
        ?conquista :nome ?nome.
    	?conquista :data ?data .
    }
"""
result3 = query_graphdb(endpoint, sparql_query3)
dataConquista = []
for r in result3['results']['bindings']:
    t = {
            'conquista': r['nome']['value'].split('#')[-1], 
            'data': r['data']['value'].split('#')[-1]
    }
    dataConquista.append(t)
    
def generate_question3():
    conquistas = random.choices(dataConquista,k=2)
    answer = random.choice([True, False])
    
    if answer:
        indexConquista = 0
    else:
        indexConquista = 1
        
    question = {
        "question": f"A conquista {conquistas[0]['conquista']} ocorreu em {conquistas[indexConquista]['data']}?",
        "options": [True, False],
        "answer": answer
    }
    return question

sparql_query4 = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT ?nome ?cognomes
    WHERE {
        ?rei a :Rei.
        ?rei :nome ?nome.
    	?rei :cognomes ?cognomes .
    }
"""
result4 = query_graphdb(endpoint, sparql_query4)
reiCognome = []
for r in result4['results']['bindings']:
    t = {
            'nome': r['nome']['value'].split('#')[-1], 
            'cognome': r['cognomes']['value'].split('#')[-1] #.split(',')
    }
    reiCognome.append(t)
    
def generate_question4():
    reis = random.choices(reiCognome,k=3)
    
    answer = random.choice([True, False])
    
    if answer:
        indexConquista = 0
    else:
        indexConquista = 1
        
    question = {
        "question": f"O rei {reis[0]['nome']} é conhecido como {reis[indexConquista]['cognome']}?",
        "options": [True, False],
        "answer": answer
    }
    return question
    
def generate_question5():
    cognomes = random.choices(reiCognome,k=4)
    cognomeSel = cognomes[random.randrange(0,4)]
    
    question = {
        "question": f"O rei conhecido por {cognomeSel['cognome']} é o...",
        "options": [cognomes[0]['nome'], cognomes[1]['nome'], cognomes[2]['nome'], cognomes[3]['nome']],
        "answer": cognomeSel['nome']
    }
    return question
    
sparql_query6 = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT distinct ?nomeconquista ?dataconquista
    WHERE {
        ?coquista a :Conquista.
    	?conquista :nome ?nomeconquista.
    	?conquista :data ?dataconquista.
    }
"""
result6 = query_graphdb(endpoint, sparql_query6)
conquistaData = []
for r in result6['results']['bindings']:
    t = {
            'nome': r['nomeconquista']['value'].split('#')[-1], 
            'data': r['dataconquista']['value'].split('#')[-1]
    }
    conquistaData.append(t)

def generate_question6():
    conquistas = random.choices(conquistaData,k=4)
    conquistaSel = conquistas[random.randrange(0,4)]
    
    question = {
        "question": f"Quando ocorreu a conquista {conquistaSel['nome']}?",
        "options": [conquistas[0]['data'], conquistas[1]['data'], conquistas[2]['data'], conquistas[3]['data']],
        "answer": conquistaSel['data']
    }
    return question

@app.route('/')
def home():
    session['score'] = 0
    return redirect(url_for('quiz'))

@app.route('/quiz', methods=['GET'])
def generate_question():
    questions = [generate_question2, generate_question3, generate_question4, generate_question5, generate_question6, generate_question1]
    random.shuffle(questions)  
    question_func = questions[0] 
    question = question_func()
    
    return render_template('quiz.html', question=question)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_answer = request.form.get('answer')
        answer_correct = request.form.get('answerCorrect')
        correct = answer_correct == user_answer
        session['score'] = session.get('score', 0) + (1 if correct else 0)
        return render_template('result.html', correct=correct, correct_answer=answer_correct, score=session['score'])

    questions = [generate_question2, generate_question3, generate_question4, generate_question5, generate_question6, generate_question1]
    random.shuffle(questions)  
    question_func = questions[0] 
    question = question_func()
    
    return render_template('quiz.html', question=question)

@app.route('/score')
def score():
    return render_template('score.html', score=session.get('score', 0))

if __name__ == '__main__':
    app.run(debug=True)
