## TPC2

Responder a questões do dataset da História de Portugal a partir de instruções em SPARQL.

### a. Quantos triplos existem na ontologia?
```
SELECT (COUNT(?s) AS ?triplos) WHERE { 
    ?s ?p ?o .
}
```
R.: Existem 6603 triplos. Cada triplo tem um 's', 'p' e 'o', contando o número de qualquer um destes elementos, obtemos o número de triplos na ontologia.

// (count(*) as ?triplos)

### b. Que classes estão definidas?
```
SELECT DISTINCT ?classe WHERE { 
  ?s rdf:type ?class .
}

```
R.: 51 classes definidas. 

### c. Que propriedas tem a classe "Rei"?
```
SELECT DISTINCT ?propriedade WHERE {
    ?s a :Rei .
    ?s ?propriedade ?o .
}
```
R.: 16 propriedades.

### d. Quantos reis aparecem na ontologia?
```
SELECT (COUNT(?s) AS ?numDeReis) WHERE { 
    ?s a :Rei .
}
```
R.: 32 reis.

### e. Calcula uma tabela com o seu nome, data de nascimento e cognome.
```
SELECT ?nome ?dataNascimento ?cognomes WHERE { 
    ?s a :Rei .
    ?s :nome ?nome .
    ?s :nascimento ?dataNascimento .
    ?s :cognomes ?cognomes .
}

ponto e virgula abrevia o sujeito
SELECT ?nome ?dataNascimento ?cognomes WHERE { 
    ?s a :Rei ;
       :nome ?nome ;
       :nascimento ?dataNascimento ;
       :cognomes ?cognomes .
}
```
R.: Feito com base na forma como a informação era armazenada no grafo.

### f. Acrescenta à tabela anterior a dinastia m que cada rei reinou.
```
SELECT ?nome ?dataNascimento ?cognomes ?nomeDinastia WHERE { 
    ?s a :Rei .
    ?s :nome ?nome .
    ?s :nascimento ?dataNascimento .
    ?s :cognomes ?cognomes .
    ?s :temReinado ?reinado .
    ?reinado :dinastia ?dinastia .
    ?dinastia :nome ?nomeDinastia . 
}
```
R.: Cada rei tem um reinado e a esse reinado vai se buscar a dinastia.

### g. Qual a distribuição de reis pelas 4 dinastias?
```
SELECT ?dinastia (GROUP_CONCAT(?nome; separator=", ") AS ?nomes) WHERE { 
    ?s a :Rei .
    ?s :nome ?nome .
    ?s :temReinado ?reinado .
    ?reinado :dinastia ?dinastia .
}

GROUP BY ?dinastia 


select ?dinastia (count(?monarca) as ?nmonarca) where {
    ?monarca a :Rei .
    ?monarca :temReinado/:dinastia ?dinastia.
}
group by ?dinastia
```

### h. Lista os descobrimentos (sua descrição) por ordem cronológica.
```
SELECT ?dataDescobrimento ?notas WHERE { 
    ?descobrimentos a :Descobrimento .
    ?descobrimentos :data ?dataDescobrimento .
    ?descobrimentos :notas ?notas.
}
ORDER BY ?dataDescobrimento
```

### i. Lista as várias conquistas, nome e data, juntamente com o nome que reinava no momento.
```
SELECT ?nomeConquista ?dataConquista ?nomeReinador WHERE { 
    ?conquistas :nome ?nomeConquista .
    ?conquistas :data ?dataConquista .
    ?conquistas :temReinado ?reinado .
    ?reinado :temMonarca ?nomeReinador .
}
```

### j. Calcula uma tabela com o nome, data de nascimento e número de mandatos de todos os presidentes portugueses.
```
SELECT ?nomePresidente ?dataNascimento (COUNT(?mandatos) AS ?numeroMandatos) WHERE { 
    ?presidentes a :Presidente .
    ?presidentes :nome ?nomePresidente .
    ?presidentes :nascimento ?dataNascimento .
    ?presidentes :mandato ?mandatos .
}
GROUP BY ?nomePresidente ?dataNascimento
```

### k. Quantos mandatos teve o presidente Sidónio Pais? Em que datas iniciaram e terminaram esses mandatos?
```
SELECT ?nome WHERE { 
    ?presidente a :Presidente .
    ?presidente :nome ?nome .

}

#"Sidónio Bernardino Cardoso da Silva Pais"

SELECT ?mandato ?comeco ?fim WHERE { 
    ?sidonio a :Presidente .
    ?sidonio :nome "Sidónio Bernardino Cardoso da Silva Pais" .
    ?sidonio :mandato ?mandato.
    ?mandato :comeco ?comeco .
    ?mandato :fim ?fim .
}
```

### l. Quais os nomes dos partidos políticos presentes na ontologia?
```
SELECT ?nome WHERE { 
    ?partidos a :Partido .
    ?partidos :nome ?nome .
}
```

### m. Qual a distribuição dos militantes por cada partido político?
```
SELECT ?partido (GROUP_CONCAT(?nome; separator=", ") AS ?militantes) WHERE { 
    ?presidente a :Presidente .
    ?presidente :nome ?nome .
    ?presidente :partido ?partidos .
    ?partidos :nome ?partido .
}
GROUP BY ?partido

select ?nome (count(?militante) as ?militante) where {
    ?p a :Partido ;
        :nome ?nome ;
        :temMilitante ?militante .
}
group by ?nome
```

### n. Qual o partido com maior número de presidentes militantes?
```
SELECT ?partidos (COUNT(?nomePresidente) AS ?numeroPresidentes) WHERE { 
    ?presidente a :Presidente .
    ?presidente :nome ?nomePresidente .
    ?presidente :partido ?partidos .

}
GROUP BY ?partidos
ORDER BY DESC(?numeroPresidentes)
LIMIT 1
```

