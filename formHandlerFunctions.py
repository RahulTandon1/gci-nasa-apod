'''
About
Consists of the 'getRightResponses' function used in app.py
to return the correct redirect/render after all the validation
'''

# ----------- IMPORTS -----------

# importing all the flask stuff that we included in app.py for safety,
# (cause the function interacts with pretty much all of the stuff that the
# main handleForm() function of app.py)
from flask import Flask, render_template, url_for, flash, \
    request, redirect
from flask_weasyprint import HTML, render_pdf


# ----------- FUNCTION DEFINITION -----------

# returns the right response to send at the very end of the formHandler
# right response can be a render / redirect.
# 'very end of the formHandler' mentioned above means the point where we
# have to send either the PDF or Webpage to the frontend
def getRightResponse(form, imgUrl, imgTitle, imgExplanation):
    # checking what kind of output the user wanted either 'pdf' or 'webpage'

    # there are 2 layers if-elif-else statements
    # the first one decide btw. 'pdf' or 'webpage' and sends an error message
    # in case it's neither.
    # the second layer which is only present in the case of PDF from 1st layer
    # ^ check btw. with/without header&footer

    if form['outputType'] == 'pdf':    # user wants pdf
        # -- send pdf to front end in whatever format the user has asked for --

        # checking what kind of pdf the user wants
        if form['pdfType'] == 'yesBanner':
            # -- send with banner pdf --

            # get and store the with banner verion in html
            src = render_template('showImg.html',
                                  imgSrc=imgUrl,
                                  imgTitle=imgTitle,
                                  imgExplanation=imgExplanation)

            # convert to pdf and send
            return render_pdf(HTML(string=src))

        elif form['pdfType'] == 'noBanner':
            # -- send without banner pdf --

            # get and store the withOUT banner verion in html
            src = render_template('noHeader.html',
                                  imgSrc=imgUrl,
                                  imgTitle=imgTitle,
                                  imgExplanation=imgExplanation)

            # convert to pdf and send
            return render_pdf(HTML(string=src))

        # never trust the user's input / form data :-)
        else:
            flash('Error: pdftType can only be "yesBanner" or "noBanner".')
            return redirect(url_for('viewForm'))

    elif form['outputType'] == 'webpage':   # user wants webpage

        # send user the webpage
        return render_template('showImg.html',
                               imgSrc=imgUrl,
                               imgTitle=imgTitle,
                               imgExplanation=imgExplanation)

    # if any other kind of value has been sent, flash error
    # might happen in the case of an attacker trying to make an exploit
    # leaving aside the fact that this is just an APOD kind of API XD
    else:

        flash('Error: outputType can only be "pdf" or "webpage".')
        redirect(url_for('viewForm'))
