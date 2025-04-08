import csv

""" 
11. Especifica queries SPARQL que permitam responder às seguintes questões:

"""

# ----------------------------------------------------------------------------
# - Quantas doenças estão presentes na ontologia?
# ----------------------------------------------------------------------------
'''
select (count(?d) as ?doencas) where {
    ?d a :Disease .
}
'''

# ----------------------------------------------------------------------------
# - Que doenças estão associadas ao sintoma "yellowish_skin"?
# ----------------------------------------------------------------------------
'''
select ?d where {
    ?d a :Disease .
    ?d :hasSymptom :yellowish_skin .
}
'''

# ----------------------------------------------------------------------------
# - Que doenças estão associadas ao tratamento "exercise"?
# ----------------------------------------------------------------------------
'''
select ?d where {
    ?d a :Disease .
    ?d :hasTreatment :exercise .
}
'''

# ----------------------------------------------------------------------------
# - Produz uma lista ordenada alfabeticamente com o nome dos doentes.
# ----------------------------------------------------------------------------
'''
select ?n where {
    ?p a :Patient .
    ?p :nome ?n .
}
order by ?d
'''