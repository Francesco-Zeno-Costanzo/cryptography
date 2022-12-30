import os
import random as rm


def mil_rab(p):
    '''
    Test di rpimalità di miller rabin

    Parametri
    ---------
    p : int
        numero di cui controllare la primalità

    Returns
    ---------
    Boolean True se p è primo False altrimenti
    '''
    if p == 1 or p % 2 == 0: return False
    if p == 2: return True
    m, k = p - 1, 0
    while m % 2 == 0:
        m, k = m // 2, k + 1
    a = rm.randint(2, p - 1)
    x = pow(a, m, p)
    if x == 1 or x == p - 1: return True
    while k > 1:
        x = pow(x, 2, p)
        if x == 1: return False
        if x == p - 1: return True
        k = k - 1
    return False


def is_prime(p, r):
    '''
    chiamando mil_rab controlla la primalità
    il test eseguito non è deterministico quindi
    è consigliato ripeterlo più volte

    Parameters
    ----------
    p : int
        numero di cui controllare la primalità
    r : int
        numero di volte in cui ripetere il controllo

    Returns
    ---------
    Boolean True se p è primo False altrimenti
    '''
    for i in range(r):
        if mil_rab(p):
            return True
        else:
            return False


def gen_primo(k, r):
    '''
    genera casualmnete un numero  e chiamando
    is_prime controlla se è primo

    Parameters
    ----------
    k : int
        dimensione in bit del numero che vogliamo generare
    r : int
        numero di volte in cui ripetere il controllo

    Returns
    ----------
    number : float
        numero primo di k bit
    '''
    if k < 2:
        return None
    while True:
        number = rm.randrange(pow(2, k - 1) + 1, pow(2, k), 2)
        if is_prime(number, r):
            return number


def MCD(a, b):
    '''
    Calcolo del massimo comune divisore

    Parameters
    ----------
    a, b : int
         numeri di cui calcolare il massimo comun divisore

    Returns
    ----------
    a : int
        massimo comune divisore
    '''
    while b != 0:
        a, b = b, a % b
    return a


def CO(phi):
    '''
    calcola un numero che è coprimo con phi

    Parameters
    ----------
   phi : int
         numero di cui trovare il coprimo

    Returns
    ----------
    H : int
        numero coprimo a phi
    '''
    while True:
        H = rm.randrange(2, phi)
        if MCD(H, phi) == 1:
            return H


def EMCD(a, b):
    '''
    algoritmo esteso di eculide, dati due nuemri a e b
    ne calcola  il massimo comun divisore a anche i coefficenti
    X e Y tali che: a*X + b*Y = MCD(a, b) [identità di Bézout].
    Se a e b sono coprimi allora si ha che:
    1)X è l'inverso moltiplicativo di a modulo b;
    2)Y è l'inverso moltiplicativo di b modulo a.

    Parameters
    ----------
    a, b : int
         numeri di cui calcolare MCD

    Returns
    ----------
    R : int
        resto della divisione
    X, Y : int
        coefficenti dll'identità di Bézout
    '''
    x = 0; X = 1
    y = 1; Y = 0
    r = b; R = a
    while r != 0:
        q = R // r
        R, r = r, R - q*r
        X, x = x, X - q*x
        Y, y = y, Y - q*y
    return R, X, Y


def MI(a, b):
    '''
    tramite ECDM calcola l'inverso moltiplicativo
    di a modulo b essendo a b coprimi

    Parameters
    ----------
    a, b : int
         devono essere coprimi

    Returns
    ----------
    x : int
        inverso moltiplicativo di a modulo b
    '''
    g, x, y = EMCD(a, b)
    if x < 0:
        x += b
    return x


def gen_chiavi(dim, r):
    '''
    Genera le chiavi:
    (N, e) è la chiave pubblica
    (N, d) e la chiave privata

    Parameters
    ----------
    dim : int
        dimensione in bit della chiave
    r : int
        numero di tentatici per il test di miller rabin

    Returns
    ----------
    N : int
        modulo
    e : int
        esponente pubblico
    d : int
        esponente privato
    '''
    p = gen_primo(dim, r)
    q = gen_primo(dim, r)
    N = p * q
    phi = (p - 1) * (q - 1)
    e = CO(phi)
    d = MI(e, phi)
    return N, e, d


def cifra(e, N, msg):
    '''
    cifra il messaggio

    Parameters
    ----------
    e, N : int
        esponente pubblico e modulo rispettivamente
        formano la chiave pubblica
    msg : str
        messaggio da cifrare

    Returns
    ----------
    cifr : str
        messaggio cifrato
    '''
    cifr = ""
    i = 0
    for l in msg:
        m = ord(l)
        M = pow(m, e, N)
        cifr += str(M) + " "
        k = ((i+1)*100)/len(msg)
        print(f"Percentuale di completamento: {k:.1f}% \r", end='')
        i += 1
    return cifr


