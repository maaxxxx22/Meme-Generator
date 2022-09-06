class QuoteModel:
    """This class is responsible for taking in the body and the author of the quote and parsing the quote
    from the files.
    """
    def __init__(self, body="", author=""):
        """The body and the author of the quote are passed as params when the class is initiated. """
        self.body = body
        self.author = author

    def __repr__(self):
        """This will return the quote as a string representation."""
        return f"{self.body} - {self.author}"