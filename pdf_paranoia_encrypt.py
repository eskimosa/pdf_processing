import os
import PyPDF2
import send2trash


def get_all_pdf(path):
    pdf_files = []
    for folderName, sub_folders, filenames in os.walk(path):
        for filename in filenames:
            if filename.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(folderName, filename))
    return pdf_files


def add_pages(pdf_reader, pdf_writer):
    for page_num in range(pdf_reader.numPages):
        pdf_writer.addPage(pdf_reader.getPage(page_num))


def save_encrypted_pdf(pdf_writer, filename):
    result_pdf = open(filename, 'wb')
    pdf_writer.write(result_pdf)
    result_pdf.close()


def process_pdf(filename):
    with open(filename, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        pdf_writer = PyPDF2.PdfFileWriter()
        add_pages(pdf_reader, pdf_writer)
        pdf_writer.encrypt('passpass')
        save_encrypted_pdf(pdf_writer, filename[:-4] + '_encrypted.pdf')


def encrypt_pdfs(files):
    for filename in files:
        process_pdf(filename)


def decrypt_remove_original(all_pdf):
    for pdf in all_pdf:
        pdf_reader = PyPDF2.PdfFileReader(open(pdf, 'rb'))
        if pdf_reader.isEncrypted:
            pass
        else:
            send2trash.send2trash(pdf)
