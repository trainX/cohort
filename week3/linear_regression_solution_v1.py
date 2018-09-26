# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Linear regression using the LinearRegressor Estimator."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
import pandas as pd
import itertools

STEPS = 1000
PRICE_NORM_FACTOR = 1000


train = pd.read_csv("gpa_data.csv", sep=",")

def main(argv):
  """Builds, trains, and evaluates the model."""
  assert len(argv) == 1
  #Load the GPA data into the system
  global train
  print(train)

# Build the training input_fn.
def input_train(data_set, num_epochs=None, n_batch = 128, shuffle=True):
    global train
    return  tf.estimator.inputs.pandas_input_fn(       
         x=pd.DataFrame(data_set['hs_gpa']),       
         y = pd.Series(data_set['c_gpa']),       
         batch_size=n_batch,          
         num_epochs=num_epochs,       
         shuffle=shuffle)
    
# Define the feature columns
feature_columns = [
      tf.feature_column.numeric_column(key="hs_gpa")
]

# Build the Estimator.
model = tf.estimator.LinearRegressor(feature_columns=feature_columns)

# Train the model.
# By default, the Estimators log output every 100 steps.
model.train(input_fn=input_train(train), 
			   steps=STEPS)


# Run the model in prediction mode.
input_dict = {
     "hs_gpa": 3.12
  }


predict_input_fn = tf.estimator.inputs.numpy_input_fn(input_dict, shuffle=False)

predict_results = model.predict(input_fn=predict_input_fn)
#TODO: Results are not printing out
print(predict_results["predictions"][0])


if __name__ == "__main__":
  # The Estimator periodically generates "INFO" logs; make these logs visible.
  tf.logging.set_verbosity(tf.logging.INFO)
  tf.app.run(main=main)
