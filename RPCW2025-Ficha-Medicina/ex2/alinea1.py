import csv

"""
1. A partir de Disease_Syntoms.csv vais criar instâncias de doença (:Disease) para cada doença;
"""

diseases = ["Flu","Diabetes"]
codigo_ttl = """"""

with open("Disease_Syntoms.csv", newline='', encoding='utf-8') as csvfile:
    
    reader = csv.reader(csvfile)
    headers = next(reader)
        
    for row in reader:
        disease = row[0].replace(" ", "_").replace("(","_").replace(")","_")
        if disease not in diseases:
            diseases.append(disease)
            codigo_ttl += f":{disease} a :Disease .\n"


with open("med_doencas.ttl", "a", encoding="utf-8") as file:
        file.write(codigo_ttl + "\n")
        
    


