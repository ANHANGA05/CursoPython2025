def minhaFuncao(seq1,seq2):
    res=[]                  # começar vazio
    for x in seq1:          # Percorre seq1
        if x in seq2:       # Item comum
            res.append(x)   #adicionar no fim
    return res

saida=minhaFuncao("SPAM","SCAM")
print(saida)

