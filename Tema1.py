#!/usr/bin/env python
# coding: utf-8

# In[325]:


import numpy as np
import matplotlib.pyplot as plt
import math


# In[326]:


# Ex.1

def metoda_bisectiei(f, a, b, eps = 1e-7): # am ales epsilon a.i. sa avem o precizie de 7 zecimale
    
    # calculam valorile in capetele intervalului
    f_a = f(a)
    f_b = f(b)
    
    # TREBUIE SA AIBA SEMNE DIFERITE!!
    assert f_a * f_b < 0
    
    # prima estimare, mijlocul intervalului initial
    x_num = (a + b) / 2
    
    # numarul necesar de iteratii
    N = math.floor(1 + math.log((b - a) / eps))
    
    # algoritmul:
    for i in range(N):
        value = f(x_num)
        if value == 0: # am gasit radacina
            break
        elif f_a * value < 0:
            b= x_num # modificam capatul b al intervalului
        else:
            a =x_num # modificam capatul a al intervalului
        x_num = (a + b) / 2 # micsoram intervalul in care cautam

    return x_num


# In[327]:


# Ex.1

f = lambda x: x ** 2 - 8   # am ales acest "f" deoarece metoda bisectiei pe "f" va calcula solutia (radical8) cu precizia ceruta


# In[328]:


# Ex.1

print('EX. 1: ')
print(metoda_bisectiei(f, 2, 3)) # sqrt(8) se gaseste in intervalul (2, 3)=> aplicam metoda bisectiei pe acest interval


# In[329]:


# Ex.2

# ecuatia din stanga egalului:
f = lambda x: math.exp(x-2) 

# ecuatia din dreapta egalului:
g = lambda x: math.cos(math.exp(x-2)) + 1

# ecuatia modificata dupa ce am dus toti termenii intr-un singur membru:
h = lambda x: math.cos(math.exp(x-2)) + 1 - math.exp(x-2)


# In[330]:


# Ex.2

# aplic metoda bisectiei pentru functia "h" pe intervalul(2,3) pentru a obtine punctul de intersectie a celor 2 functii "f" si "g"
# am ales acest interval, fiind un interval apropiat solutiei din reprezentarea grafica 
print('EX. 2: ')
pct_intersectie = metoda_bisectiei(h, 2, 3)
print('Punctul de intersectie: ', pct_intersectie)


# In[331]:


# Ex.2
### Desenez graficul functiilor "f" si "g", luand intervalul (-5,5)

plt.subplots(1, dpi=100)
# iau 100 de numere egal departate din intervalul (-5, 5):
x = np.linspace(-5, 5, 100)

# aplic functiile f si g pe datele din x, adica pe toate numerele din intervalul ales (-5, 5):
y_f = [f(number) for number in x] 
y_g = [g(number) for number in x]

plt.title('Intersectia graficelor functiilor de la EXERCITIUL 2')
plt.xlabel('x')
plt.ylabel('y')

# graficul functiei "f" este reprezentat cu portocaliu, graficul functiei "g" cu albastru, iar punctul de intersectie cu rosu :
plt.plot(x, y_f, 'orange')
plt.plot(x, y_g, c= 'blue')
plt.axvline(0, c='black')
plt.axhline(0, c='black')
plt.scatter(pct_intersectie, f(pct_intersectie), c='red')


# In[332]:


# Ex.3   a)

def pozitie_falsa(f, a0, b0, eps = 1e-7):
    # N = numarul de iteratii
    N = 0
    a = [0] # a[0] = a0, a[1] = a1 ... din pseudocod
    b = [0] # b[0] = b0, b[1]= b1... din pseudocod
    x = [0] # x[0]= x0,x[1]= x1... din pseudocod
    k = 0;
    a[0] = a0
    b[0] = b0
    # formula lui xk cand k = 0:
    x[0] = (a[0] * f(b[0])) - b[0] * f(a[0]) / (f(b[0]) - f(a[0]))

    while True:
        k = k + 1
        N = N + 1
        a.append(0)
        b.append(0)
        x.append(0)
        
        if f(x[k-1]) == 0:
            x[k] = x[k-1]
            break
        # modificam intervalul in functie de produs, pentru a putea la urmatorul pas sa obtinem urmatorul x (intersectam axa Ox):
        elif f(a[k-1]) * f(x[k-1]) < 0:
            a[k] = a[k-1]
            b[k] = x[k-1]
            # formula lui xk:
            x[k] = (a[k]*f(b[k])-b[k]*f(a[k])) / (f(b[k])-f(a[k]))
        elif f(a[k-1])*f(x[k-1]) > 0:
            a[k] = x[k-1]
            b[k] = b[k-1]
            # formula lui xk:
            x[k] = (a[k]*f(b[k])-b[k]*f(a[k])) / (f(b[k])-f(a[k]))
            
        # conditie in cazul in care radacina este 0:
        if f(x[k]) == 0 and x[k] == 0:
            return(0.0,N)
    
         # conditia de oprire:
        if not abs(x[k] - x[k-1]) / abs(x[k-1]) >= eps:
            return (x[k], N)


