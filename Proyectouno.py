import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


datos1= pd.read_csv("Datosmat.csv",delimiter =";")
notas1=datos1["G3"]*5/20
#Si toman Alcohol
alcohol1=datos1["Walc"]
alcohol2=datos1["Dalc"]
lim_alcoholD=alcohol2>=3
lim_alcoholW=alcohol1>=3
lim_alcohol=lim_alcoholD+lim_alcoholW
que_beben=notas1[lim_alcohol]
que_nobeben=notas1[-(lim_alcohol)]
plt.hist(que_beben, bins=20)
plt.hist(que_nobeben, bins=20)

# Si tiene relaciones romanticas
tienen_relaciones=notas1[(datos1["romantic"]=="yes")]
no_tienen_relaciones=notas1[-(datos1["romantic"]=="yes")]
promedio_relaciones=np.mean(tienen_relaciones)
promedio_norelaciones=np.mean(no_tienen_relaciones)

#Relaciones con la famila 

Relacion_buena=notas1[(datos1["famrel"]>=3)]
Relacion_mala=notas1[-(datos1["famrel"]>=3)]
#No sirve tanto

#Tiempo de viaje
Mas_de_30=notas1[(datos1["traveltime"]>=3)]
Menos_de_30=notas1[-(datos1["traveltime"]>=3)]

#Educacion madres
madre_educacionsup=notas1[(datos1["Medu"]==4)]
madre_sineducacionsup=notas1[-(datos1["Medu"]==4)]
promedio_madrescon=np.mean(madre_educacionsup)
primedio_madressin=np.mean(madre_sineducacionsup)

#Eduacion padres
padre_educacionsup=notas1[(datos1["Fedu"]==4)]
padre_sineducacionsup=notas1[-(datos1["Fedu"]==4)]
promedio_padrescon=np.mean(padre_educacionsup)
promedio_padressin=np.mean(padre_sineducacionsup)


def shuffle(lista_a,lista_b,nombre):
    diferencia=np.mean(lista_a)-np.mean(lista_b)
    N_interracciones=10000
    lista_grande=list(lista_a)+list(lista_b)
    diferencias=np.zeros(N_interracciones)
    for i in range(N_interracciones):
        np.random.shuffle(lista_grande)
        lista_a1=lista_grande[:len(lista_a)]
        lista_b1=lista_grande[len(lista_a):]
        diferencias[i]=np.mean(lista_a1)-np.mean(lista_b1)
    p_value=2*(np.count_nonzero(diferencias>diferencia)/len(diferencias))
    plt.figure()
    plt.title("{} y P_value de {}".format(nombre,p_value))
    plt.hist(diferencias, bins=40, density="true")
    plt.vlines(diferencia,0,4,color="red")
    
    
shuffle(que_nobeben,que_beben,"Beben o no beben alcohol")     
shuffle(no_tienen_relaciones,tienen_relaciones, "Tienen o no relaciones sentimentales") 
shuffle(Relacion_buena,Relacion_mala,"Tiene buena o mala relacion con sus familas" )
shuffle(Menos_de_30,Mas_de_30,"Su tiempo de viaje es mayor o menor a 30 min")
shuffle(madre_educacionsup,madre_sineducacionsup,"Madres que tienen o no educacion superior")
shuffle(padre_educacionsup,padre_sineducacionsup,"Padres que tienen o no educacion superior")
