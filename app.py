# importing flask
from flask import Flask, render_template, url_for
import requests
import json


def getApiKey():
    f = open('key', 'r')
    key = f.read()
    print(key)
    f.close()
    return key


apiKey = getApiKey()

# creating the app
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def tryingApi():
    apiKey = getApiKey()
    # date ='YYYY-MM-DD'
    url = f'https://api.nasa.gov/planetary/apod?api_key={apiKey}?date=2003-02-01'
    result = requests.get(url)
    print(result.status_code)

    res = json.loads(result.content)
    basicImgUrl = res['url']
    print('img url:', basicImgUrl)
    img = requests.get(basicImgUrl).content
    f = open('img.jpg', 'wb')
    f.write(img)
    f.close()

app.run(debug=True)
