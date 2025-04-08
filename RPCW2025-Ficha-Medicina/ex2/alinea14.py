import csv

""" 
14. Cria um query SPARQL que poduza uma distribuição das doenças pelos sintomas, ou seja, dá como
resultado uma lista de pares (sintoma, nº de doenças com o sintoma);

"""

from rdflib import Graph, Namespace, RDF, OWL

g = Graph()
g.parse("med_doentes2.ttl")

q = """
    select ?s (count(?d) as ?ds) where {
        ?s a :Symptom .
        ?d a :Disease .
        ?d :hasSymptom ?s .
    }
    group by ?s
    """

n = Namespace("http://www.example.org/disease-ontology#")

results = g.query(q)

for r in results:
    print(r[0].split("#")[1],r[1])