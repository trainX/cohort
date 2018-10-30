# Setting Up Alexa

## Goal:  To configure Alexa to take a seed phrase as input and generate a song based on your trained LSTM model

## Assumption:

- Python3 is being used
- Tensorflow and/or Keras has to be installed - Use the LSTM model provided

### Background:

During the past weeks, we used Apache Spark to create a Linear Regression model to predict a persons college GPA based on their high school GPA.  This model is categorized as supervised learning because we feed the model a set of [historical data](https://github.com/trainX/cohort/blob/master/week2/gpa_data.csv) from students that contains their high school GPA and their college GPA.  This information enables the model to generate a mathmatical equation that can predict college GPA's.  We will use the high level concepts to connect our LSTM model to Alexa.

Here are the high level steps

1. Create a RestFul service from your trained model

2. Setup your skill via the Alexa console.  The screenshots I took earlier in the classed is located [here](https://docs.google.com/a/goflyball.com/presentation/d/e/2PACX-1vRc2NRSga6k3mUHDWCTdJPnqY4os7DAxpMXp2q38i77XvCj-Qwgd5TwaN2Q42tbIjWHYHkUb8nCl2jb/pub?start=false&loop=false&delayms=3000)

3. Ensure that your service is working correctly.  Remember, your service has to use HTTPS.  So, you need to secure your service if you haven't already.  The step are in the [Enabling SSL on Flask](#enabling_ssl_on_flask) section of this document

4. Test your skill from the console.  We will attempt to deploy our skills to an actual Alexa on Monday.



## Enabling SSL on Flask

0. pip3 install -r ./requirements.txt

1. Login to the server that contains your LSTM model and RestFul service that you created:


2. Change to your working directory

For example, I can change to my directory by doing this

```
cd mack
```

3. Execute the following commands

```
openssl req -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out MyCertificate.crt -keyout MyKey.key
```


4. Change the App Run line

Originally it looks like this

```
app.run(host='0.0.0.0', port=5010, debug=True, threaded=True)
```

```
app.run(host='0.0.0.0', port=5010, debug=True, threaded=True, ssl_context=('MyCertificate.crt', 'MyKey.key'))
```


5. Start screen  

```
screen -S <username>
```

Replace <your name> with your username

You can leave screen by closing your terminal of by hitting [CTRL-A] and then [d]

If you get disconnected from the server.  You can login back in and do

```
screen -r <username>
```

This will reconnect you to your screen session.

6. Start the sample LSTM service thats contained in this repo


```
python3 lstm_as_service.py
```

When it's ready, it should look like this:

```
* Serving Flask app "lstm_as_service" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on https://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
```

7. Open a web browser and execute the service

Run the following commands using the following format from your web browser

https://<external ip>:<your assigned port>/train
https://<external ip>:<your assigned port>/predict?gpa=<any integer or float>

For example,

```
https://11.22.33.44:5000/train
https://11.22.33.44:5000/predict?seed="rock the bells"
```
Note the above IP address is not real.  I'm just giving you an example of what the URL would look like 


8. Add your LSTM model to the Restful framework
