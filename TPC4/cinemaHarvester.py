# 2025-03-17

import json
from query import query_graphdb

endpoint = "http://dbpedia.org/sparql" 
dataset = [] # lista de dicionários


# ver para quais desportos
with open("movies.json") as f:
    movies = json.load(f)
    
# info movies
for m in movies:
    sparql_query=f"""
    select distinct ?nome ?pais ?data ?realizador ?sinopse where {{
    <{m}> a dbo:Film.
    OPTIONAL {{ <{m}> rdfs:label ?nome. filter(lang(?nome)="en") }}
    OPTIONAL {{ <{m}> dbo:country ?p. }}
    OPTIONAL {{ ?p rdfs:label ?pais FILTER(LANG(?pais) = "en") }}
    OPTIONAL {{ <{m}> dbp:director ?r. }}
    OPTIONAL {{ ?r rdfs:label ?realizador FILTER(LANG(?realizador) = "en") }}
    OPTIONAL {{ <{m}> dbo:abstract ?sinopse. filter(lang(?sinopse)="en") }}
    OPTIONAL {{ <{m}> dbo:releaseDate ?data .}}
    }} 
    """
    
    genero_query=f"""
    select ?genero where {{
        <{m}> dbo:genre ?g.
        OPTIONAL {{ ?g rdfs:label ?genero. filter(lang(?genero)="en")}}
    }} 
    
    """
    
    atores_query=f"""
    select distinct ?ator ?nome ?origem ?data where {{
        ?ator a dbo:Person.
        <{m}> dbo:starring ?ator.
        OPTIONAL {{ ?ator foaf:name ?nome. filter(lang(?nome)="en") }}
        OPTIONAL {{ ?ator dbo:birthDate ?data. filter(lang(?data)="en") }}
        OPTIONAL {{ ?ator dbo:birthPlace ?birthPlace. }}
        OPTIONAL {{ ?birthPlace dbo:country ?origem. filter(lang(?origem)="en") }}
    }} 
    """
    
    result = query_graphdb(endpoint,sparql_query)
    result2 = query_graphdb(endpoint,atores_query)
    result3 = query_graphdb(endpoint,genero_query)
    
    atores = []
    generos = []

    for ator in result2.get('results', {}).get('bindings', []):
        atores.append({
            "id": ator.get('ator', {}).get('value', "N/A"),
            "nome": ator.get('nome', {}).get('value', "N/A"),
            "origem": ator.get('origem', {}).get('value', "N/A"),
            "dataNasc": ator.get('data', {}).get('value', "N/A")
        })

        
    for genero in result3.get('results', {}).get('bindings', []):
        generos.append(genero['genero']['value'])

    result = result.get('results', {}).get('bindings', [])[0]
    dataset.append(
        {
            "id": m,
            "titulo": result.get('nome', {}).get('value', "N/A"),
            "pais": result.get('pais', {}).get('value', "N/A"),
            "data": result.get('data', {}).get('value', "N/A"),
            "realizador": result.get('realizador', {}).get('value', "N/A"),
            "elenco": atores,
            "genero": generos,
            "sinopse": result.get('sinopse', {}).get('value', "N/A")
        }
    )


# guardar o dataset em json
with open("dataset.json","w") as fout:
    json.dump(dataset,fout,ensure_ascii=False)

    
    

