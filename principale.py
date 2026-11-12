stringa="banana"
print(stringa)
elemento_aggiunto="$"
stringa_elemento=stringa+elemento_aggiunto
print(stringa_elemento)

#per ogni i che va da 1 alla lunghezza
#stringa_elemento︃[0:i]
#i = 1 -> b
#stringa_elemento︃[i:]
#i = 1 -> anana$
#
#anana$b

for i in stringa_elemento[:-1]:
    carattere=stringa_elemento[0]
    stringa=stringa_elemento[0]+carattere
    print(stringa)