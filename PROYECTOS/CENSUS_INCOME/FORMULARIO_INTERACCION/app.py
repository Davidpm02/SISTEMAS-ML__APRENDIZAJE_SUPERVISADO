"""
En este fichero .py, genero la lógica para realizar predicciones con el modelo final desarrollado.
Como el modelo final hace uso de 4 modelos (2 LightGBM; 1 RandomForestClassifier; 1 regresor logístico), deberemos 
almacenarlos todos en el directorio local del formulario.

En la lógica del formulario, haré uso del ensamblaje de modelos para generar predicciones en base a la información
que el usuario introduce en el formulario.
"""

## IMPORTS -----------

## Metodos Flask
from flask import Flask, request, render_template, redirect, jsonify

import numpy as np
import pandas as pd
import joblib
import random
from sklearn.preprocessing import MinMaxScaler

## SERVER Flask --------

app = Flask(__name__)


## FUNCTIONS ----------

def estructurarMatrizCaract(lista_parametros):
    # Lista de todas las características posibles después de la codificación One-Hot
    matrix_caracts = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss',
                      'hours-per-week', 'workclass_Federal-gov', 'workclass_Local-gov',
                      'workclass_Private', 'workclass_Self-emp-inc',
                      'workclass_Self-emp-not-inc', 'education_10th', 'education_11th',
                      'education_12th', 'education_5th-6th', 'education_7th-8th',
                      'education_9th', 'education_Assoc-acdm', 'education_Assoc-voc',
                      'education_Bachelors', 'education_Doctorate', 'education_HS-grad',
                      'education_Masters', 'education_Prof-school', 'education_Some-college',
                      'marital-status_Divorced', 'marital-status_Married-AF-spouse',
                      'marital-status_Married-civ-spouse', 'marital-status_Never-married',
                      'marital-status_Separated', 'marital-status_Widowed',
                      'occupation_Adm-clerical', 'occupation_Craft-repair',
                      'occupation_Exec-managerial', 'occupation_Farming-fishing',
                      'occupation_Handlers-cleaners', 'occupation_Machine-op-inspct',
                      'occupation_Other-service', 'occupation_Priv-house-serv',
                      'occupation_Prof-specialty', 'occupation_Protective-serv',
                      'occupation_Sales', 'occupation_Transport-moving',
                      'relationship_Husband', 'relationship_Not-in-family',
                      'relationship_Other-relative', 'relationship_Unmarried',
                      'relationship_Wife', 'race_Asian-Pac-Islander', 'race_Black',
                      'race_Other', 'race_White', 'sex_Female', 'native-country_Cambodia',
                      'native-country_China', 'native-country_Columbia',
                      'native-country_England', 'native-country_France',
                      'native-country_Germany', 'native-country_India', 'native-country_Iran',
                      'native-country_Italy', 'native-country_Japan', 'native-country_Laos',
                      'native-country_Mexico', 'native-country_Nicaragua',
                      'native-country_Peru', 'native-country_Philippines',
                      'native-country_Portugal', 'native-country_Puerto-Rico',
                      'native-country_Scotland', 'native-country_Taiwan',
                      'native-country_Thailand', 'native-country_Vietnam']

    # Inicializo todas las características con cero
    caracts_usuario = [0.0] * len(matrix_caracts) 

    # Asigno los valores numéricos directamente desde lista_parametros
    caracts_usuario[0] = float(lista_parametros[0])  # age
    caracts_usuario[1] = float(lista_parametros[1])  # fnlwgt
    caracts_usuario[2] = float(lista_parametros[2])  # education-num
    caracts_usuario[3] = float(lista_parametros[3])  # capital-gain
    caracts_usuario[4] = float(lista_parametros[4])  # capital-loss
    caracts_usuario[5] = float(lista_parametros[5])  # hours-per-week

   
    categorical_features = [
        'workclass', 'education', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'native_country'
    ]
    categorical_values = lista_parametros[6:14]  # Lo ajusto para incluir todas las categóricas

    for feature, value in zip(categorical_features, categorical_values):
        if feature == 'sex':
            if value == 1:  # Ya pre-procesado como 0 o 1
                cat_feature = 'sex_Female'
            else:
                continue  # No hacemos nada si es 0, ya que es el caso base
        else:
            cat_feature = f"{feature}_{value}"

        if cat_feature in matrix_caracts:
            index = matrix_caracts.index(cat_feature)
            caracts_usuario[index] = 1.0

    # Creo un DataFrame con la información del usuario
    # d = {columna: [valor] for columna, valor in zip(matrix_caracts, caracts_usuario)}
    # input_df = pd.DataFrame(data=d)

    
    input_pf_array = np.array(caracts_usuario).reshape(1, -1)

    # Normalizo las características
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(input_pf_array.T)
    X_scaled = np.array(X_scaled).reshape(1, -1)


    return X_scaled
     