# In[333]:


# Ex.3  b)

eps = 1e-7
i = lambda x: (x ** 3) + (3 * (x ** 2) ) - (4 * x)


# In[334]:


# Ex.3
### Desenez graficul functiei "i" si solutiile sale, luand intervalul (-5,5)

print('EX. 3: ')
plt.subplots(1, dpi=100)

# iau 100 de numere egal departate din intervalul (-5, 5):
x = np.linspace(-5, 5, 100)

# aplic functia "i" pe datele din x, adica pe toate numerele din intervalul ales (-5, 5):
y = [i(number) for number in x]

# denumim plot-ul si axele
plt.title('EXERCITIUL 3')
plt.xlabel('x')
plt.ylabel('y')

# graficul functiei "i":
plt.plot(x, y, c = 'green')
plt.axvline(0, c='black')
plt.axhline(0, c='black')
plt.ylim(-5,13.5)


# Din reprezentarea grafica a functiei => solutiile sunt punctele: (-4, 0), (0, 0), (1, 0) =>
# => valorile alese pentru a0 si b0 sunt aproape de aceste puncte:
a = pozitie_falsa(i, -4 - eps, -4+eps, eps)
print('Solutie: ', a[0], ' Numar de iteratii: ', a[1])
b = pozitie_falsa(i, -eps, eps, eps)
print('Solutie: ', b[0], ' Numar de iteratii: ', b[1])
c = pozitie_falsa(i, 1 - eps, 1 + eps, eps)
print('Solutie: ', c[0], ' Numar de iteratii: ', c[1])

# solutiile reprezentate cu rosu:
plt.scatter(a[0], 0, c='red')
plt.scatter(b[0], 0, c='red')
plt.scatter(c[0], 0, c='red')


# In[335]:


# Ex.4  a)

def secanta(f, a, b, x0, x1, eps = 1e-7):
    # N = numarul de iteratii
    N = 0
    x = [0,0]
    k = 1
    x[0] = x0 # x[0] = x0, x[1] = x1... x[k] = xk   din pseudocod
    x[1] = x1


    while True:
        k = k + 1
        N = N + 1
        x.append(0)
        
        # formula lui xk:
        x[k] = (x[k-2] * f(x[k-1]) - x[k-1] * f(x[k-2])) / (f(x[k-1]) - f(x[k-2]))

        if x[k] < a or x[k] > b:
            print("Introduceti alte valori pentru x0 si x1")
            return
      
         # conditie in cazul in care radacina este 0:
        if f(x[k]) == 0:
            return(0.0, N)
        
        # conditia de oprire:
        if not abs(x[k] - x[k-1]) / abs(x[k-1]) >= eps:
            return (x[k], N)


# In[336]:


# Ex.4  b)

j = lambda x: (x ** 3) + (x ** 2) - (6 * x)
eps = 1e-7


# In[337]:


# Ex.4
### Desenez graficul functiei "i" si solutiile sale, luand intervalul (-5,5)

print('EX. 4: ')
# iau 100 de numere egal departate din intervalul (-3, 3):
x = np.linspace(-3, 3, 100)

# aplic functia "j" pe datele din x, adica pe toate numerele din intervalul ales (-3, 3):
y = [j(p) for p in x]

# graficul functiei "j":
plt.plot(x, y)
plt.axvline(0, c='black')
plt.axhline(0, c='black')

# denumim plot-ul si axele
plt.title('EXERCITIUL 4')
plt.xlabel('x')
plt.ylabel('y')


# Din reprezentarea grafica a functiei => solutiile sunt punctele: (-3, 0), (0, 0), (2, 0) =>
# => valorile alese pentru a0 si b0 sunt aproape de aceste puncte:
a = secanta(j, -3, 3, -3-eps, -3+eps, eps)
print('Solutie: ', a[0], ' Numar de iteratii: ', a[1])
b = secanta(j, -3, 3, -0.5, 0.5, eps)
print('Solutie: ', b[0], ' Numar de iteratii: ', b[1])
c = secanta(j, -3, 3, 1.5, 2.5+ eps, eps)
print('Solutie: ', c[0], ' Numar de iteratii: ', c[1])

# solutiile reprezentate cu rosu:
plt.scatter(sol1[0], 0, c='red')
plt.scatter(sol2[0], 0, c='red')
plt.scatter(sol3[0], 0, c='red')


# In[ ]:





# In[ ]:




