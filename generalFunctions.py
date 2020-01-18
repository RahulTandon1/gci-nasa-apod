'''
About
Consits of functions used within app.py.
Written here to make the code more readable in general.

This file/script/module has 3 functions:
1. verifyDate()
Checks the date that the user entered in the front end, that is passed to it
in string format and returns a boolean specifying if the date is
NOT of the future
i.e. today + past -> True | Future dates -> False.

2. getApiKey()
Reads the NASA APOD API Key stored in the file called 'key' and returns it

3. fetchFromAPI()
Takes input of the API Key and verified date (using verifyDate from above)
and returns the dictionary form of the response object sent by the API.
'''

# -------------- IMPORTS --------------

# for getting the API's result
import requests

# for converting result from JSON to a Python Dictionary
import json

# for handling date comparisons and conversions
from datetime import datetime


# -------------- FUNCTION DEFINITIONS --------------

# takes input of the date in the form of a string
# returns whether or not the date is valid in the form of a boolean
# where valid means less than or equal to the day's date
def verifyDate(dateStr):

    # ensuring string type to avoid any errors
    dateStr = str(dateStr)

    # the format in which the date given by the user will be
    # (it'll be given to us in the form of a string)
    givenDateFormat = '%Y-%m-%d'
    '''
    Meaning of the symbols above:
    %Y - Year with century as a decimal number - e.g. 0001, 0002...2001....9999
    %m - Month as a zero-padded decimal number - e.g. 01, 02...12
    %d - Day of the month as a zero-padded decimal number - e.g. 01, 02, 31
    src:
    https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    '''
    # since we only need the date and NOT the time
    # we convert the givenDate to a datetime object / type
    # and get only the date using 'date()'
    givenDate = datetime.strptime(dateStr, givenDateFormat).date()

    # getting today's date for comparison
    rn = datetime.today().date()

    '''
    Note: dates of the future are > dates of the past
    '''

    # comparing the date the user sent with the today's date
    if givenDate > rn:  # if user's given date is in the future
        return False

    else:   # i.e. givenDate is less/equal to today's date
        return True


# reads the NASA APOD apiKey from the file called 'key'
# and returns it
def getAPIKey():

    # opening file called 'key', with 'read' 'mode'
    f = open('key', 'r')

    # reading from file and storing in temporary variable
    # file only consists of the API key, so we read all of it in one go
    # also we store in a temporary variable so that we can close the file
    # and THEN send the api key
    key = f.read()

    # closing file for convention and it can cause errors from what I've read
    f.close()

    # returning the key
    return key


# takes input of apiKey and date of the picture to be taken
# returns an object consisting of:
# 1. url of image
# 2. title of image
# 3. explanation of image
def fetchFromAPI(apiKey, picDate):

    # date format for api-> ='YYYY-MM-DD'
    # fortuntaely, the user's given date will also come in that format
    # (the format in which the 'form.html' template sends the date to backend)

    apiKey = apiKey

    # if picDate is not assigned
    if not bool(picDate):
        # assign it today's date
        picDate = datetime.today().date()

    # forming URl
    url = (
        f'https://api.nasa.gov/planetary/apod?api_key={apiKey}&date={picDate}'
        )

    # getting result using the requests module
    result = requests.get(url)

    # printing response status code
    print('request status code', result.status_code)

    # parsing the result's content into a dictionary
    # by default it's a json string (to the best of my knowledge)
    res = json.loads(result.content)
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

    '''
    Reason for choosing to pass the object as it is from this function

    Had an option between the following:
    1. Making a new dict of selected key:value pairs and and returning that
    // rejected because the endpoint handler would anyway have to
    // get all the value from keys again

    2. Using tuple which can be unpacked
    // essentially same thing as the dict option
    // BUT, it's not good design since it relies on the order in which
    // values are put in tuple, i.e. things can go haywire with minor changes
    // so rejected as well

    3. returning the object as it is
    // while the endpoint handler would need to be passed the entire object
    // which might endup getting a bit more computationally costly
    // compared to the other options, it makes the most sense to me.
    So I chose this
    '''

    # returning the dictionary
    return res


# returns today's date as a string in YYYY-MM-DD format
# used for setting default date in the 'form.html' template
def getDateRN():
    # getting the date right now by:
    # first getting datetime of right now
    # and getting date from that
    # returns a tuple of format -> (yyyy, mm, dd)
    dateRN = datetime.today().date()

    # returns a string in 'iso format'
    # see docs at:
    # https://docs.python.org/3/library/datetime.html#datetime.date.isoformat
    formattedDate = dateRN.isoformat()
    return formattedDate
