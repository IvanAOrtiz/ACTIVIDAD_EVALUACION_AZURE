SQL Regression Model Deployment - Azure
Este proyecto demuestra un flujo completo de Machine Learning utilizando una base de datos en la nube, desde la conexión y limpieza de datos hasta el entrenamiento, empaquetado y despliegue de un modelo de regresión en Azure.
Objetivo
Predecir la columna ModifiedDate de la tabla SalesLT.Customer de una base de datos SQL utilizando un modelo de regresión entrenado con variables seleccionadas tras un preprocesamiento exhaustivo.
1. Montar base de datos en SQL
Se creó un servidor de base de datos SQL en Azure.
Se utilizó la base de datos de prueba que incluye la tabla SalesLT.Customer.
2. Preprocesamiento de datos
Se eliminaron columnas irrelevantes o con poca información:
* "Suffix", "rowguid", "NameStyle", "CustomerID", 
*  "Title", "FirstName", "MiddleName", 
*  "LastName", "EmailAddress"
Se revisaron los value_counts para identificar y eliminar columnas sin información útil.
Se extrajo el código de área del número telefónico (Phone).
La fecha ModifiedDate se transformó a valor numérico utilizando timestamp.
Se aplicó One Hot Encoding a las variables categóricas:
CompanyName
SalesPerson
3. Entrenamiento del modelo
Se utilizó un modelo de regresión (por ejemplo, LinearRegression) para predecir ModifiedDate.
Variables predictoras:
CompanyName (one-hot)
SalesPerson (one-hot)
Phone (con código de área extraído)
El modelo fue entrenado y probado localmente.
Se evaluó el modelo con 4 filas aleatorias de x_test mediante model.predict().
4. Despliegue del modelo
El modelo entrenado fue empaquetado y desplegado como un servicio en Azure.
Se desarrolló una API para consumir el modelo desde la nube y realizar predicciones en tiempo real.

