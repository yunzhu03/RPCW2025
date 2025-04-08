import csv

""" 
15. Cria um query SPARQL que poduza uma distribuição das doenças pelos tratamentos, ou seja, dá
como resultado uma lista de pares (tratamento, nº de doenças com o tratamento).

"""

from rdflib import Graph, Namespace, RDF, OWL

g = Graph()
g.parse("med_doentes2.ttl")

q = """
    select ?t (count(?d) as ?ds) where {
        ?t a :Treatment .
        ?d a :Disease .
        ?d :hasTreatment ?t .
    }
    group by ?t
    """

n = Namespace("http://www.example.org/disease-ontology#")

results = g.query(q)

for r in results:
    print(r[0].split("#")[1],r[1])