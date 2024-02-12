# END-TO-END DATA ENGINEERING WITH AZURE: TOKYO OLYMPIC 2021 DATASET

<p align="Left">
  <img src="https://github.com/naqibzainal/DE_ENDTOEND_TOKYOOLYMPICANALYTIC/blob/main/DE%20Azure%20end%20to%20end%20analytic.png" alt="Alt Text" width="700" />
</p>


**PROJECT DESCRIPTION:**

This project provides understanding on how data works by using Microsoft Azure ecosystem and ends it as dasboard insight for analytics purpose by using Tableau.


**MICROSOFT AZURE SERVICES USED:**

**1. Azure Storage Gen2:** Mainly used for storage solution  
**2. Azure Data Factory:** Used to ingest CSV dataset from Github  
**3. Azure DataBricks:** Data Transformation  
**4. Azure Synapse Analytics:** Data analytics (SQL Query)

<p align="left">
  <img width="1411" alt="Services" src="https://github.com/naqibzainal/DE_ENDTOEND_TOKYOOLYMPICANALYTIC/assets/126558710/79b66fd5-b368-4e71-bb80-b8dd6c0ea973">
</p>


**DATA INGESTION USING AZURE DATA FACTORY:**

1. Download Dataset from https://www.kaggle.com/datasets/arjunprasadsarkhel/2021-olympics-in-tokyo/data
2. Upload the dataset to the github.
3. On Azure Data Factory Studio, create a pipeline by selecting "Copy Data" transformation.
4. Then select "HTTP" dataset and linked it with the Github URL.
5. This transformation will then fetch the dataset from Github.
6. Format must be set as "Delimited" as it correspond with the CSV data format.
7. Name all the dataset as required.

<p align="left">
  <img width="1428" alt="Pipeline" src="https://github.com/naqibzainal/DE_ENDTOEND_TOKYOOLYMPICANALYTIC/assets/126558710/2b5fcee0-21e4-4a72-ad6f-62953fbde6c7">
</p>






















