"""Flask Web app interface to generate memes."""
import random
import os
import requests
from itertools import chain
from flask import Flask, render_template, abort, request
from meme import MemeEngine
from All_Ingestors.Ingestors import Ingestor


app = Flask(__name__)
meme = MemeEngine("./static")


def setup():
    """Load all resources."""
    quote_files = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]

    all_quotes = list(chain(*[Ingestor.parse(f) for f in quote_files]))

    images_path = "./_data/photos/dog/"
    all_images = []
    for root, dirs, files in os.walk(images_path, topdown=False):
        all_images = [os.path.join(root, name) for name in files]
    return all_quotes, all_images


all_quotes, all_images = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme."""
    img = random.choice(all_images)
    quote = random.choice(all_quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information."""
    return render_template("meme_form.html")


@app.errorhandler(Exception)
def http_error_handler(error):
    """Handle invalid url and returns error page."""
    return flask.render_template("error.html", error=error), error.code


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme."""
    img_temp = "./temp_image.jpg"

    """Request is used to save the image from the image_url."""
    image_url = request.form.get("image_url")
    body = request.form.get("body", "")
    author = request.form.get("author", "")

    img_data = requests.get(
        image_url, stream=True, allow_redirects=True
        ).content
    h = requests.head(image_url, allow_redirects=True)
    header = h.headers
    content_type = header.get("content-type")

    """Arguments to be mapped to the make_meme parameters."""
    m_args = {"img_path": img_temp, "text": body, "author": author}

    if "image" in content_type.lower():

        with open(img_temp, "wb") as f:
            f.write(img_data)

        path = meme.make_meme(**m_args)
        print(path)
        os.remove(img_temp)
        return render_template("meme.html", path=path)
    else:
        return render_template(
            "error.html",
            error_message="Url does not point to a valid image. Try again.",
        )


if __name__ == "__main__":
    app.run()
