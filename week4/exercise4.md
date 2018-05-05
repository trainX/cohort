# Exercise 4:  Take your data and store it in the feature_data table in the trainx database. This will prepare us to create our neural network based on the features stored in the feature_data table.

## Goal: To give you experience with storing your features into a database table.  This table will contain features for each dataset.  Hence, this table will be used to train our Tensorflow neural network. 

## System Access:

The ip address and username/password  will be provided via the trainX slack channel

- Zeppelin: http://[ip address]:9995

## Other Info:

Your column assignments for the feature_data table is below:

- 0-9: Olu
- 10-19: Howard
- 20-29: Moe
- 30-39: Aaron
- 40-49: Mack
- 50-59: Jeseekia

An example of doing this is located here: http://[zeppelin ip]:9995/#/notebook/2DFB6621V

## Task(s)

1. Put your data into a Panda dataframe if not already in that format

2. Rename the columns of the dataframe so that it matches your assigned column assignments

3. Store the data in the feature_data table using the .tosql method of the Panda dataframe

4. Validte the data was stored in the MySQL table



