import json
import shutil

linguas = ["Francês", "Inglês", "Português"]
paises = ["Estados_Unidos", "França", "Ingraterra", "Portugal"]
generos = ["Aventura", "Ação", "Comédia", "Drama", "Ficção", "Infantil", "Romance", "Terror", "Thriller"]
atores = ["Billy_Burke", "Kristen_Stewart", "Robert_Pattinson", "Taylor_Lautner", "Sarah_Carke"]
realizadores = ["Catherine_Hardwick"]

def formatar_nome(nome):
    return nome.replace(" ", "_").replace(".","").replace("'","").replace("?","").replace(",","").replace(";","") if nome else "N_A"

def novoGenero(genero):
    if genero and genero not in generos:
        generos.append(genero)
    g = f":{formatar_nome(genero)} rdf:type owl:NamedIndividual ,\n    :Género .\n"
    return g

def novaLingua(lingua):
    if lingua and lingua not in linguas:
        linguas.append(lingua)
    l = f":{formatar_nome(lingua)} rdf:type owl:NamedIndividual ,\n    :Língua .\n"
    return l

def novoPais(pais):
    if pais and pais not in paises:
        paises.append(pais)
    p = f":{formatar_nome(pais)} rdf:type owl:NamedIndividual ,\n    :País .\n"
    return p

def novoAtor(nome):
    if nome and nome not in atores:
        atores.append(nome)
    a = f":{formatar_nome(nome)} rdf:type owl:NamedIndividual ,\n    :Ator .\n"
    return a

def novoRealizador(nome):
    if nome and nome not in realizadores:
        realizadores.append(nome)
    r = f":{formatar_nome(nome)} rdf:type owl:NamedIndividual ,\n    :Realizador .\n"
    return r

def generoFilme(lista_generos):
    if not lista_generos:
        return ""
    # Join all genres by comma after formatting each
    genres_str = ", ".join(":" + formatar_nome(g) for g in lista_generos if g)
    return f":temGénero {genres_str} ;\n"

def novoFilme(titulo, duracao, data, pais, diretor, elenco, lista_generos, sinopse=None):
    filme_uri = f":{formatar_nome(titulo)}"
    filme = f"{filme_uri} rdf:type owl:NamedIndividual ,\n    :Filme ;\n"
    filme += f"    :título \"{titulo}\";\n"

    if duracao is not None:
        filme += f"    :duração {int(duracao)};\n"

    if data:
        filme += f"    :data \"{int(float(data))}\";\n"

    if pais:
        filme += f"    :temPaísOrigem :{formatar_nome(pais)} ;\n"

    filme += generoFilme(lista_generos)

    if diretor:
        filme += f"    :temRealizador :{formatar_nome(diretor)} ;\n"

    for pessoa in elenco:
        if pessoa:
            filme += f"    :temAtor :{formatar_nome(pessoa)} ;\n"

    if sinopse:
        filme += f"    :sinopse \"{sinopse}\";\n"

    # Ensure all separators are `;`, then replace the last one with `.`
    filme = filme.rstrip(" ;\n") + " .\n"
    return filme


if __name__ == '__main__':
    with open("movies.json", "r", encoding="utf-8") as file:
        movies = json.load(file)

    shutil.copy("Cinema.ttl", "Cinema_povoado.ttl")

    with open("Cinema_povoado.ttl", "a", encoding="utf-8") as f:
        for m in movies.get("movies", []):
            diretor_nome = m["peopleInvolved"][0].get("name") if m.get("peopleInvolved") and len(m["peopleInvolved"]) > 0 else None
            diretor_ttl = novoRealizador(diretor_nome) if diretor_nome else ""

            ator_ttls = "\n".join(novoAtor(p.get("name")) for p in m.get("peopleInvolved", []) if p.get("name")) if m.get("peopleInvolved") else ""

            pais_ttl = novoPais(m.get("originalCountry"))

            genero_ttls = "\n".join(novoGenero(g) for g in m.get("genres", []) if g)

            filme_ttl = novoFilme(
                titulo=m.get("originalTitle"),
                duracao=m.get("duration"),
                data=m.get("releaseYear"),
                pais=m.get("originalCountry"),
                diretor=diretor_nome,
                elenco=[p.get("name") for p in m.get("peopleInvolved", []) if p.get("name")],
                lista_generos=m.get("genres", []),
                sinopse=m.get("sinopse")
            )

            ttl_output = "\n".join(filter(None, [pais_ttl, genero_ttls, diretor_ttl, ator_ttls, filme_ttl]))

            f.write("\n" + ttl_output)
