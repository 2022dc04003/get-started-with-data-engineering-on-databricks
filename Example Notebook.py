# Databricks notebook source
# MAGIC %md
# MAGIC ### This is an example
# MAGIC This notebook creates a dataframe with some sample data that can be used for a quick visualization.

# COMMAND ----------

data = [[1, "Elia"], [2, "Teo"], [3, "Fang"]]
sdf = spark.createDataFrame(data, schema="id LONG, name STRING")
display(sdf)

# COMMAND ----------

def tower_of_hanoi(n, source, destination, auxiliary):
    if n > 0:
        tower_of_hanoi(n-1, source, auxiliary, destination)
        print("Move disk from {} to {}".format(source, destination))
        tower_of_hanoi(n-1, auxiliary, destination, source)

n = 3
tower_of_hanoi(n, 'A', 'C', 'B')
