# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 12:09:03 2022

@author: jimen
"""
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model
import sklearn.model_selection
datos= pd.read_csv("Datos.csv")
tiempo=np.array(datos["time_study"])
notas=np.array(datos ["Marks"])*(5/60)
cursos= np.array(list(datos["number_courses"]))
lim_media=cursos <=3
lim_extra= 6< cursos
lim_normal4= cursos==4
lim_normal5= cursos==5
lim_normal6= cursos==6
tiempo_de_media=tiempo[lim_media]
tiempo_normal=np.array(list(tiempo[lim_normal4])+list(tiempo[lim_normal5])+list(tiempo[lim_normal6]))
tiempo_extra=tiempo[lim_extra]
notas_media=notas[lim_media]
notas_normal=np.array(list(notas[lim_normal4])+list(notas[lim_normal5])+list(notas[lim_normal6]))
notas_extra=notas[lim_extra]

def p_value(lista_a,lista_b,nombre):
    n_interacciones=10000
    diferencia_real=(np.mean(lista_b)-np.mean(lista_a))
    diferencia=np.zeros(n_interacciones)
    notas=(list(lista_a)+list(lista_b))
    for i in range(n_interacciones):
        np.random.shuffle(notas)
        notas_a=notas[:len(lista_a)]
        notas_b=notas[len(lista_a):]
        diferencia[i]=(np.mean((notas_b))-np.mean(notas_a))
    diferencia_p=2*(np.count_nonzero(diferencia>diferencia_real)/len(diferencia))
    nombre_final=str(nombre)+" con P_value de "+ str(diferencia_p)
    plt.figure()
    plt.title(str(nombre_final))
    plt.hist(diferencia, bins=40, density="true")   
    plt.vlines(diferencia_real,0,1.3,color="red")
def Regresion(x,y,nombre):
    regresion= sklearn.linear_model.LinearRegression()
    x_entrenar, x_prueba, y_entrenar, y_prueba= sklearn.model_selection.train_test_split(x.reshape(-1,1),y,test_size=0.5)
    regresion.fit(x_entrenar,y_entrenar)
    prediccion=regresion.predict(x.reshape(-1,1))
    pendiente=regresion.coef_
    intercepto=regresion.intercept_
    nombrefinal= nombre+" con pendiente "+ str(round(pendiente[0],4)) +" y intercepto " + str(round(intercepto,4))  +"\n" +"Y con R igual a " + str((regresion.score(x_prueba,y_prueba)))
    plt.figure()
    plt.title(nombrefinal)
    plt.ylabel("Notas")
    plt.xlabel("Tiempo de estudio")
    plt.scatter(x.reshape(-1,1),prediccion, label="Prediccion")
    plt.scatter(x,y, label="Real")
    plt.legend()
         
#p_value(notas_media,notas_extra,"Media Matricula y Extracreditados")
#p_value(notas_media,notas_normal,"Media Matricula y Matricula Normal")
#p_value(notas_normal,notas_extra,"Matricula Normal y Extracreditados" )
Regresion(tiempo_de_media,notas_media, "Media Matricula")
Regresion(tiempo_normal,notas_normal, "Matricula Normal")
Regresion(tiempo_extra,notas_extra, "Extreditados")
#plt.scatter(tiempo_de_media,notas_media)
#plt.scatter(tiempo_normal,notas_normal)
#plt.scatter(tiempo_extra,notas_extra)
