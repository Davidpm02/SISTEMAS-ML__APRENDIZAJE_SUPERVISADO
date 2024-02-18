# CardioCheck

CardioCheck es un proyecto de Machine Learning diseñado para predecir la presencia o ausencia de enfermedades cardiovasculares en pacientes basándose en una combinación de características objetivas, resultados de exámenes médicos y datos subjetivos proporcionados por los pacientes.

Para el desarrollo del proyecto, se ha tomado prestado un conjunto de datos publicado en Kaggle, por parte del usuario ***Svetlana Ulianova*** (https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset).


---

## Modelos Desarrollados

En el desarrollo de este proyecto, se implementaron y evaluaron cuatro modelos diferentes de Machine Learning, utilizando las siguientes técnicas:

### 1. K-Nearest Neighbors (KNN)

El modelo KNN ha sido utilizado para clasificar los casos basándose en las características más cercanas en el espacio de características.

- [CardioCheck_K-NN](../../Sistemas-ML-CLASIFICACION/K-Nearest_Neighbors__[Clasificación]/CardioCheck_K-NN)

### 2. Logistic Regression

Este modelo aplica la regresión logística para predecir la probabilidad de ocurrencia de enfermedad cardiovascular.

- [CardioCheck_LogisticRegression](/ruta/al/proyecto/LogisticRegression)

### 3. Multi-Layer Perceptron (MLPClassifier)

Se ha implementado un perceptrón multicapa para modelar la complejidad de las relaciones entre las características y la presencia de enfermedades cardiovasculares.

- [CardioCheck_MLPClassifier](/ruta/al/proyecto/MLPClassifier)

### 4. Support Vector Machine (SVM)

El modelo SVM se utilizó para encontrar el hiperplano que mejor divide los casos de enfermedades cardiovasculares de los no casos.

- [CardioCheck_SVM](/ruta/al/proyecto/SVM)





## Descripción del Dataset

El dataset utilizado en CardioCheck consta de varios tipos de características:

* **Características Objetivas**: Información factual sobre el paciente.
    
* **Examen Médico**: Resultados obtenidos de exámenes médicos.

* **Características Subjetivas**: Información proporcionada directamente por el paciente.


### Características

* **Edad**: En días.

* **Altura**: En centímetros.

* **Peso**: En kilogramos.

* **Género**: Código categórico (1 ==> Hombre;  2 ==> Mujer).

* **Presión sanguínea sistólica**.

* **Presión sanguínea diastólica**.

* **Colesterol**: 1- normal, 2- por encima de lo normal, 3- muy por encima de lo normal.

* **Glucosa**: 1- normal, 2- por encima de lo normal, 3- muy por encima de lo normal.

* **Fumador**: Binario.

* **Consumo de alcohol**: Binario.

* **Actividad física**: Binario.

* **Presencia o ausencia de enfermedad cardiovascular**: Binario (variable objetivo).

Todos los valores del dataset fueron recopilados en el momento del examen médico.


---

## Contribuir

Si deseas contribuir al proyecto CardioCheck, por favor, sientete libre de contactar conmigo para proporcionar cualquier aporte.


---

## Contacto

Si tienes alguna pregunta o deseas discutir sobre el proyecto, no dudes en contactar.
