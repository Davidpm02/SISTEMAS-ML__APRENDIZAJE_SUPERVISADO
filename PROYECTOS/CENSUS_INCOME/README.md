# Prediccion de Ingresos "Census Income"

## Descripción

Este proyecto se centra en el uso del dataset "adult" de OpenML, también conocido como "Census Income" dataset. El objetivo es aplicar técnicas de clasificación, dentro del Aprendizaje Supervisado, para predecir si el ingreso de una persona supera los 50K dólares al año, basándose en una serie de atributos sociodemográficos y de empleo.

---

## Dataset

El dataset "adult" contiene datos del censo de EE.UU., enfocándose en características relacionadas con el empleo y aspectos sociodemográficos. La meta es predecir si el ingreso de una persona excede los $50K/año a partir de estas variables.

### Características del Dataset

A continuación, se presentan las variables (con sus nombres originales) y sus descripciones:

* **age**: La edad del individuo.
* **workclass**: El tipo de empleador para el cual trabaja el individuo (por ejemplo, Private, Self-emp-not-inc, State-gov).
* **fnlwgt (Final Weight)**: Una ponderación asignada por el censo, reflejando la cantidad de personas que la observación representa.
* **education**: El nivel máximo de educación alcanzado (por ejemplo, Bachelors, Some-college, 11th).
* **education-num**: Número que representa el nivel educativo (código numérico equivalente a "education").
* **marital-status**: El estado civil del individuo (por ejemplo, Married-civ-spouse, Divorced).
* **occupation**: La ocupación del individuo (por ejemplo, Tech-support, Craft-repair, Other-service).
* **relationship**: Describe la relación del individuo con su familia (por ejemplo, Wife, Own-child, Not-in-family).
* **race**: La raza del individuo (por ejemplo, White, Asian-Pac-Islander, Amer-Indian-Eskimo).
* **sex**: El género del individuo (Male, Female).
* **capital-gain**: Ingresos de fuentes de inversión fuera del trabajo regular.
* **capital-loss**: Pérdidas de fuentes de inversión fuera del trabajo regular.
* **hours-per-week**: El número de horas que el individuo trabaja por semana.
* **native-country**: El país de origen del individuo.

### Variable Objetivo

* ***class (income)***: Si el ingreso anual del individuo es mayor a $50K/año o no (">50K", "<=50K").

### Tamaño del dataset

Actualmente, la version 4 publicada en OpenML (que es la que voy a utilizar) cuenta con un total de 48842 ejemplos registrados (en torno a un 35-40% mas cantidad de ejemplos que en su version inicial).

Esta cantidad de ejemplos permite entrenar el modelo comodamente, pues, para nuestro caso de uso, contamos con una cantidad de registros mas que suficiente.

---

### Contacto

Si tienes preguntas, sugerencias o te gustaría contribuir al proyecto, me encantaría escuchar tus ideas. Puedes contactar conmigo a traves de las siguientes maneras:

***Correo Electrónico***: padishdev@duck.com

***GitHub***: Si encuentras algun problema, o ves conveniente aplicar alguna modificacion, no dudes en abrir un issue. También puedes contribuir directamente mediante pull requests.

***LinkedIn***: https://www.linkedin.com/in/david-padilla-mu%C3%B1oz-52126725a/

