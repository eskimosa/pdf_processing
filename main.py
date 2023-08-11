import pdf_paranoia_encrypt


def start(pdfs_path):
    pdf_files = pdf_paranoia_encrypt.get_all_pdf(pdfs_path)
    pdf_paranoia_encrypt.encrypt_pdfs(pdf_files)
    pdf_paranoia_encrypt.decrypt_remove_original(pdf_files)


if __name__ == '__main__':
    pdf_loc = '/Users/jenya/Desktop/becoming_full_stack/python/pdfs'
    start(pdf_loc)
