# Project Overview
The goal of this project is to construct a Meme generator. This will be a flask web application that will be responsible for dynamically generating an image with an overlaid quote, otherwise known as a meme. The skills and tools used in this project are the same skills used by **Data Engineers** and **Full stack Developers**.

# How to setup 
The program can be run through the flask web app or the comand line interface.
### Command line interface
In the command line the module can be run using this command `python3 meme.py`.
The full command setup looks like this :
    
    python -m meme --path <path_of_the_file> --body <quote_body> --author <quote_author>
    
Here are some examples of the command in action.  

![mem4](https://user-images.githubusercontent.com/111069500/188812939-8742dc12-0b51-4494-a172-0defa434f762.PNG)

Here is another example with the path of the image file included :

![mem7](https://user-images.githubusercontent.com/111069500/188813424-585c3d3d-0793-4e1f-8d2b-c916c2511fb8.PNG)

To get more information, just run `python meme.py --help`.
    
### Flask Web App
To run it with the app just use the command `python3 app.py` and go to the link.
Here are some examples of the app at work:

![mem8](https://user-images.githubusercontent.com/111069500/188956984-84b0cf4e-2884-4a15-bcb8-32a7f94139f4.PNG)

The output generates a link with a fully functional web interface from which you can generate random memes from your local file or even create one yourself.



# Module Roles and Responsibilities
The three main modules are the `QuoteEngine`, the `MemeEngine`, and the `Ingestors`.

### QuoteEngine Module
The `QuoteEngine` module is responsible for loading and parsing quotes from files. So basically its job is to recognize and ingest the different file types that contain the quotes. 

### MemeEngine
The `MemeEngine` Module is responsible for manipulating and drawing text onto images. The class implements code to load the image using pillow (PIL), resize the image, Add a quote body and a quote author to the image, and ultimately returns the path to the manipulated image. 
  
### Ingestors
The `Ingestors` module is a compilation of all the ingestor classes from which separate strategy objects are implemented in order to realize the (IngestorInterface) for each file type (csv, docx, pdf, txt). This module lives in the All_ingestors file directory.






# Dependencies
Install all needed dependencies via pip. (see below)

    pip install -r requirements.txt
    
## List of packages in requirements.txt

certifi==2021.5.30
charset-normalizer==2.0.4
click==8.0.1
Flask==2.0.1
idna==3.2
itsdangerous==2.0.1
Jinja2==3.0.1
lxml==4.6.3
MarkupSafe==2.0.1
numpy==1.19.5
pandas==1.1.5
pdfplumber==0.6.0
Pillow==8.3.1
python-dateutil==2.8.2
python-docx==0.8.11
pytz==2021.1
requests==2.26.0
six==1.16.0
urllib3==1.26.6
Werkzeug==2.0.1

