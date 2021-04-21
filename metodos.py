#!/usr/bin/env python
# coding: utf-8

# In[6]:


#metodo de biseccion
import math
#funcion a sustituir
def poli(x):
      y = math.tan(x)-0.1*x
      return (y)
#Programa principal
print ("Este programa encuentra una raíz, por el método de bisección")
xi=float(input('Introduce el valor de xi: '))
xs=float(input('Introduce el valor de xs: '))
error=float((input('Introduce el error: ')))
xa = (xi+xs)/2.0
i=0
print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('i','xi','xs','xa','signo','cambio','ERROR'))
while abs(poli(xa)) > error:
    i=i+1
    xa = (xi+xs)/2.0
    if poli(xi)*poli(xa) < 0:
        xs=xa
        signo="negativo"
        limite="superior"
    else:
        xi=xa
        signo="positivo"
        limite="inferior"
    print('{:^10}{:^10.4f}{:^10.4f}{:^10.4f}{:^10}{:^10}{:^10.4f}'.format(i,float(xi),float(xs),float(xa),signo,limite,float(poli(xa))))
print("La raíz es: ",xa)


# In[7]:


#metodo de newton
import math
#funcion a sustituir
def fx(x):
    return 2*math.sin(math.pi*x)+x 
#derivada de la funcion a sustutuir
def derivadafx(x):
    return 2*math.pi*math.cos(math.pi*x)+1 

def errorabsoluto(xactual,xanterior):
    return ((xactual-xanterior)/xactual)


# In[8]:


def newton(x,cota,iteraciones):
    error=1
    i=0
    while error>cota:
        i=i+1
        xactual=x-(fx(x)/derivadafx(x))
        error=errorabsoluto(xactual,x)
        x=xactual
        print ("iteracion: ",i," f(x): ",fx(x)," f'(x): ",derivadafx(x),"   Error: ",error)
    print("la raiz es: ",xactual)


# In[9]:


#x0,tolerancia a sustituir
newton(1,0.01,10)


# In[10]:


#metodo de la secante
import math
#funcion a sustituir
def fxsecan(x):
    return math.tan(math.pi*(x))-6

def errorabsoluto(xactual,xanterior):
    return abs(((xactual-xanterior)/xactual))


# In[11]:


def secante(xo,xi,cota,iteraciones):
    error=1
    i=0
    while error>cota:
        i=i+1
        xactual=xi-((fxsecan(xi)*(xo-xi))/(fxsecan(xo)-fxsecan(xi)))
        error=errorabsoluto(xactual,xi)
        xo=xi
        xi=xactual
        if error>=cota:
            print ("iteracion: ",i," fx: ",fxsecan(xi),"   Error: ",error)
    print("la raiz es: ",xactual)


# In[12]:


#x0,xi,tolerancia a sustituir
secante(0,0.44,0.001,10)


# In[13]:


#metodo de punto fijo
import math
def fx(x):
    return math.exp(-x)

def errorabsoluto(xactual,xanterior):
    return abs(((xactual-xanterior)/xactual))


# In[14]:


import math

def punto_fijo(x,cota,iteraciones):
    error=1
    i=0
    while error>cota:
        i=i+1
        xactual=fx(x)
        error=errorabsoluto(xactual,x)
        x=xactual
        if error>=cota:
            print ("iteracion: ",i," fx(x): ",fx(x)," Error: ",error)
    print("la raiz es: ",xactual)


# In[15]:


#x0,tolerancia a sustituir
punto_fijo(0.44,0.001,10)


# In[ ]:




