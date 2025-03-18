## TPC4: Harvester de DBPedia sobre Cinema.

Estrutura da informação de cada filme a buscar:
```
[
    {
        "id":           _________,
        "titulo":       _________,
        "país":         _________,
        "data":         _________,
        "realizador":   _________,
        "elenco":       [elencos],
        "genero":       [generos],
        "sinópse":      _________
        ""
    }
]
```
Informação de cada ator a ser buscado.
```
atores: id, nome, dataNasc, origem
```

### Resolução adaptada do código de Sport das aulas

(1) buscar a lista dos filmes manualmente, guardar resultado para um ficheiro json
```
select distinct ?filme where {
    ?filme a dbo:Film.
}
```

(2) iterar a cada filme para obter as informações 

(3) iterar sobre cada filme para buscar a. o nome de cada género e b. as informações de cada ator


