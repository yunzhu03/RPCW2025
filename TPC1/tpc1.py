import json

def main():
    
    # abrir ficheiro json
    file = open('emd.json','r')
    
    ttl = open('resultado.ttl', 'a')

    # dicionário do ficheiro json
    data = json.load(file)
    
    exame_individual = "Exame"
    modalidade_individual = "Modalidade"
    pessoa_individual = "Pessoa"
    
    # iterando para cada pessoa
    for person in data:
        
        id = person['_id']
        
        exame_individual = "Exame"+id
        modalidade_individual = "Modalidade"+id
        pessoa_individual = "Pessoa"+id
        
        # Exame
        dataEMD = person['dataEMD']
        resultado = person['resultado']
        
        ttl.write("\t :"+exame_individual+" rdf:type owl:NamedIndividual ;\n")
        ttl.write("\t\t :dataEMD "+"\""+dataEMD+"\" ;\n")
        ttl.write("\t\t :resultado "+"\""+str(resultado).lower()+"\"^^xsd:boolean .\n")
        
        # Modalidade
        modalidade = person['modalidade']
        
        ttl.write("\t :"+modalidade_individual+" rdf:type owl:NamedIndividual ;\n")
        ttl.write("\t\t :modalidade "+"\""+modalidade+"\" .\n")
        
        # Pessoa
        nome = person['nome']
        primeiro = nome['primeiro']
        ultimo = nome['Ãºltimo']
        
        idade = person['idade']
        genero = person['gÃ©nero']
        morada = person['morada']
        email = person['email']
        federado = person['federado']
        clube = person['clube']
        
        ttl.write("\t :"+pessoa_individual+" rdf:type owl:NamedIndividual ,\n")
        ttl.write("\t\t\t [ rdf:type owl:Restriction ;\n")
        ttl.write("\t\t\t   owl:onProperty owl:topObjectProperty ;\n")
        ttl.write("\t\t\t   owl:someValuesFrom :Pessoa\n")        
        ttl.write("\t\t\t ] ;\n")
        
        ttl.write("\t\t :temExame :"+exame_individual+" ;\n")
        ttl.write("\t\t :temModalidade :"+modalidade_individual+" ;\n")
        ttl.write("\t\t :clube \""+clube+"\" ;\n")
        ttl.write("\t\t :email \""+email+"\" ;\n")
        ttl.write("\t\t :federado \""+str(federado).lower()+"\"^^xsd:boolean ;\n")
        ttl.write("\t\t :género \""+genero+"\" ;\n")
        ttl.write("\t\t :idade "+str(idade)+" ;\n")
        ttl.write("\t\t :morada \""+morada+"\" ;\n")
        ttl.write("\t\t :primeiro \""+primeiro+"\" ;\n")
        ttl.write("\t\t :último \""+ultimo+"\" .\n\n\n")

    file.close()
    ttl.close()
    
    return 0

if __name__ == "__main__":
    main()