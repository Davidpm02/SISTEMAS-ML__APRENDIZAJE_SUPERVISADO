# Introduccion

El 'wine_dataset' es otro de los conjuntos de datos 'toy' que ofrece SkLearn dentro de su Framework, con el que poder experimentar el procesamiento de datos, y el desarrollo y entrenamiento de modelos.
En el caso dl conjunto 'wine_dataset', esta enfocado al desarrollo de un modelo de clasificacion, por lo que, en este caso, hare uso de un modelo KNN para clasificar los ejemplos en los diferentes
posibles valores que admita la etiqueta del conjunto de datos.

Este dataset se encuentra dentro de sklearn.datasets, y he creado un notebook en el que lo analizo a fondo.


## Descripcion del conjunto de datos

#### Origen de la Información

El conjunto de datos load_wine procede del resultado de un análisis químico de vinos cultivados en la misma región de Italia pero derivados de tres diferentes cultivares. La análisis determinó las cantidades de 13 componentes encontrados en cada uno de los tres tipos de vinos.

#### Nombres de las Columnas y Representación

El conjunto de datos load_wine incluye 13 características (columnas) que representan diferentes medidas químicas. Estas características son:

**Alcohol**: la cantidad de alcohol presente en el vino.

**Ácido málico**: un ácido orgánico presente en los vinos.

**Cenizas**: residuo no orgánico que queda después de la evaporación y pirólisis.

**Alcalinidad de las cenizas**: una medida de la basicidad de las cenizas.

**Magnesio**: cantidad de magnesio en el vino.

**Fenoles totales**: compuestos que afectan el sabor y el color del vino.

**Flavonoides**: un tipo de fenol, asociados con propiedades antioxidantes.

**Fenoles no flavonoides**: fenoles que no son flavonoides.

**Proantocianidinas**: otro tipo de antioxidante.

**Intensidad del color**: medida de la intensidad del color del vino.

**Hue**: el matiz o tonalidad del color del vino.

**OD280/OD315 de vinos diluidos**: una medida de la cantidad de proteínas en el vino.

**Prolina**: un aminoácido importante en la composición del vino.


#### Objetivo del Dataset

El objetivo principal de este conjunto de datos es clasificar los vinos en una de las tres categorías posibles, correspondientes a los tres cultivares de origen. Esto lo hace un conjunto de datos ideal para tareas de clasificación multiclase.


## Información Adicional

El conjunto de datos contiene un total de 178 muestras de vino.
La variable objetivo (target) es un factor que indica el cultivar al cual pertenece cada muestra de vino, representado como clases 0, 1, y 2.
Este conjunto de datos es especialmente útil para practicar técnicas de clasificación y análisis exploratorio de datos en el campo del Machine Learning, dada su relativa simplicidad y el hecho de que incluye múltiples características con relaciones interesantes para explorar.