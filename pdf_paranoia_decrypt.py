import pdf_paranoia_encrypt
import PyPDF2

pdf_path = '/Users/jenya/Desktop/becoming_full_stack/python/pdfs'


def find_encrypted_files(file):
    pdf_reader = PyPDF2.PdfFileReader(open(file, 'rb'))
    if pdf_reader.isEncrypted:
        if pdf_reader.decrypt('passpass'):
            with open(file, 'rb') as new_pdf:
                pdf_writer = PyPDF2.PdfFileWriter()
                pdf_paranoia_encrypt.add_pages(pdf_reader, pdf_writer)
                pdf_paranoia_encrypt.save_encrypted_pdf(pdf_writer, file[:-4] + '_decrypted.pdf')
                print(f"Decryption successful for {file}")
        else:
            print(f"Skipping {file}, it's not encrypted.")


if __name__ == '__main__':
    pdfs = pdf_paranoia_encrypt.get_all_pdf(pdf_path)
    for pdf_file in pdfs:
        find_encrypted_files(pdf_file)