def decifra(d, N, cifr):
    '''
    decifra il messaggio

    Parameters
    ----------
    d, N : int
        esponente privato e modulo rispettivamente
        formano la chiave privata
    cifr : str
        messaggio da decifrare

    Returns
    ----------
    msg : str
        messaggio decifrato
    '''
    msg = ""
    lett = cifr.split()
    i = 0
    for l in lett:
        c = int(l)
        C = pow(c, d, N)
        msg += chr(C)
        k = ((i+1)*100)/len(lett)
        print(f"Percentuale di completamento: {k:.1f}% \r", end='')
        i += 1
    return msg


def main():
    '''main del programma
    '''

    print("Il codice codifica e decodifica testi presenti su un txt. \n"
          "Anche le chiavi se, già si possiedono, devono essere in un txt\n"
          "nell'ordine N, e, d, separate da un a capo. \n"
          )

    print("Si è in possesso o si vuole generare la chiave?\ndigitare 0 per generarle, 1 altrimenti")
    E = int(input("generare? "))

    if E == 0:
        dim = int(input("\ndimensione in bit della chiave:"))
        r = int(input("numeri di tentativi per il test di miller rabin, 40 possono andare:"))
        p_gen = input('inseire path dove salvare il file:\n')
        f_gen = input('inseire nome del file (con estensione.txt):\n')
        N, e, d = gen_chiavi(dim, r)

        path = os.path.join(p_gen, f_gen)
        print(path)
        file = open(path, "w")
        file.write(str(N))
        file.write('\n')
        file.write(str(e))
        file.write('\n')
        file.write(str(d))
        file.close()
        print("Chiavi generate, veranno lette automaticamente")

    while True:
        A = int(input("\n"
                      "Digitare 1 per leggere file.txt da cifrare \n"
                      "Digitare 2 per leggere file.txt da decifrare \n"
                      "Digitare 3 per terminare l'esecuzione \n"))

        if A == 1:

            if E == 0:

                chiave = open(path, "r").read()
                chiave = chiave.split()
                N = int(chiave[0])
                e = int(chiave[1])

            elif E == 1:

                p_c = input("Path assoluto del file con le chiavi: \n")
                f_c = input('Nome del file (con estensione.txt):\n')
                path = os.path.join(p_c, f_c)

                chiave = open(path, "r").read()
                chiave = chiave.split()
                N = int(chiave[0])
                e = int(chiave[1])


            p_l_1 = input("Path assoluto del file da leggere: \n")
            f_l_1 = input('Nome del file (con estensione.txt):\n')
            pathl = os.path.join(p_l_1, f_l_1)

            p_s_1 = input("Path assoluto del file su cui scrivere: \n")
            f_s_1 = input('Nome del file (con estensione.txt),\n'
                          "se non esiste esso viene creato automaticamente: \n")
            paths = os.path.join(p_s_1, f_s_1)

            msg = open(pathl, "r").read()
            enc = cifra(e, N, msg)

            file = open(paths, "w")
            file.write(enc)
            file.close()

            print("Mesaggio cifrato e stamapto")

        elif A == 2:
            if E == 0:

                chiave = open(path, "r").read()
                chiave = chiave.split()
                N = int(chiave[0])
                d = int(chiave[2])

            elif E == 1:

                p_c = input("Path assoluto del file con le chiavi: \n")
                f_c = input('Nome del file (con estensione.txt):\n')
                path = os.path.join(p_c, f_c)

                chiave = open(path, "r").read()
                chiave = chiave.split()
                N = int(chiave[0])
                d = int(chiave[2])

            p_l_2 = input("Path assoluto del file da leggere: \n")
            f_l_2 = input('Nome del file (con estensione.txt):\n')
            pathl = os.path.join(p_l_2, f_l_2)

            p_s_2 = input("Path assoluto del file su cui scrivere: \n")
            f_s_2 = input('Nome del file (con estensione.txt),\n'
                          "se non esiste esso viene creato automaticamente: \n")
            paths = os.path.join(p_s_2, f_s_2)

            enc = open(pathl, "r").read()
            dec = decifra(d, N, enc)

            file = open(paths, "w")
            file.write(dec)
            file.close()

            print("Mesaggio decifrato e stamapto")

        elif A == 3:
            print("garzie e arrivederci")
            break


if __name__ == "__main__":
    main()