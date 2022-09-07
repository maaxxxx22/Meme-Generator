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
    
### Flask Web App
To run it with the app just use the command `python3 app.py` and go to the link.
Here are some examples of the app at work:



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
nd 
###
Start the flask web app by `python app.py`.
The console will tell you the server it is running on.
Head to the browser and enter the server it is running on.
Hit `random` to create a random meme.
Hit `custom` to create one
# Dependencies
Install all needed dependencies via pip. (see below)

    pip install -r requirements1.txt

