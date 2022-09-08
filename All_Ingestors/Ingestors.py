"""Classes that will read the quotes from the different file types."""
import pandas as pd
from QuoteEngine import QuoteModel
from docx import Document
from abc import ABC, abstractmethod
import os
import subprocess
import csv
import pdfplumber
import tempfile


file_ext = {
    "DOCX": ".docx",
    "PDF": ".pdf",
    "CSV": ".csv",
    "TXT": ".txt",
}


class IngestorInterface(ABC):
    """An abstract base class that is implemented to the IngestorInterface.

    This class defines two methods, one of which returns a boolean value and
    the other returns a list.
    """

    @classmethod
    def verify(cls, path):
        """File extentions matches are checked and returns boolean value."""
        return path in file_ext.values()

    @abstractmethod
    def parse(cls, path):
        """Return a Quotemodels list for each quote found."""
        pass


class DocxIngestor(IngestorInterface):
    """The docx file ingestion is handled by this class."""

    @classmethod
    def parse(cls, path):
        """Return a list from parsed docx files."""
        doc = Document(path)
        quotes = []
        quotes = [QuoteModel(*i.text.split(" - ")) for i in doc.paragraphs]

        return quotes


class PDFIngestor(IngestorInterface):
    """The pdf file ingestion is handled by this class."""

    @classmethod
    def parse(cls, path):
        """Return a list from extracted pdf files."""
        temp1 = './pdf_text.txt'
        with open('pdf_text.txt', 'w') as fp:
            pass

        cmd = f"pdftotext.exe -layout -nopgbrk {path} {temp1}"
        subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        quotes = TextIngestor.parse(temp1)
        os.remove(temp1)
        return quotes


class CSVIngestor(IngestorInterface):
    """The csv file ingestion is handled by this class."""

    @classmethod
    def parse(cls, path):
        """Return a list from parsed csv files."""
        with open(path) as csvfile:
            csv_1 = {}
            csv_1 = csv.DictReader(csvfile)
            quotes = [QuoteModel(**r) for r in csv_1]
        return quotes


class TextIngestor(IngestorInterface):
    """The text file ingestion is handled by this class."""

    @classmethod
    def parse(cls, path):
        """Return a list from parsed text files."""
        with open(path, "r", encoding="utf-8-sig") as f:
            lines = f.readlines()
        return [QuoteModel(*i.rstrip("\n").split(" - ")) for i in lines]


class Ingestor(IngestorInterface):
    """Encapsulates and selects the appropriate helper class for given file."""

    ingestors = {
        DocxIngestor: ".docx",
        PDFIngestor: ".pdf",
        CSVIngestor: ".csv",
        TextIngestor: ".txt",
    }

    @classmethod
    def parse(cls, path: str):
        """Goes through ingestors and selects the appropriate method."""
        filename, file_ext = os.path.splitext(path)
        if not cls.verify(file_ext):
            raise ValueError("Unsupported file extension:", file_ext)
        for i in cls.ingestors:
            if cls.ingestors.get(i) == file_ext:
                return i.parse(path)
            else:
                continue
