from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.linalg import Vectors
from pyspark.mllib.linalg import DenseVector
from pyspark.sql.types import *
from flask import Flask, request

sc = SparkContext()
sqlContext = SQLContext(sc)
spark= sqlContext.sparkSession

app = Flask(__name__)

model = None

gpa_df = sqlContext.read.load("./gpa_data.csv",
    format='com.databricks.spark.csv',
    header='true',
    inferSchema='true')

lr = LinearRegression(maxIter=20)
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
    global model

    training = split[0]
    model = lr.fit(training)
    return 'It\'s Trained!'

@app.route('/predict')
def doPredict():
    if request.args.get('gpa') == None:
        return "Please specify a GPA as URL parameter.  For example: http://my.example.com/predict?gpa=2.9"
   
    raw_gpa = float(request.args.get('gpa'))
    data = [{'hs_gpa_vector':Vectors.dense(raw_gpa)}]
    hs_gpa = sqlContext.createDataFrame(data)
    predictions = model.transform(hs_gpa)
    predictions.show()

    first = predictions.first()

    return str(first.prediction)

app.run(host='0.0.0.0', port=5010, debug=True, threaded=True)
