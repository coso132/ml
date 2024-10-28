# La libreria random permette di generare numeri casuali
import random
import numpy as np

#impostiamo un seme in modo da ottenere sempre (tutti) i medesimi risultati
random.seed(10)

def genera_dataset(c, n, type, l1=None, l2=None):
    x = []
    y = np.empty(c*n)

    if len(l1)!= c or len(l2)!= c:
        raise ValueError("Valori inconsistenti")

    if type == 'uniform':
        for c_i in range(c): # l1 è usato come a e l2 è usato come b
            x = x + [random.uniform(l1[c_i], l2[c_i]) for _ in range(n)]
            y[c_i*n:c_i*n+n] = (np.ones(n)*c_i)
    elif type == 'gaussian': # l1 è usato come mu e l2 è usato come sigma
        for c_i in range(c):
            x = x + [random.gauss(l1[c_i], l2[c_i]) for _ in range(n)]
            y[c_i*n:c_i*n+n] = (np.ones(n)*c_i)
    else:
        raise ValueError("Distribuzione non consentita")

    return np.array(x), y
