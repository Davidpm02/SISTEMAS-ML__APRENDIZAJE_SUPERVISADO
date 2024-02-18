# Hotel Booking Demand

## Introduccion

El conjunto de datos que utilizo en este proyecto consta de datos de reservas de un hotel urbano y un hotel turístico. Incluye muchos detalles sobre las reservas, incluidas las especificaciones de la habitación, la duración de la estancia, el tiempo entre la reserva y la estancia, si la reserva se canceló y cómo se realizó la reserva. Los datos se recopilaron entre julio de 2015 y agosto de 2017.

El conjunto de datos lo he obtenido del portal web ***ScienceDirect***, y puedes acceder a el a partir del siguiente enlace: https://www.sciencedirect.com/science/article/pii/S2352340918315191 .

---

## Modelos Desarrollados

Para este proyecto, se han desarrollado tres modelos de clasificación diferentes, utilizando técnicas de Machine Learning avanzadas:

### 1. Decision Tree (Árbol de Decisión)

Este modelo utiliza un árbol de decisión para predecir la cancelación de reservas, basándose en la estructura de árbol para la toma de decisiones.

- [Hotel Booking Demand_DecisionTreeClassifier](../../Sistemas-ML-CLASIFICACION/Decision_Tree__[Clasificación]/HotelBookingDemand_DecisionTreeClassifier)

### 2. Random Forest (Bosque Aleatorio)

El modelo de Random Forest mejora la predicción utilizando múltiples árboles de decisión para reducir el riesgo de sobreajuste.

- [Hotel Booking Demand_RandomForestClassifier](../../Sistemas-ML-CLASIFICACION/Random_Forest__[Clasificación]/HotelBookingDemand_RandomForestClassifier)

### 3. Multi-Layer Perceptron (MLPClassifier)

Se implementó un modelo de perceptrón multicapa (MLPClassifier) para capturar las complejidades de las relaciones entre las características mediante una red neuronal.

- [Hotel Booking Demand_MLPClassifier](/ruta/al/proyecto/MLPClassifier)


## Conjunto de datos



El conjunto de datos esta contenido en un fichero .csv, el cual consta de 119210 ejemplos, de los cuales, se recogen un total de 53 caracteristicas.

### Caracteristicas

* **is_canceled**	Variable binaria que indica si una reserva fue cancelada.

* **lead time**	Número de días entre la fecha de reserva y la fecha de llegada.

* **arrival_date_week_number**, **arrival_date_day_of_month**, **arrival_date_month**	Número de semana, fecha del día y número del mes de la fecha de llegada.

* **stays_in_weekend_nights**, **stays_in_week_nights**	Número de noches de fin de semana (sábado y domingo) y noches entre semana (de lunes a viernes) que reservó el cliente.

* **adults**, **children**, **babies**	Número de adultos, niños y bebés reservados para la estancia.

* **is_repeated_guest**	Variable binaria que indica si el cliente era un huésped habitual.

* **previous_cancellations**	Número de reservas anteriores que fueron canceladas por el cliente.

* **previous_bookings_not_canceled**	Número de reservas anteriores que no fueron canceladas por el cliente.

* **required_car_parking_spaces**	Número de plazas de aparcamiento solicitadas por el cliente.

* **total_of_special_requests**	Número de solicitudes especiales realizadas por el cliente.

* **avg_daily_rate**	Tarifa diaria promedio, definida dividiendo la suma de todas las transacciones de alojamiento por el número total de noches de estadía.

* **booked_by_company**	Variable binaria que indica si una empresa realizó la reserva.

* **booked_by_agent**	Variable binaria que indica si un agente realizó la reserva.

* **hotel_City**	Variable binaria que indica si el hotel reservado es un "Hotel de ciudad".

* **hotel_Resort**	Variable binaria que indica si el hotel reservado es un "Hotel Resort".

* **meal_BB**	Variable binaria que indica si se reservó una comida en régimen de alojamiento y desayuno.

* **meal_HB**	Variable binaria que indica si se ha reservado media pensión.

* **meal_FB**	Variable binaria que indica si se reservó una comida en pensión completa.

* **meal_No_meal**	Variable binaria que indica si no se había reservado ningún paquete de comida.

* **market_segment_Aviation**, **market_segment_Complementary**, **market_segment_Corporate**, **market_segment_Direct**, **market_segment_Groups**, **market_segment_Offline_TA_TO**, **market_segment_Online_TA**, **market_segment_Undefined**	Indica la designación del segmento de mercado con un valor de 1. "TA"= agente de viajes, "TO"= operadores turísticos.

* **distribution_channel_Corporate**, **distribution_channel_Direct**, **distribution_channel_GDS**, **distribution_channel_TA_TO**, **distribution_channel_Undefined**	Indica el canal de distribución de reservas con un valor de 1. "TA"= agente de viajes, "TO"= operadores turísticos, "GDS" = Sistema de Distribución Global.

* **reserved_room_type_A**, **reserved_room_type_B**, **reserved_room_type_C**, **reserved_room_type_D**, **reserved_room_type_E**, **reserved_room_type_F**, **reserved_room_type_G**, **reserved_room_type_H**, **reserved_room_type_L**  Indica código de tipo de habitación reservada con un valor de 1. Se presenta el código en lugar de la designación por motivos de anonimato.

* **deposit_type_No_Deposit**	Variable binaria que indica si se realizó un depósito.

* **deposit_type_Non_Refund**	Variable binaria que indica si se realizó un depósito por el valor del costo total de la estadía.

* **deposit_type_Refundable**	Variable binaria que indica si se realizó un depósito con un valor inferior al costo total de la estadía.

* **customer_type_Contract**	Variable binaria que indica si la reserva tiene asociada una asignación u otro tipo de contrato.

* **customer_type_Group**	Variable binaria que indica si la reserva está asociada a un grupo.

* **customer_type_Transient**	Variable binaria que indica si la reserva no forma parte de un grupo o contrato y no está asociada a otra reserva transitoria.

* **customer_type_Transient-Party**	Variable binaria que indica si la reserva es transitoria, pero está asociada al menos a otra reserva transitoria.


---

## Contexto

Una cadena de hoteles acaba de contratarte como analista de datos. Han notado que la tasa de cancelación ha aumentado en los últimos años. Esto a menudo lleva a que las habitaciones no se alquilen durante varios días seguidos.

La dirección del hotel está interesada en desarrollar un modelo para predecir la probabilidad de que un cliente cancele su reserva. Si tiene éxito, esto podría utilizarse para optimizar su servicio de reservas y anticipar cuándo se producirán cancelaciones.

Deberá preparar un informe que sea accesible a una audiencia amplia. Debe describir su motivación, pasos, hallazgos y conclusiones.

---

## Herramientas y Tecnologías Utilizadas

**Python**: Lenguaje de programación principal para el desarrollo del proyecto.

**Scikit-Learn (sklearn)**: Biblioteca de Python para Machine Learning que proporciona herramientas simples y eficientes para el análisis de datos y modelado. Se utilizará para cargar el dataset 'digits', así como para la implementación y evaluación de modelos de clasificación.

**Jupyter Notebook**: Ambiente interactivo que permite la creación de notebooks que contienen código, visualizaciones y texto explicativo, facilitando así la documentación y compartición del análisis y resultados.

## Contribuir

Se invita a contribuir al proyecto mediante la sugerencia de mejoras en el código, la implementación de nuevos modelos de clasificación o la mejora de los procesos de evaluación y optimización. Para contribuir, por favor, crea un pull request con tus propuestas.

