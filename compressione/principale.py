s=str(input("inserisci la parola: "))
dollaro="$"
print(s+dollaro)
SD=s+dollaro
print(SD)
listaSD2=[SD]
for i in SD[1:]: #inizia da una posizione dopo per fare un ciclo in meno e terminare correttmante 
    primo_carattere=SD[0]
    SD2=SD[1:]# 1: serve per togliere il primo elemento
    SD=SD2#serve per aggiornare la stringa e rendere uguale a SD2
    SD2=SD+primo_carattere
    SD=SD2
    print(SD2)
    listaSD2.append(SD2)#salva la parola alla fine della lista 
print(listaSD2)

listaSD2.sort()#riordina la lista in ordine alfabetico 
print(listaSD2)

SD3=""
for i in listaSD2:
     SD3=SD3+i[-1]# la i prende la posizione della parola nella lista e il numero dentro le quadre prende l'ultimo carattere della prola nella strigna
print(SD3)