# Homework Week 2: Connect Your GPA Predictor to Alexa 

## Goal:  To give you experence with deploying your model and having an external application calling your prediction engine 

### Background:

During the past week, we used Apache Spark to create a Linear Regression model to predict a persons college GPA based on their high school GPA.  This model is categorized as supervised learning because we feed the model a set of [historical data](https://github.com/trainX/cohort/blob/master/week2/gpa_data.csv) from students that contains their high school GPA and their college GPA.  This information enables the model to generate a mathmatical equation that can predict college GPA's. 

1. Ensure that your GPA Predictor service is working correctly.  Remember, your service has to use HTTPS.  So, you need to secure your service if you haven't already.  The step are in the [Enabling SSL on Flask](#enabling_ssl_on_flask) section of this document

***NOTE: We are fixing the GPA Predictor service so that it outputs correctly.  I shooting to have this done by Saturday morning (Sept 15th)

2. Setup your skill via the Alexa console.  The screenshots I took is located [here](https://docs.google.com/a/goflyball.com/presentation/d/e/2PACX-1vRc2NRSga6k3mUHDWCTdJPnqY4os7DAxpMXp2q38i77XvCj-Qwgd5TwaN2Q42tbIjWHYHkUb8nCl2jb/pub?start=false&loop=false&delayms=3000)

3. Test your skill from the console.  We will attempt to deploy our skills to an actual Alexa on Monday.




## Enabling SSL on Flask

1. Login internally or externally to the server via ssh:

Internal: ssh student@10.10.10.156
Externally: ssh student@<ip address in slack> -p 3333

The password is in slack as well

2. Change to your working directory

For example, I can change to my directory by doing this

```
cd mack
```

3. Execute the following commands

```
openssl req -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out MyCertificate.crt -keyout MyKey.key
```

4. Open the predictor service in nano (text editor in Linux)

```
nano gpa_prediction.py
```

5. Change the App Run line

Originally it looks like this

```
app.run(host='0.0.0.0', port=5010, debug=True, threaded=True)
```

```
app.run(host='0.0.0.0', port=5010, debug=True, threaded=True, ssl_context=('MyCertificate.crt', 'MyKey.key'))
```


Note, make sure you change the port number to your assigned port, which is in slack.  Mine is 5010.


6. Start screen  

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

7. Start the GPA predictor service


```
python2 gpa_prediction.py
```

When it's ready, it should look like this:

```
* Serving Flask app "gpa_prediction" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on https://0.0.0.0:5010/ (Press CTRL+C to quit)
 * Restarting with stat
```

8. Open a web browser and execute the service

Run the following commands using the following format from your web browser

https://<external ip>:<your assigned port>/train
https://<external ip>:<your assigned port>/predict?gpa=<any integer or float>

For example,

```
https://11.22.33.44:5010/train
https://11.22.33.44:5010/predict?gpa=3.2
```
Note the above IP address is not real.  I'm just giving you an example of what the URL would look like 


