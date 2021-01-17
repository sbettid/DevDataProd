Davide Sbetti - 14032

SMART TEXT CONTENT MODERATION

This POC represents my POC for the SMART TEXT CONTENT MODERATION project of the Development of Data Products class. 

The POC consists in a HTML interface that will apply a previously trained machine learning model to classify posts inputted by the user, providing also, for the hate speech ones, a possible "mitigating answer". 

In order to run this POC, first install the required Python packages launching from a terminal the following command: 

pip install -r requirements.txt

You can then launch the POC using the command: 

python DavideSbetti_14032-POC_WebServer.py

The launched module will load the machine learning model (you will probably see some warnings printed by tensorflow, please ignore them). 

When the webserver is ready you will see a confirmation message similar to the one reported here below: 

------------------------------------------------------------
Model loaded
 * Serving Flask app "DavideSbetti_14032-POC_WebServer" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
----------------------------------------------------------

You can now open your preferred web-browser and copy and paste the local address on which the POC has been launched (probably http://127.0.0.1:5000/ if the port is available). 