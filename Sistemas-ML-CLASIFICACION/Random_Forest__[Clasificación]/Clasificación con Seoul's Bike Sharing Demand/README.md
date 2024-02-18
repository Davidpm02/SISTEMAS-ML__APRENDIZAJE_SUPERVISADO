# Descripcion del proyecto

En el directorio actual se describe un ejercicio de regresion lineal multivariable, haciendo uso de bosques aleatorios.
El proyecto esta dividido en un conjunto de notebooks de Jupyter, que permiten dividir y centralizar la carga de trabajo con respecto al analisis, visualizacion y procesamiento de los datos de los que se dispone para desarrollar y entrenar el modelo.

En concreto, el conjunto de datos a utilizar se encuentra en el directorio 'dataset', y ha sido obtenido a traves de una publicacion de la plataforma DataCamp (https://archive.ics.uci.edu/dataset/560/seoul+bike+sharing+demand). Este se compone de 8760 ejemplos, de los cuales se han recogido 14 caracteristicas diferentes. Es un dataset de tamanio mediano, por lo que, en principio, no deberiamos de tener problemas en el entrenamiento del modelo a desarrollar.

El objetivo principal del mini 'proyecto' consiste en ser capaz de representar de forma clara las diferentes relaciones existentes entre las distintas categorias (entre si, y con respecto a nuuestra etiqueta), y finalmente, desarrollar un modelo util, que pudiesemos implementar en la vida real.


## Informacion sobre el conjunto de datos.

Como he dicho, el conjunto de de datos esta compuesto por 14 columnas:

Date.

Rented Bike Count.

Hour.

Temperature (C).

Humidity(%).

Wind speed(m/s).

Visibility(10m).

Dew point temperature(C)

Solar Radiation (MJ/m2)

Rainfall(mm).

Snowfall(cm).

Seasons.

Holiday.

Functioning Day.



## Procesamiento de datos

## Visualizacion de datos

## Creacion y entrenamiento de modelos

## Explicacion resultados

Si se ha revisado el notebook de desarrollo de los modelos (desarrollo_modelos_clasificacion.ipynb), podremos ver como hemos obtenido un rendimiento buenisimo en los modelos entrenados a partir de los conjuntos de datos en los que no se ha tenido en cuenta los coeficientes de correlacion entre la variable dependiente con el resto de variables, por lo que todas las variables del dataset han actuado como predictoras, obtenido un coeficiente de F1-Score de 1.0 para cada una de las clases posibles de la variable dependiente.

Sin embargo, esto no ha sido asi al entrenar el modelo clasificador con el conjunto de datos al cual se le han asignado manualmente las variables que actuan como predictoras. En este caso, el coeficiente de Exactitud general del modelo es de 0.97, pero si se aprecia el coeficiente de F1-Score para las dos clases posibles de la variable dependiente, se muestra como el modelo tiene una capacidad bastante limitada de clasificar correctamente los ejemplos de dias en los que nuestra variable dependiente toma el valor de 1 (F1-Score para la clase 1 ==> 0.47; F1-Score para la clase 0 ==> 0.99).

***¿A qué se debe esto?***

El conjunto de datos para el que se han elegido manualmente las variables predictoras, solo ha tenido en cuenta variables en las que el coeficiente de correlación era >0. Podemos ver como esto, en la práctica, no es la mejor decisión, pues aunque negativo, el coeficiente de correlacion sigue indicando una relacion entre ambas variables, por lo que al eliminar estas caracteristicas, el modelo pierde informacion (se puede ver en los resultados obtenidos).

Al momento de escoger las variables predictoras de nuestro modelo, se deberian excluir aquellas que el coeficiente tenga un valor de 0, o muy cercano a este, y hacer pruebas para comprobar el resultado de un entrenamiento con y sin estas variables (puesto que, al tener un coeficiente de correlacion igual a 0, se indica que no mantiene ninguna relacion lineal con nuestra variable dependiente).

***¿Relación lineal entre variables?***

Hacer nuestras elecciones de variables dependientes basándonos en el coeficiente de correlación de Pearson, es muy bueno al momento de trabajar con algoritmos basados en relaciones lineales. Si bien podriamos trabajar con un algoritmo más complejo, modelar nuestro dataset basándonos nuevamente en los coeficientes de correlación, y obtener unos resultados positivos, no es siempre la mejor práctica posible. Muchos algoritmos de Machine Learning tienen en cuenta relaciones más complejas entre las variables de nuestro dataset (no necesariamente lineales), y basarnos en la correlación de Pearson para modelar nuestro dataset puede no ser suficiente, o incluso confundir a nuestro modelo final.

Por otro lado, es posible aplicar regularización de LASSO en nuestros entrenamiento, para tratar de penalizar al modelo al momento de hacer predicciones. Esta regularización es capaz de igual a 0 los coeficientes de variables que no aporten información al modelo, por lo que hace una "elección automática" de las variables predictoras. En los entrenamientos vistos en el notebook de este proyecto no se ha aplicado regularización en las funciones de pérdida de los entrenamientos, y aún así, hemos obtenido buenos resultados para el conjunto de datos completo. A pesar de ello, aplicar regularización es un procedimiento importantísimo en la mayoría de desarrollos que hagamos.