from argparse import ArgumentParser
from meme import generate_meme
from ingestors import Ingestors

quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
               './_data/DogQuotes/DogQuotesDOCX.docx',
               './_data/DogQuotes/DogQuotesPDF.pdf',
               './_data/DogQuotes/DogQuotesCSV.csv']

for f in quote_files:
    try:
        print(Ingestor.parse(f))
    except ValueError as error:
        print(f"ValueError: {error}")

parser = ArgumentParser(description="Generates meme and prints their path")

"""The three CLI arguments path, body and author are parsed."""
parser.add_argument("--path", type=str, required=False, nargs="?", default=None, help="path to an image file")
parser.add_argument("--body", type=str, required=False, nargs="?", default=None, help="quote body to add to the image")
parser.add_argument("--author", type=str, required=False, nargs="?", default=None, help="quote author to add to the image")
args = parser.parse_args()
print(generate_meme(args.path, args.body, args.author))
