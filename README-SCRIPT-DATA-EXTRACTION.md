# Nombre del componente
**getDataPlanBackendNewFront
## Descripción proyecto
Script que realiza la extracción, transformación y cargue de la data del historico KPI. 
Estado del proyecto: Productivo, Version 1.0.0.

## Entradas y Salidas
El estado actual del script para su ejecución es a través de un cronjob en el kernel linux ubuntu 20.04, sin embargo es posible ejecutarlo a través del terminal con el siguiente comando 
en la terminal de un bash shell:

Eje : /usr/bin/python3.8 /home/sebastian/Documentos/BBVA/PROPUESTA\ KPI\ VISUAL/GetDataPlanBackendNewFront/dailyJsonFileProcess.py 
"cp ./dataKPIGeneralProd.json /home/sebastian/Documentos/BBVA/PROPUESTA\ KPI\ VISUAL/DashboardBBVA/src && cd /home/sebastian/Documentos/BBVA/PROPUESTA\ KPI\ VISUAL/DashboardBBVA && ng build --configuration production --output-path docs --base-href /lraKpiTest/ && git add . && git commit -m 'KPI Updated' && git push origin gh-pages"

## Lógica
Descripción de cada paso del proceso.

 1. El componente consulta toda la data existente del año anterior hastla la fecha actual.
 2. Posteriormente realiza la transformación de los datos recuperados por la consulta en objetos.
 3. Procede a convertir todos los datos en un formato JSON.
 4. Genera un archivo de salida con todos lo datos contenidos en un fichero con nombre dataKPIGeneralProd.json
 5. Se ejecuta un proceso en bash shell para mover este fichero a la ruta absoluta donde habita el proyecto y código fuente del proyecto Front escrito en angular, para confirmar el cambio del archivo y cargarlo en gitHub con comandos reservados de git.
 6. En ultima instancia lanza la solicitud al server de backend de notificación informando en el apartado frontal y también dispositivos moviles la mensajeria push.

```
$ {"field":"value"}
```

## Despliegue

Tecnologias utilizadas (JSON Library, Request Library, mysql connector, Python) Para mayor información de dependencias consultar requirements.txt

Conexión a base de datos Planbackend actual del equipo.

Host Actual : devosfernando.com

Port: 9999

## Pruebas

No se ha realizado un circuito formal de pruebas para este script, se tiene funcionando en producción como proceso de misión critica.


## Requisitos del entorno de desarrollo para ejecución

Python 3.8 en adelante, IDE Intellij Idea, WebStorm, VIsual studio code (recomendado) etc..
Sistema operativo Windows 10 o superior, linux ubuntu 20.04

|Autor  | Descripción | Fecha |
|Sebastian Torres Encizo|Linea Base inicial|24/04/2024|


