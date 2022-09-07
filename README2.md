# Project Overview
This project sets up a flask web application that either randomly
generates memes (An image with text and a quote author) or lets the user 
type in text and the author.
# Running the program
The program can be run by the CLI or a flask web app
### Command line interface
Main access is the `meme.py` script.
Called without any options it will pull example images and quotes from the `_data` folder.
Possible options are:  
`--path` Path to image file
`--body` The text for the quote to add to the image
`--author` The author of the quote to add to the image
# Roles & Responsibilities of submodules
The `QuoteEngine` submodule handels the ingestion and creation of quote objects.
The Ingestor class takes a file path and automatically chooses the fitting Ingestor
subclass to read the quotes and return a list of quote objects.

The `MemeEngine` loads the image, resizes if necessary, adds the quote and
saves the meme under the specified path.

# Examples
### CLI
`python meme.py` Creates a random meme.  
`python meme.py --body "To shit or not to shit." --author "Gnarles Barkley"`
Puts this quote on a random picture.  
`python meme.py --path "example_image.jpg" --body "To shit or not to shit." --author "Gnarles Barkley"`
Like the example above with a supplied image.

###
Start the flask web app by `python app.py`.
The console will tell you the server it is running on.
Head to the browser and enter the server it is running on.
Hit `random` to create a random meme.
Hit `custom` to create one
# Dependencies
pdftotext of xpdfReader needs to be installed on the system and available over the command line.
Download and install it [here](https://www.xpdfreader.com/pdftotext-man.html).  
Mac:  
Add the pdftotext to the path for the current terminal session:
`PATH=$PATH:/Users/<<path to xpdf tools>>/xpdf-tools-mac-4.03/bin64`

certifi==2020.12.5  
chardet==4.0.0  
click==7.1.2  
Flask==1.1.2  
idna==2.10  
itsdangerous==1.1.0  
Jinja2==2.11.3  
lxml==4.6.3  
MarkupSafe==1.1.1  
numpy==1.20.1  
pandas==1.2.3  
Pillow==8.1.2  
pydocstyle==6.0.0  
python-dateutil==2.8.1  
python-docx==0.8.10  
pytz==2021.1  
requests==2.25.1  
six==1.15.0  
snowballstemmer==2.1.0  
urllib3==1.26.4  
Werkzeug==1.0.1  
