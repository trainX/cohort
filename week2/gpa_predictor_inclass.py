from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler
from flask import Flask, request



sc = SparkContext()
sqlContext = SQLContext(sc)

app = Flask(__name__)

# Load Data using a Dataframe versus using RDD's - it's so much easier

def init():
    gpa_df = sqlContext.read.load ("file:/root/scripts/gpa_data.csv",
        format='com.databricks.spark.csv',
        header='true',
        inferSchema='true')
        
    # Show our dataframe

    gpa_df.show()


init()
