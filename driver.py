import logging
import config
import codecs

from pdf_extractor import extract_pdf
from text_to_speech import TexttoSpeech

__author__ = 'Saurav Mukherjee'
__email__ = 'mkhrje.saurav@gmail.com'

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
    logging.info("Code started")

    # If the book is a pdf
    if config.PATH_OF_BOOK.endswith('.pdf'):
        text_contents = extract_pdf(config.PATH_OF_BOOK)

    # If its a text file
    elif config.PATH_OF_BOOK.endswith('.txt'):
        with codecs.open(config.PATH_OF_BOOK, "r", encoding="utf-8", errors="ignore") as file_to_read:
            text_contents = file_to_read.read()

    # If it is any other format of the file
    else:
        text_contents = "We just support pdf and txt now. File was either not in proper format or not loaded properly"

    # Text to speech object - also initialising the object with all the properties
    text_to_speech_obj = TexttoSpeech()

    # Converting to the audio-book
    text_to_speech_obj.text_to_speech(text_contents)

    logging.info(f"Book has been converted to audiobook and stored in {config.PATH_OF_AUDIOBOOK}")
