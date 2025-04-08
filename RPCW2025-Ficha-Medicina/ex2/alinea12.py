import csv

""" 
12. Cria uma query CONSTRUCT que diagnostique a doença de cada pessoa, ou seja, produza uma lista
de triplos com a forma :patientX :hasDisease :diseaseY. No fim, acrescenta estes triplos à
ontologia;

"""


from rdflib import Graph, Namespace, RDF, OWL

g = Graph()
g.parse("med_doentes.ttl")

q = """
    CONSTRUCT {
        ?p :hasDisease ?d .
    } WHERE {
        ?p a :Patient .
        ?d a :Disease .
        ?p :exhibitsSymptom ?s1 .
        ?p :exhibitsSymptom ?s2 .
        ?p :exhibitsSymptom ?s3 .
        ?d :hasSymptom ?s1 .
        ?d :hasSymptom ?s2 .
        ?d :hasSymptom ?s3 .
        FILTER(?s1 != ?s2 && ?s1 != ?s3 && ?s2 != ?s3)
    } LIMIT 100
    """

n = Namespace("http://www.example.org/disease-ontology#")


for r in g.query(q):
    g.add(r)

print(g.serialize())


