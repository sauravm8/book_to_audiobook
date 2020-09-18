import PyPDF2
import config
import logging
import codecs

# Given the file path, it extracts the pdf and returns the text version of the file
def extract_pdf(file_path):

    with codecs.open(f"{config.PATH_OF_BOOK}.txt", "w", encoding="utf-8", errors="ignore") as text_to_write:
        total_txt = ""
        with open(file_path, "rb") as pdf_to_read:
            pdf_reader = PyPDF2.PdfFileReader(pdf_to_read)
            logging.info(f"Book to read -->{pdf_reader.getDocumentInfo()} has {pdf_reader.numPages} pages")
            if pdf_reader.getIsEncrypted():
                logging.info("The pdf is encrypted")

            # Getting the whole text and also saving it to interim file for processing
            for each_page_number in range(pdf_reader.numPages):
                page = pdf_reader.getPage(each_page_number)
                text_from_page = page.extractText()
                text_to_write.write(text_from_page)
                total_txt += text_from_page
            logging.info("Written into the interim text file at interim texts")

        return total_txt