def generarPrediccion(input_array):
    
    """Funcion auxiliar que permite actua como ensamblador de los modelos que conforman el modelo final.
       El objetivo fundamental de esta funcion no es otra que la de enviar una determinada entrada a los modelos del ensamblaje 
       encargados de recibirla. Por otro lado, las salidas de estos modelos se envia al meta modelo, cuya salida servira como salida
       o prediccion del ensamblaje.
    
    Keyword arguments:
        input_array -- Matriz de caracteristicas con la informacion del input proporcionado por el usuario en el formulario web.
    Return: 
        model_prediction -- Lista con la estructura (clase_predicha, prediction_proba), generada como salida del ensamblaje de modelos.
    """
    
    # Defino las rutas donde se encuentran los modelos, y los cargo en memoria
    MODEL1_PATH = "src/modelos/ensemble_model_1.joblib"
    MODEL2_PATH = "src/modelos/ensemble_model_2.joblib"
    MODEL3_PATH = "src/modelos/ensemble_model_3.joblib"
    META_MODEL_PATH = "src/modelos/ensemble_meta_model.joblib"
    
    model_1 = joblib.load(MODEL1_PATH)
    model_2 = joblib.load(MODEL2_PATH)
    model_3 = joblib.load(MODEL3_PATH)
    meta_model = joblib.load(META_MODEL_PATH)
    
    
    # Genero las predicciones
    preds_1_test = model_1.predict_proba(input_array)[:, 1]
    preds_2_test = model_2.predict_proba(input_array)[:, 1]
    preds_3_test = model_3.predict_proba(input_array)[:, 1]
    
    X_test_new = np.column_stack((preds_1_test, preds_2_test, preds_3_test))

    # Finalmente, hago las predicciones con el meta-modelo
    prediction = meta_model.predict(X_test_new)
    
    # Probabilidad de la clase predicha
    #prediction_proba = meta_model.predict_proba(X_test_new)[::,1]
    model_prediction = [prediction.item()]

    return model_prediction


## ROUTES ---------

@app.route("/")
def index():
    
    """Ruta principal del servidor generado por Flask."""
    
    # No hace nada, solo retorna el HTML del formulario
    return render_template("formulario.html")


#################################################################################

@app.route("/output_predict", methods=['POST'])
def output_predict():
    """
    Ruta a la que se envía el formulario una vez que este ha sido enviado.
    La función de la ruta recoge todos los parámetros de la información proporcionada en el formulario web, y es utilizada
    para generar la matriz de características que se envía al modelo para calcular la predicción.
    """

    if request.method == 'POST':
        # Accedo a los datos enviados por el formulario
        datos_formulario = request.form


        form_answers = [
            datos_formulario.get('age', type=int),
            random.randint(50000, 300000),  # Valores generados aleatoriamente para fnlwgt (esta variable es necesaria, y el usuario no tiene porque saber su valor)
            datos_formulario.get('education_num', type=int),
            datos_formulario.get('capital_gain', type=int),
            datos_formulario.get('capital_loss', type=int),
            datos_formulario.get('hours_per_week', type=int),
            datos_formulario.get('workclass', ''),
            datos_formulario.get('education', ''),
            datos_formulario.get('marital_status', ''),
            datos_formulario.get('occupation', ''),
            datos_formulario.get('relationship', ''),
            datos_formulario.get('race', ''),
            1 if datos_formulario.get('sex', '') == 'Female' else 0,  # Convierte el sexo a 1 si es Femenino, de lo contrario a 0
            datos_formulario.get('native_country', '')
        ]

        # Genero la matriz de características
        X_scaled = estructurarMatrizCaract(form_answers)
        model_prediction = generarPrediccion(X_scaled)
    
        if model_prediction == 0:
            respuesta = ">$50K"
        else:
            respuesta = "<=$50K"
    
        return jsonify(message = respuesta)



if __name__ == "__main__":
    
    app.run(debug=True)
    