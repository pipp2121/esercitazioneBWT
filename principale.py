#stringa="banana"
#print(stringa)
#elemento_aggiunto="$"
#stringa_elemento=stringa+elemento_aggiunto
#print(stringa_elemento)

#per ogni i che va da 1 alla lunghezza
#stringa_elemento︃[0:i]
#i = 1 -> b
#stringa_elemento︃[i:]
#i = 1 -> anana$
#
#anana$b
#stringa_elemento=stringa_elemento + elemento_aggiunto
#for i in stringa_elemento[:-1]:
    #carattere=stringa_elemento[0]
    #stringa_elemento = stringa[1:] + carattere
    #print(stringa_elemento)


s="banana"
dollaro="$"
print(s+dollaro)
SD=s+dollaro
print(SD)

for i in SD:
    primo_carattere=SD[0]
    SD2=SD[1:]# 1: serve per togliere il primo elemento
    SD=SD2
    print(SD2)