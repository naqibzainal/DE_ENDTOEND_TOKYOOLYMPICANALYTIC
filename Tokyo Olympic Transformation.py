# Databricks notebook source
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType, DoubleType, BooleanType, DataType
from pyspark.sql.functions import avg

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth", 
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider", 
           "fs.azure.account.oauth2.client.id": "47fef898-ad9e-4345-89bc-ef8ca72fd782", 
           "fs.azure.account.oauth2.client.secret": "jhb8Q~MYGQEG4GASQO5B0s-UsVfhX~oBpV0oBb_H", 
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/02a73a08-bedc-4c90-8d88-bec78cf6ecff/oauth2/token"} 

dbutils.fs.mount(
    source = "abfss://tokyo-olympic-data@tokyoolympicdatanaqib.dfs.core.windows.net", 
    mount_point = "/mnt/tokyoolympic",
    extra_configs = configs)



# COMMAND ----------

# MAGIC %fs
# MAGIC ls "mnt/tokyoolympic"

# COMMAND ----------

spark

# COMMAND ----------

athletes = spark.read.format("csv").load("/mnt/tokyoolympic/raw-data/Athletes.csv")

# COMMAND ----------

athletes.show()

# COMMAND ----------

athletes = spark.read.format("csv").option("header","true").option("inferSchema", "true").load("/mnt/tokyoolympic/raw-data/Athletes.csv")

coaches = spark.read.format("csv").option("header","true").option("inferSchema", "true").load("/mnt/tokyoolympic/raw-data/Coaches.csv")

entriesgender = spark.read.format("csv").option("header","true").option("inferSchema", "true").load("/mnt/tokyoolympic/raw-data/EntriesGender.csv")

medals = spark.read.format("csv").option("header","true").option("inferSchema", "true").load("/mnt/tokyoolympic/raw-data/Medals.csv")

teams = spark.read.format("csv").option("header","true").option("inferSchema", "true").load("/mnt/tokyoolympic/raw-data/Teams.csv")

# COMMAND ----------

athletes.show()

# COMMAND ----------

athletes.printSchema()

# COMMAND ----------

coaches.show()

# COMMAND ----------

coaches.printSchema()

# COMMAND ----------

entriesgender.show()

# COMMAND ----------

entriesgender.printSchema()

# COMMAND ----------

#entriesgender = entriesgender.withColumn("Female", col("Female").cast(IntegerType()))

entriesgender = entriesgender.withColumn("Female", col("Female").cast("int"))\
    .withColumn("Male", col("Male").cast("int"))\
        .withColumn("Total", col("Total").cast("int"))


# COMMAND ----------

entriesgender.printSchema()

# COMMAND ----------

medals.show()

# COMMAND ----------

medals.printSchema()

# COMMAND ----------

teams.show()

# COMMAND ----------

teams.printSchema()

# COMMAND ----------

# Find the top countries with the highest number of gold medals.

top_gold_medal_countries =  medals.orderBy("gold", ascending = False).select("Team/NOC","Gold").show()

# COMMAND ----------

# Calculate the average number of entries by gender for each discipline

avg_entries_by_gender = entriesgender.groupBy('Discipline').agg(avg('Female').alias('Avg_Female'), avg('Male').alias('Avg_Male'), avg('Total').alias('Avg_Total')).orderBy('Discipline')
avg_entries_by_gender.show()

# COMMAND ----------

athletes.write.option("header",'true').csv("/mnt/tokyoolympic/transformed-data/athletes")
coaches.write.option("header",'true').csv("/mnt/tokyoolympic/transformed-data/coaches")
entriesgender.write.option("header",'true').csv("/mnt/tokyoolympic/transformed-data/entriesgender")
medals.write.option("header",'true').csv("/mnt/tokyoolympic/transformed-data/medals")
teams.write.option("header",'true').csv("/mnt/tokyoolympic/transformed-data/teams")

# athletes.repartition(1).write.mode("overwrite").option("header",'true').csv("/mnt/tokyoolymic/transformed-data/athletes")
# coaches.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolymic/transformed-data/coaches"
# entriesgender.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolymic/transformed-data/
# entriesgender") medals.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolymic/transformed-data/medals")
# teams.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolymic/transformed-data/teams")

# COMMAND ----------



# COMMAND ----------


