import csv

"""
2. Para os sintomas de cada doença vais criar uma instância para cada sintoma se esta ainda não existir;
"""

symptoms = ["Fever","Cough","SoreThroat","IncreasedThirst","FrequentUrination","Fatigue"]
codigo_ttl = """"""

with open("Disease_Syntoms.csv", newline='', encoding='utf-8') as csvfile:
    
    reader = csv.reader(csvfile)
    headers = next(reader)
        
    for row in reader:
        line = [symptom.replace(" ", "").replace("(","").replace(")","") for symptom in row[1:] if symptom]
        for s in line:
            if s not in symptoms:
                symptoms.append(s)
                codigo_ttl += f":{s} a :Symptom .\n"
            
            
with open("med_doencas.ttl", "a", encoding="utf-8") as file:
        file.write(codigo_ttl + "\n")
        