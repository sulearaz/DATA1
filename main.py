import logging
import requests
import simplejson 
import json
from flask import Flask, escape, request
from flask import render_template
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello(name=None):
    #JSON data goes here, so long as it's kept between the def function and fuchsia return, which ends its use.

    uri = "https://api.stackexchange.com/2.0/users?   order=desc&sort=reputation&inname=fuchida&site=stackoverflow"
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"  
    Jresponse = uResponse.text
    data = json.loads(Jresponse)

    displayName = data['items'][0]['display_name']# <-- The display name
    reputation = data['items'][0]['reputation']# <-- The reputation

    print(Jresponse) 
    kibble=Jresponse
    return render_template('index.html', name=kibble)


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart] <!DOCTYPE html>
