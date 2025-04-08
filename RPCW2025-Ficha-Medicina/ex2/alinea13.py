import csv

""" 
13. Cria um query SPARQL que poduza uma distribuição dos doentes pelas doenças, ou seja, dá como
resultado uma lista de pares (doença, nº de doentes);

"""

from rdflib import Graph, Namespace, RDF, OWL

g = Graph()
g.parse("med_doentes2.ttl")

q = """
    select ?d (count(?p) as ?ps) where {
        ?p a :Patient .
        ?d a :Disease .
        ?p :hasDisease ?d .
    }
    group by ?d
    """

n = Namespace("http://www.example.org/disease-ontology#")

results = g.query(q)

for r in results:
    print(r[0].split("#")[1],r[1])








