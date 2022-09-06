import pandas as pd
from QuoteEngine import QuoteModel
from docx import Document
from abc import ABC, abstractmethod
import os
import subprocess
import csv
import pdfplumber



file_ext = {"DOCX": ".docx","PDF": ".pdf","CSV": ".csv","TXT": ".txt",}

class IngestorInterface(ABC):
    """An abstract base class that is implemented to the IngestorInterface. This class defines two methods, one of
    which returns a boolean value and the other returns a list.
    """
    @classmethod
    def verify(cls, path):
        """File extentions are checked to see if it matches. Returns boolean value."""
        return path in file_ext.values()

    @abstractmethod
    def parse(cls, path):
        """Returns a Quotemodels list for each quote found in the parsed files."""
        pass


class DocxIngestor(IngestorInterface):
    """The docx file ingestion is handled by this class. This class utilizes the IngestorInterface in order to parse
     through the docx file to return a list.
     """
    @classmethod
    def parse(cls, path):
        """Returns a list from parsed docx files."""
        doc = Document(path)
        quotes = []
        quotes = [QuoteModel(*i.text.split(" - ")) for i in doc.paragraphs]
        
        return quotes


class PDFIngestor(IngestorInterface):
    """The pdf file ingestion is handled by this class. This class utilizes the IngestorInterface in order to parse
         through the pdf file to return a list."""
    @classmethod
    def parse(cls, path):
        """The pdfplumber tool is used to extract text from the pdf that we can parse and return a list."""
        with pdfplumber.open(path) as pdf2:
            pdf_text = pdf2.pages[0].extract_text()
            text_list = pdf_text.split('\n')[: -3 or None]
            quotes = [QuoteModel(*i.rstrip("\n").split(" - ")) for i in text_list]
        return quotes  

class CSVIngestor(IngestorInterface):
    """The csv file ingestion is handled by this class. This class utilizes the IngestorInterface in order to parse
    through the csv file to return a list.
    """
    @classmethod
    def parse(cls, path):
        """Returns a list from parsed csv files."""
        with open(path) as csvfile:
            csv_1={}
            csv_1 = csv.DictReader(csvfile)
            quotes = [QuoteModel(**r) for r in csv_1]
        return quotes

class TextIngestor(IngestorInterface):
    """The text file ingestion is handled by this class. This class utilizes the IngestorInterface in order to parse
    through the text file to return a list.
    """
    @classmethod
    def parse(cls, path):
        """Returns a list from parsed text files."""
        with open(path, "r", encoding="utf-8-sig") as f:
            lines = f.readlines()
        return [QuoteModel(*i.rstrip("\n").split(" - ")) for i in lines]




class Ingestor(IngestorInterface):
    """The Ingestor class encapsulates the helper classes. It implements logic to select the appropriate helper class
    for the given file, based on filetype.
    """
    ingestors = {DocxIngestor:".docx", PDFIngestor:".pdf", CSVIngestor:".csv", TextIngestor:".txt"}
    @classmethod
    def parse(cls, path: str):
        """This will go through the defined ingestors and selects the appropriate ingestor method."""
        filename, file_ext = os.path.splitext(path)
        if not cls.verify(file_ext):
            raise ValueError("Unsupported file extension:", file_ext)
        for i in cls.ingestors:
            if cls.ingestors.get(i) == file_ext:
                return i.parse(path)
            else:
                continue


