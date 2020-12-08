#!/usr/bin/env python
# coding: utf-8

# In[102]:


import numpy as np
import matplotlib.pyplot as plt
import math
import sys


# In[115]:


# Ex. 1:

A = np.array([[0.,1.,2., -4.], [-10.,-3.,5., 2.], [-5.,-7.,-1., -6.], [-10.,-7.,-1., 3.]])
b=np.array([[-8.],[7.],[-18.],[-15.]])
# Numarul de linii si coloane:
n = A_.shape[0]

x = np.zeros(n)

# Matricea extinsa:
A_ = np.concatenate((A, b), axis=1) 

def det():
    """ Functia returneaza determinantul matricii A 
    daca aceasta admite solutie unica"""
    
    # Determinantul matricii:
    det_A = np.linalg.det(A)
    det_A

    # Verificam daca admite solutie unica:
    if np.abs(det_A) < 1e-14:
        return None
    else:
        return det_A


indeces = np.arange(n-1)
def gauss_cu_pivotare_totala():
    """ Functia determina solutia sistemului 
    prin metoda Gauss cu pivotare totala. Sistemul
    trebuie sa aiba solutie unica"""
    
    if not det():
        print("Sistemul nu are solutie unica")
    else:
        for k in range (0, n-1):
            # Submatrice:
            subMat = A_[k:,k:n-1]
            # print(subMat)

            # Elementul maxim din submatrice:
            elem_max = np.argmax(subMat)
        
            # Indexul elementului maxim din submatrice:
            index_max = np.unravel_index(elem_max, subMat.shape)
    
            # Indexul elementului maxim din matricea extinsa:
            index_max = (index_max[0] + k, index_max[1] + k)

            # Indexul in matricea extinsa si interschimbam:
            A_[[k, index_max[0] + k]] = A_[[index_max[0] + k, k]]
            A_[:, [index_max[1] + k,k]] = A_[:, [k, index_max[1] + k]]

            # Actualizam indicii
            indeces[k], indeces[index_max[1] + k] = indeces[index_max[1] + k], indeces[k]


            # Facem elementele de sub diagonala principala egale cu 0:
            D = A_[k + 1:, k] / A_[k, k]  # Determinam raportul pentru fiecare linie.
            A_[k + 1:, :] = A_[k + 1:, :] - np.outer(D, A_[k, :]) # Inmultesc fiecare raport cu prima linie si actualizez matricea.
        
            # Obtinem un sistem superior triunghiular
            # Aplicam metoda substitutiei descendente:
            
            for i in range(n - 1, -1, -1):
                coef = A[i, i + 1:]
                val = x[i + 1:]

                x[i] = (b[i] - coef @ val) / A[i, i]

            
            # => Se obtine solutia sistemului prin metoda Gauss cu pivotare totala
            return x
gauss_cu_pivotare_totala()


# In[104]:


# Ex. 2
B = np.array([[0.,-10.,-9.,-8.], [8.,-9.,-8.,1.], [5.,-6.,-10.,6.], [6.,8.,5.,-5.]])


# In[105]:


# Ex. 3
A2 = np.array([[0.,2.,-9.,-9.], [4.,4.,-4.,0.], [-7.,-5.,2.,9.], [-4.,-3.,-1.,9.]])
b2 = np.array([[-107.],[12.],[22.],[26.]])


# In[116]:


# Ex. 4

C = np.array([[81.,0.,45., 90.], [0.,16.,-36., -8.], [45.,-36.,170., 68.], [90.,-8.,68.,120.]])
# det. daca matricea e pozitiv definita
def positive_def():
    return np.all(np.linalg.eigvals(C) > 0)

# det. daca matricea e simetrica
def symmetric_matrix():
    return C == C.traspose()

def cholesky():
    """Factorizarea Cholesky pe matricea C, care trebuie sa fie
    simetrica si pozitiv definita. Functia returneaza 
    factorizarea Cholesky pe matricea C"""
    
    # Daca matricea nu este simetrica si pozitiv definita, atunci aceasta nu admite factorizarea Cholesky:
    if not positive_def() and not symmetric_matrix():
        print("Matricea C nu admite factorizarea Cholesky")
        
    n = C.shape[0]

    # Cream matricea O -- matrice nula
    O = [[0.0] * n for i in range(n)]

    # Factorizarea Cholesky:
    for i in range(n):
        for k in range(i + 1):
            tmp_sum = sum(O[i][j] * O[k][j] for j in range(k))
            
            # Elementele de pe diagonala principala:
            if (i == k): 
                O[i][k] = math.sqrt(C[i][i] - tmp_sum)
            else:
                
                O[i][k] = (1.0 / O[k][k] * (C[i][k] - tmp_sum))
    return O
    
print(cholesky())


# In[ ]:





# In[ ]:





# In[ ]:




