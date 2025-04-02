import csv

"""
3. Vais associar cada doença criada aos respetivos sintomas;
"""

codigo_ttl = """"""

# { doença : [sintomas] }
dic = {}

dic["Flu"] = ["Fever", "Cough", "SoreThroat"]
dic["Diabetes"] = ["IncreasedThirst", "FrequentUrination", "Fatigue"]

with open("Disease_Syntoms.csv", newline='', encoding='utf-8') as csvfile:
    
    reader = csv.reader(csvfile)
    headers = next(reader)
        
    for row in reader:
        disease = row[0].replace(" ", "_").replace("(","_").replace(")","_")
        line = [symptom.replace(" ", "").replace("(","").replace(")","") for symptom in row[1:] if symptom]
        
        for s in line:
            if disease not in dic:
                dic[disease] = []
            if s not in dic[disease]:
                dic[disease].append(s)

def generate_ttl(dic):
    ttl_code = ""
    
    for disease, symptoms in dic.items():
        disease_ttl = f":{disease} a :Disease ;\n"
        symptoms_ttl = ", ".join(f":{symptom}" for symptom in symptoms)
        disease_ttl += f"    :hasSymptom {symptoms_ttl} .\n"
        
        ttl_code += disease_ttl
    
    return ttl_code

codigo_ttl = generate_ttl(dic)
            
with open("med_doencas.ttl", "a", encoding="utf-8") as file:
        file.write(codigo_ttl + "\n")