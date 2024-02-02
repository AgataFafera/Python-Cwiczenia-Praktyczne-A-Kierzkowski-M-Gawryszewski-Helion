#!/usr/bin/env python
# coding: utf-8

# In[61]:


# Napisz funkcję, która dla podanej liczby typu całkowitego tworzy łańcus znakowy z tą liczbą, 
# ale łatwiejszą do przeczytania - z trzycyfrowymi grupami cyfr oddzielnymi spacją 
# (na przykład dla 1234567 wartością funkcji powinien być łańcuch: 1 234 567. 
# Wykorzystaj funkcję str().

duza_liczba = str(input("Podaj dużą liczbę: )")) # Pobranie od użytkowanika dowolnej dużej liczby

def grupowanie(duza_liczba):
    lista_na_cyfry = list(duza_liczba) # Zamiana stringa na listę
    
    for i in range(len(lista_na_cyfry)-3, 0, -3): # Przechodzenie się po liście co 3 miejsca od końca
        lista_na_cyfry.insert(i," ") # Dodawanie spacji na każde 3 miejsce od końća
    nowa_liczba = "".join(lista_na_cyfry) # Zamiana listy na docelowy string
    return nowa_liczba

print(grupowanie(duza_liczba))

