# TPC3: Acrescentar 6 perguntas diferentes. Se possível usar os 3 tipos de questão.

- Fazer questões:
    - V/F
    - 4 Respostas 1 Verdadeira
    - (não foi feito) Correspondência (duas listas com a mesma cardinalidade e têm que fazer match com a outra)


Exitem 6 tipos de questões:

1. Em que ano é que ocorreu a batalha {batalhaSel['batalha']}?
> 4 opções

2. Em que dinastia é que pertence o rei {dinastia['rei']}?
> 4 opções - mais que um rei numa dinastia -> lista de dinastias diferentes

3. A conquista {conquistas[0]['conquista']} ocorreu em {conquistas[indexConquista]['data']}?
> V/F

4. O rei {reis[0]['nome']} é conhecido como {reis[indexConquista]['cognome']}?
> V/F

5. O rei conhecido por {cognomeSel['cognome']} é o...
> 4 opções

6. Quando ocorreu a conquista {conquistaSel['nome']}?
> 4 opções