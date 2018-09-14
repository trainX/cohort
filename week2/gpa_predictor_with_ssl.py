from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.linalg import Vectors
from pyspark.sql.types import *
from flask import Flask, request

sc = SparkContext()
sqlContext = SQLContext(sc)

app = Flask(__name__)

model = None

gpa_df = sqlContext.read.load("./gpa_data.csv",
    format='com.databricks.spark.csv',
    header='true',
    inferSchema='true')

lr = LinearRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)
lr.setFeaturesCol("hs_gpa_vector")
lr.setLabelCol("c_gpa")

assembler = VectorAssembler(inputCols=["hs_gpa"],outputCol="hs_gpa_vector")
output = assembler.transform(gpa_df)
split = output.randomSplit([0.7,0.3])

@app.route('/home')
def doHome():
    return 'Hello, World!'

@app.route('/train')
def doTrain():
    training = split[0]
    model = lr.fit(training)
    return 'It\'s Training!'

@app.route('/predict')
def doPredict():
    #vectorizedRequestData = Vectors.dense(float(request.args.get('gpa')))
    #hs_gpa = sqlContext.createDataFrame([(vectorizedRequestData),], ["hs_gpa_vector"])
    hs_gpa = sqlContext.createDataFrame([(Vectors.dense(2.9),)],["hs_gpa_vector"])
    predictions = model.transform(hs_gpa)
    return predictions.show()

app.run(host='0.0.0.0', port=5010, debug=True, threaded=True, ssl_context=('MyCertificate.crt', 'MyKey.key'))
