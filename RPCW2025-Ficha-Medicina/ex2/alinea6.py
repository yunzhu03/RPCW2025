import csv

"""
6. A partir de Disease_Treatment.csv vais criar uma instância para cada tratamento se esta ainda não existir;

se esta não existir - descartar quando existe (?)
"""

codigo_ttl = """"""

treatments = ["Rest", "Hydration", "AntiviralDrugs","InsulinTherapy","DietModification","Exercise"]
new_treatments = []
                
with open("Disease_Treatment.csv", newline='', encoding='utf-8') as csvfile:
    
    reader = csv.reader(csvfile)
    headers = next(reader)
        
    for row in reader:
        disease = row[0].replace(" ", "_").replace("(","_").replace(")","_")
        line = ["".join(word.capitalize() for word in treatment.split()).replace("(","").replace(")","") for treatment in row[1:] if treatment]
        
        for treatment in line:
            if treatment not in treatments:
                treatments.append(treatment)
                new_treatments.append(treatment)

codigo_ttl = ""
    
for t in new_treatments:
    codigo_ttl += f":{t} a :Treatment.\n"
            
with open("med_doencas.ttl", "a", encoding="utf-8") as file:
        file.write(codigo_ttl + "\n")
        