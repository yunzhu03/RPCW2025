import json

"""
9. A partir de doentes.json vais criar as instâncias dos doentes:
    um doente deverá ter 
        um id (usa a tua imaginação), 
        um nome (extraído do dataset) e 
        uma lista de sintomas associados (extraídos do dataset);
        
# Patient instances
:Patient1 a :Patient ;
    :name "Paul Harrods";
    :exhibitsSymptom :Fever ;
    :exhibitsSymptom :Cough ;
    :exhibitsSymptom :SoreThroat .

:Patient2 a :Patient ;
    :name "Ana Montana";
    :exhibitsSymptom :IncreasedThirst ;
    :exhibitsSymptom :FrequentUrination ;
    :exhibitsSymptom :Fatigue .
    
    {
        "nome": "Dhevin Araujo",
        "sintomas": [
            "vomiting",
            "breathlessness",
            "chest_pain"
        ]
    },
    
"""

with open("doentes.json") as f:
    doentes = json.load(f)

    id = 3
    codigo_ttl = ""
    
    for doente in doentes:
        paciente = doente["nome"]
        sintomas = doente["sintomas"] # lista de sintomas
        sintomas_ttl = ""
         
        for index, sintoma in enumerate(sintomas):
            sintoma = sintoma.replace(" ","").replace("(","").replace(")","")
            if index == len(sintomas) - 1:
                sintomas_ttl += f"    :exhibitsSymptom :{sintoma} .\n"
            else:
                sintomas_ttl += f"    :exhibitsSymptom :{sintoma} ;\n"
                    
        codigo_ttl += f":Patient{id} a :Patient ;\n"
        codigo_ttl += f"    :name \"{paciente}\" ;\n"
        codigo_ttl += sintomas_ttl
        codigo_ttl += "\n"
        
        id += 1

with open("med_doentes.ttl", "a", encoding="utf-8") as file:
        file.write(codigo_ttl + "\n")
