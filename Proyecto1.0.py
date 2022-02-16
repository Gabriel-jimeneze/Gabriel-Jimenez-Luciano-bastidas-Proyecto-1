

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("Student-mat.csv",delimiter =";")
notas= data["G3"]

def histo(lisA,nombre):
    plt.figure()
    plt.hist(lisA,density=True)
    plt.title("Histograma de {}".format(nombre))
def cumulativa(lisA,nombre):
    ordena=np.sort(lisA)
    n=len(ordena)
    cumulativa=np.linspace(1.0/n,1.0,n)
    plt.figure()
    plt.plot(ordena,cumulativa)
    plt.vlines(np.mean(ordena),0,1,color="red",label="promedio={:.2f}".format(np.mean(ordena)))
    plt.title("Acumulativa de {}".format(nombre))
    plt.legend()

histo(notas,"notas finales")
cumulativa(notas,"notas finales")
studytime=data["studytime"]
absences=data["absences"]
plt.figure()
plt.scatter(studytime,notas)
plt.xlabel("Tiempo de estudio")
plt.ylabel("Calificaciones")
plt.title("Agrupacion tiempo de estudio y calificaciones")

#Solo horas de estudio 
ii_1= (studytime==1)
n_1=np.count_nonzero(ii_1)

ii_2=(studytime==2)
n_2=np.count_nonzero(ii_2)

ii_3=(studytime==3)
n_3=np.count_nonzero(ii_3)

ii_4=(studytime==4)
n_4=np.count_nonzero(ii_4)

notas_1=notas[ii_1]
notas_2=notas[ii_2]
notas_3=notas[ii_3]
notas_4=notas[ii_4]
def acumulativa_tod(notas_1,n_1,notas_2,n_2,notas_3,n_3,notas_4,n_4,nombre):
    plt.figure()
    plt.plot(np.sort(notas_1),np.linspace(1/n_1,1,n_1),label="1, mean={:.2f}".format(np.mean(notas_1)))
    plt.plot(np.sort(notas_2),np.linspace(1/n_2,1,n_2),label="2, mean={:.2f}".format(np.mean(notas_2)))
    plt.plot(np.sort(notas_3),np.linspace(1/n_3,1,n_3),label="3, mean={:.2f}".format(np.mean(notas_3)))
    plt.plot(np.sort(notas_4),np.linspace(1/n_4,1,n_4),label="4, mean={:.2f}".format(np.mean(notas_4)))
    plt.title(nombre)
    plt.xlabel("Calificaciones")
    plt.legend()
    
acumulativa_tod(notas_1, n_1, notas_2, n_2, notas_3, n_3, notas_4, n_4, "Acumulativa para diferentes horas")
def pvalueprom(lista_A,lista_B,nombre):
    n_iteraciones=10000 
    dif_ini=(np.mean(lista_A)-np.mean(lista_B))
    notas=list(lista_A)+list(lista_B)
    n_1=len(lista_A)
    difs=np.zeros(n_iteraciones)
    for i in range(n_iteraciones):
        np.random.shuffle(notas)
        notas_fake_1=notas[:n_1]
        notas_fake_2=notas[n_1:]
        difs[i]=np.mean(notas_fake_1)-np.mean(notas_fake_2)
    p_value=2*(np.count_nonzero(difs<dif_ini)/len(difs))
    
    plt.figure()
    plt.hist(difs,bins=40,density=True)
    plt.vlines(dif_ini,0,1,color="red",label="p_value={:.3f}".format(p_value))
    plt.title(nombre)
    plt.legend()

pvalueprom(notas_1,notas_2, "Diferencia notas 1 y 2")
pvalueprom(notas_2,notas_3,"Diferencia notas 2 y 3")
pvalueprom(notas_2,notas_3,"Diferencia notas 3 y 4")



#Solo horas de estudio + absence<20
ii_1= (studytime==1) &(absences<20)
n_1=np.count_nonzero(ii_1)

ii_2=(studytime==2) &(absences<20)
n_2=np.count_nonzero(ii_2)

ii_3=(studytime==3) &(absences<20)
n_3=np.count_nonzero(ii_3)

ii_4=(studytime==4) &(absences<20)
n_4=np.count_nonzero(ii_4)
notas_1=notas[ii_1]
notas_2=notas[ii_2]
notas_3=notas[ii_3]
notas_4=notas[ii_4]

acumulativa_tod(notas_1, n_1, notas_2, n_2, notas_3, n_3, notas_4, n_4, "Acumulativa para diferentes horas[F._faltas]")
pvalueprom(notas_1,notas_2, "Diferencia notas 1 y 2")
pvalueprom(notas_2,notas_3,"Diferencia notas 2 y 3")
pvalueprom(notas_2,notas_3,"Diferencia notas 3 y 4")

#horas de estudio +absence<20+internet(yes)+freetime>=3

internet=data["internet"]
freetime=data["freetime"]
failures=data["failures"]

ii_1= (studytime==1) &(absences<20)&(internet=="yes")&(freetime>=3)
n_1=np.count_nonzero(ii_1)

ii_2=(studytime==2) &(absences<20)&(internet=="yes")&(freetime>=3)
n_2=np.count_nonzero(ii_2)

ii_3=(studytime==3) &(absences<20)&(internet=="yes")&(freetime>=3)
n_3=np.count_nonzero(ii_3)

ii_4=(studytime==4) &(absences<20)&(internet=="yes")&(freetime>=3)
n_4=np.count_nonzero(ii_4)
notas_1=notas[ii_1]
notas_2=notas[ii_2]
notas_3=notas[ii_3]
notas_4=notas[ii_4]
acumulativa_tod(notas_1, n_1, notas_2, n_2, notas_3, n_3, notas_4, n_4, "Acumulativa para diferentes horas[F._completo]")
pvalueprom(notas_1,notas_2, "Diferencia notas 1 y 2")
pvalueprom(notas_2,notas_3,"Diferencia notas 2 y 3")
pvalueprom(notas_2,notas_3,"Diferencia notas 3 y 4")
