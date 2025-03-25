# TPC 5: Povoar a ontologia com mais 500 filmes !

```
https://www.ldf.fi/service/rdf-grapher
```
> dataset de movies do Rui  

### Indivíduos
- Filme
- Língua 
- País
- Ator
- Realizador

---

### Ligações 

- Filme (temLingua) Língua
- Filme (temGénero) Género
- Filme (temPaísOrigem) País
- Filme (temAtor) Pessoa :: inverso de :: Ator (atuou) Filme
- Filme (temRealizador) Pessoa :: inverso de :: Pessoa (realizou) Filme

---

### Propriedades que não vão ser consideradas para a povoação

- Filme (temArgumento) Argumento
- Filme (temPeçaMusical) Peça_Musical
- Pessoa (escreveu) Obra :: inverso de :: Obra (foiEscrita) Pessoa
- Pessoa (compôs) Obra :: inverso de :: Obra (foicomposta) Pessoa
- Ator (temPersonagem) Personagem :: inverso de :: Personagem (éPersonagem) Ator




