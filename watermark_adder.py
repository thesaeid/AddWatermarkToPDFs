# code by @thesaeid

# we need this library to work with pdf's
import PyPDF2

# get file names from user
input_file = input(
    "Enter the name of pdf file you wanna add watermark on(with .pdf): ")
watermark_file = input(
    "Enter the name of watermark file you wanna add(with .pdf): ")
output_file = input("Enter Output file name (with .pdf): ")

# check if output file has .pdf, if not add it
if ".pdf" not in output_file:
    output_file += ".pdf"

# opens input file
with open(input_file, "rb") as pdf_file:
    pdf = PyPDF2.PdfFileReader(pdf_file)
    # opens watermark file
    with open(watermark_file, "rb") as watermark_handle:
        watermark = PyPDF2.PdfFileReader(watermark_handle)
        # get watermark file first page
        page_watermark = watermark.getPage(0)
        # create a Pdf file writer object
        writer = PyPDF2.PdfFileWriter()

        # loop through pages of input file
        for page_num in range(pdf.getNumPages()):
            # get pages one by one
            page = pdf.getPage(page_num)
            # merging watermark and selected page of input file
            page.mergePage(page_watermark)
            # add page to writer object
            writer.addPage(page)

        # create and write into output file
        with open(output_file, "wb") as output_handle:
            writer.write(output_handle)
