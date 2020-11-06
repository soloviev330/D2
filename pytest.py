import raven
from raven import Client

from sentry_sdk import capture_message


import bottle

app = bottle.app()
app.catchall = False

from raven.contrib.bottle import Sentry

client = Client('https://039e373048ff49d3a33edf3ca28d9b81:3ab270af7e344f37a57fd996c897a775@o471510.ingest.sentry.io/5504099?timeout=5&verify_ssl=0')
app = Sentry(app, client)

run(app=app)

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()

client.captureMessage('Hello, world4!')

@app.route('/')  
def index():  
    raise RuntimeError("There is an error!")  
    return  

app.run(host='localhost', port=8080)