
#risolvi il problema del
# qual è il senso della vita nel mondo e tutto quanto

# risposta corretta = 42


def leggi_input():
    """ mi aspetto di ricevere 
        l'input dall'utente
        due interi 
    """
    i = int(input("intero 1: "))
    j = int(input("intero 2: "))
    return(i,j)

def risolvi_problema(c):
    soluzione = "Niente e nessuno lo sa. \nNon sarà di certo un programma così semplice a spiegarlo... XD"
    return soluzione
    pass

def stampa_risultato(r):
    print("Il senso della vita è: ", end="")
    print(r) 

def main():
    print("Inizia il mio programma")
    c = leggi_input()
    r = risolvi_problema(c)
    stampa_risultato(r)
    print("Fine.")


main()