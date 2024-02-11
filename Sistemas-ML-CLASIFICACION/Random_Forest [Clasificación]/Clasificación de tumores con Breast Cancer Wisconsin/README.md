# Introduccion

El proyecto actual tratara sobre la representacion y analisis de un conjunto de datos que utilizare para desarrollar un modelo que me ayude  a clasificar, basandome en informacion de diferentes aspectos de 
una celula animal, o un conjunto de ellas, si el tumor desarrollado es beningo o maligno.

El conjunto de datos a utilizar recoje informacion de 569 ejemplos diferentes, que utilizare para el desarrollo del modelo.

Los valores de cada caracteristica del dataset viene representada en valores de


## Sobre el conjunto de datos

Las características se calculan a partir de una imagen digitalizada de un aspirado con aguja fina (AAF) de una masa mamaria. Describen características de los núcleos celulares presentes en la imagen.
El espacio tridimensional es el descrito en: [K. P. Bennett y O. L. Mangasarian: "Robust Linear Programming Discrimination of Two Linearly Inseparable Sets", Optimization Methods and Software 1, 1992, 23-34].

Esta base de datos también está disponible a través del servidor ftp de UW CS:
ftp ftp.cs.wisc.edu
cd math-prog/cpo-dataset/machine-learn/WDBC/

También se puede encontrar en UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29

Información sobre atributos:

1) Número de identificación.

2) Diagnóstico (M = maligno, B = benigno)
3-32)

Se calculan diez características de valor real para cada núcleo celular:

a) Radio (media de las distancias del centro a los puntos del perímetro)
b) Textura (desviación estándar de los valores en escala de grises)
c) Perímetro
d) Area
e) Suavidad (variación local de las longitudes de los radios)
f) Compacidad (perímetro^2 / área - 1,0)
g) Concavidad (gravedad de las partes cóncavas del contorno)
h) Puntos cóncavos (número de porciones cóncavas del contorno)
i) Simetría
j) Dimensión fractal ("aproximación de la línea de costa" - 1)

Se calcularon la media, el error estándar y el "peor" o mayor (media de los tres
(media de los tres valores más grandes) de estas características,
resultando 30 características. Por ejemplo, el campo 3 es el radio medio, el campo
13 es el Radio SE, el campo 23 es el Peor Radio.

Todos los valores de las características se recodifican con cuatro dígitos significativos.

El conjunto de datos NO cuenta con valores nulos.

Distribución por clases: **357 benignas**, **212 malignas**.