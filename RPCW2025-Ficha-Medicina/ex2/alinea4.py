import csv

diseases = ["Flu","Diabetes"]
diseases_ = {}
codigo_disease_ttl = """"""
codigo_ttl = """"""

# encher a lista das doenças existentes
with open("Disease_Syntoms.csv", newline='', encoding='utf-8') as csvfile:
    
    reader = csv.reader(csvfile)
    headers = next(reader)
        
    for row in reader:
        disease = row[0].replace(" ", "_").replace("(","_").replace(")","_")
        if disease not in diseases:
            diseases.append(disease)
        

with open("Disease_Description.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        
        for row in reader:
            disease = row[0].strip().replace(" ", "_").replace("(","_").replace(")","_")
            description = row[1].strip()
            
            diseases_[disease] = {
                "description": description,
            }
    

for d, des in diseases_.items():
    if d not in diseases:
        diseases.append(disease)
        codigo_disease_ttl += f":{d} a :Disease .\n"

    codigo_ttl += f"\n:{d} :description \"{des['description']}\" .\n"
    
with open("medical.ttl", "a", encoding="utf-8") as file:
        file.write(codigo_disease_ttl + "\n")
        file.write(codigo_ttl + "\n")