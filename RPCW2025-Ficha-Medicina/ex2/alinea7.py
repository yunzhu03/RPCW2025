import csv

"""
7. Vais associar cada doença criada aos respetivos tratamentos;

"""

codigo_ttl = """"""

diseases = ["Flu", "Diabetes"]

with open("Disease_Syntoms.csv", newline='', encoding='utf-8') as csvfile:
    
    reader = csv.reader(csvfile)
    headers = next(reader)
        
    for row in reader:
        disease = row[0].replace(" ", "_").replace("(","_").replace(")","_")
        
        if disease not in diseases:
                diseases.append(disease)
                
                
treatments = ["Rest", "Hydration", "AntiviralDrugs","InsulinTherapy","DietModification","Exercise"]
                
with open("Disease_Treatment.csv", newline='', encoding='utf-8') as csvfile:
    
    reader = csv.reader(csvfile)
    headers = next(reader)
        
    for row in reader:
        disease = row[0].replace(" ", "_").replace("(","_").replace(")","_")
        treatments = ["".join(word.capitalize() for word in treatment.split()).replace("(","").replace(")","") for treatment in row[1:] if treatment]
        
        treatments_ttl = ", ".join(f":{treatment}" for treatment in treatments)
        codigo_ttl += f":{disease} :hasTreatment {treatments_ttl} .\n"
            
            
with open("med_doencas.ttl", "a", encoding="utf-8") as file:
        file.write(codigo_ttl + "\n")
        