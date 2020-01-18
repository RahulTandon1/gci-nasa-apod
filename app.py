# --------------- IMPORTS ---------------
from flask import Flask, render_template, url_for, flash, \
    request, redirect
from flask_weasyprint import HTML, render_pdf

# files written for myself
from generalFunctions import *
from formHandlerFunctions import *

# --------------- INITIALISING STUFF ---------------
# creating the app
app = Flask(__name__)

# fake secret key required for 'Flashing' errors using Flask
app.config['SECRET_KEY'] = 'secretsecret'

# getting API key
apiKey = getAPIKey()

# --------------- MAIN PROGRAM ---------------

# redirect the base URL to the form page
@app.route('/')
def index():
    # fill this in with a redirect afterwards
    return redirect(url_for('viewForm'))


# endpoint for the main form page that gets the date input from the user
@app.route('/form')
def viewForm():
    # gets the default date  (i.e. current date)
    # from the 'getDateRN()' function located in 'generalFunctions.py'
    defaultDate = getDateRN()

    # rendering the form
    return render_template('form.html', defaultDate=defaultDate)


# the form handler enpoint that the form in 'form.html' template uses
@app.route('/handleForm', methods=['GET', 'POST'])
def handleForm():
    '''
    TL;DR
    I just verify that the date given by the user is not from the future.
    Check if the response from the API was a 400 or something despite that.
    And finally return the right redirect / rendered pdf / rendered html page
    '''

    # getting the API key which was stored in a variable
    # in the 'INITIALISING STUFF' part
    global apiKey

    # checking if the endpoint was used as a get request by mistake
    if request.method == 'GET':

        # redirecting to the main form page
        return redirect(url_for('viewForm'))

    # ---- if the method if POST ----

    # getting the picture's date from the form's request obj
    givenDate = request.form['picDate']

    # verifiying date
    date_is_okay = verifyDate(givenDate)

    # Returning a 404 not found if the user sends
    # a date that is of the future
    # logic for if condition:
    # date_is_okay -> false
    # inverting using the NOT operator -> expression -> true
    if not date_is_okay:
        err = 'Error: Date can only be of the past or of today.'
        return render_template('404.html', errorMessage=err)

    # -- continuing if the date is valid --

    # getting url, title and explanation using givenDate and apiKey
    imgDict = fetchFromAPI(apiKey, givenDate)

    '''
    Sample json obj -> https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY
    Dictionary's keys and what they store:

    1. date -> date of image
    [to be honest, i'm not sure if this is
    the date of img being clicked or that of the image being posted
    of as the APOD]
    2. explanation -> of the image
    3. hdurl -> url of hd image
    4. media type -> (image in this case)
    5. service_version -> v1 as of 17th Jan 2020
    6. title -> title of the image
    7. url -> url of the standard image
    '''

    # in the case that there isn't an image for the give VALID date
    # e.g. happened in the case of putting the today's date
    # early in the morning.
    # sample dict in this case ->
    # imgDict {'code': 400,
    #          'msg': 'Date must be between Jun 16, 1995 and Jan 17, 2020.',
    #          'service_version': 'v1'}

    if ('code' in imgDict.keys() and imgDict['code'] == 400):
        # flashing the error message given by the APOD api itself
        flash(imgDict['msg'])
        return redirect(url_for('viewForm'))

    # getting image's URL, Title and Explanation as sent by the APOD API
    imgUrl = imgDict['url']
    imgTitle = imgDict['title']
    imgExplanation = imgDict['explanation']

    # outsourced getting the right kind of response to 'getRightResponse'
    # which is located in a separate file called 'formHandlerFunctions.py'.
    # Here response can mean -> a redirect, pdf render or html page render
    response = getRightResponse(request.form, imgUrl, imgTitle, imgExplanation)
    return response


app.run(debug=True)
