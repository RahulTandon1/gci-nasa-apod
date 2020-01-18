**Install the requirements and packages**
The python based packages can be downloaded using ```python3 -m pip install -r requirements.txt```
But for the conversion of HTML to PDF documents, I've used **weasyprint** which requires a special installation process.
Please use: https://weasyprint.readthedocs.io/en/latest/install.html to get weasy print set up and then run the ```python3 -m pip install -r requirements.txt``` command once again. You might have to add some commands to your bash profile and/or uninstall/install font-config as mentioned by online tutorials.

To make the main program (located in ```app.py```) easier to understand, I've created 2 separate files for functions that are used by the 

**Run It**
Use ```python3 app.py``` to run the application, and headover to localhost:5000

**Basic Concepts**
1. Form page which allows the user to input the date for which they want the APOD. 
2. A form handler which returns the correctly rendered html/pdf document OR redirect.

main program.
- generalFunctions.py
Used for:
    1. validating date
    2. get API key
    3. getting result from API
- formHandlerFunctions.py
Used for sending the right result to the front after basic validation has been done. 
Mainly deals with whether to send:
    A. webpage
    B. pdf file (with/without header and footer)

3. Store static files (css + js) in the static folder
4. HTML Templates in templates folder
5. API Key for NASA APOD is stored in the 'key' file, that is read from using the getApiKey and then used in the program.
**Exisiting Issues**
The UTF for the heart sybmol isn't working will making the PDF.


