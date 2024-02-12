# END-TO-END DATA ENGINEERING WITH AZURE: TOKYO OLYMPIC 2021 DATASET

<p align="Left">
  <img src="https://github.com/naqibzainal/DE_ENDTOEND_TOKYOOLYMPICANALYTIC/blob/main/DE%20Azure%20end%20to%20end%20analytic.png" alt="Alt Text" width="700" />
</p>


**PROJECT DESCRIPTION:**
-----------------------------------------------------------
This project provides understanding on how data works by using Microsoft Azure ecosystem and ends it as dasboard insight for analytics purpose by using Tableau.


**MICROSOFT AZURE SERVICES USED:**
-----------------------------------------------------------
**1. Azure Storage Gen2:** Mainly used for storage solution  
**2. Azure Data Factory:** Used to ingest CSV dataset from Github  
**3. Azure DataBricks:** Data Transformation  
**4. Azure Synapse Analytics:** Data analytics (SQL Query)

<p align="left">
  <img width="1411" alt="Services" src="https://github.com/naqibzainal/DE_ENDTOEND_TOKYOOLYMPICANALYTIC/assets/126558710/79b66fd5-b368-4e71-bb80-b8dd6c0ea973">
</p>


**DATA INGESTION USING AZURE DATA FACTORY:**
-----------------------------------------------------------
1. Download Dataset from https://www.kaggle.com/datasets/arjunprasadsarkhel/2021-olympics-in-tokyo/data
2. Upload the dataset to the github.
3. Create a container for raw dataset and transformed dataset.
4. Raw container is mainly for the dataset pulled from Github.
5. Tranformed container is for cleaned dataset by using Pyspark later.
6. On Azure Data Factory Studio, create a pipeline by selecting "Copy Data" transformation.
7. Then select "HTTP" dataset and linked it with the Github URL.
8. This transformation will then fetch the dataset from Github.
9. Format must be set as "Delimited" as it correspond with the CSV data format.
10. Name all the dataset as required and repeat for the rest of the dataset.

<p align="left">
  <img width="1428" alt="Pipeline" src="https://github.com/naqibzainal/DE_ENDTOEND_TOKYOOLYMPICANALYTIC/assets/126558710/2b5fcee0-21e4-4a72-ad6f-62953fbde6c7">
</p>


**DATA TRANSFORMATION USING AZURE DATABRICKS:**
-----------------------------------------------------------
1. Setting up notebook within Databricks.
2. Mount ADLS Gen2 to Databricks.
3. Creating an App Registration and get the Client ID and Tenant ID. This will be use in the Pyspark code.
4. Generate and secured the Secret Key under "Certificates & Secrets".
5. Mount ADLS Gen2 with the (SecretKey, Client ID, Tenant iD) generated.
6. The process is to Seamlessly connect the bridge between Databricks and ADLS, allowing the connection of Data Access.
7. Tranform data by using Pyspark. Refer: https://github.com/naqibzainal/DE_ENDTOEND_TOKYOOLYMPICANALYTIC/blob/main/Tokyo%20Olympic%20Transformation.ipynb

<p align="left">
  <img width="1422" alt="Datasets pyspark" src="https://github.com/naqibzainal/DE_ENDTOEND_TOKYOOLYMPICANALYTIC/assets/126558710/3d474895-52af-4ec0-b755-6bfa0910e706">
</p>


**DATA ANALYTICS USING AZURE SYNAPSE ANALYTICS:**
-----------------------------------------------------------






















