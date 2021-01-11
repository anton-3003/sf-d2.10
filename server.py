import os
import configparser
import sentry_sdk
from bottle import Bottle, request, response, run, route
from sentry_sdk.integrations.bottle import BottleIntegration

config = configparser.ConfigParser()
config.read('settings.ini')

sentry_link = config["MySet"]['DSN']


sentry_sdk.init(
    dsn=sentry_link,
    integrations=[BottleIntegration()]
)

app = Bottle()


@route("/")
def index():
    html = """
            <!doctype html>
            <html lang="en">
              <head>
                <title>HomeWork D2.10</title>
              </head>
              <body>
                <div class="container">
                  <h1>Домашняя работа D2.10</h1>
                  <p><a href="/success">Тут удачный запрос</a></p>
                  <p><a href="/fail">А тут с ошибкой</a></p>
                  <p><a href="/joke">А тут шутка</a></p>
                </div>
              </body>
            </html>
          """
    return html


@route("/success")
def successR():
    return response.status


@route("/fail")
def failR():
    raise RuntimeError("There is an error!")
    return 'HTTP статус - {status}'.format(status=response.status)


@route("/joke")
def teapotR():
    joke_response = "HTTP статус - 418 \nЯ - чайник \n{status}".format(status=response.status)
    return joke_response


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)

