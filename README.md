Intro
--

In a digital age where data security is paramount, safeguarding sensitive information has never been more crucial. 
This project empowers you to take control of your PDF files by implementing robust encryption and decryption mechanisms. 

The project comprises two essential tasks:
1. Encrypt PDFs - This script identifies PDF files and encrypts them using a password provided via the command line. Each encrypted PDF is saved with an appended "_encrypted.pdf" suffix to its original filename. As an added layer of verification, the program attempts to read and decrypt the newly encrypted file, ensuring the encryption process was successful.
2. Decrypt Encrypted PDFs - This script searches a designated folder structure for encrypted PDF files. When an encrypted file is detected, the script creates a decrypted copy using a user-provided password. Should an incorrect password be used, the program gracefully alerts the user while continuing its decryption process for valid files.

Requirements
--
```shell
$ cat requirements.txt
PyPDF2==1.26.0
Send2Trash==1.5.0
```

Setup
--

You can run this code by installing the requirements in a virtual environment.

```shell
$ virtualenv venv
$ venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Execute the primary script, main.py, to initiate the encryption and decryption tasks. Customize the pdf_loc variable within the script to point to the desired folder containing your PDF files.

Usage
--

Safeguard confidential contracts and legal documents with unbreakable encryption.
Securely share sensitive financial statements without fearing data breaches.
Protect intellectual property by encrypting crucial research papers and reports.
Unlock encrypted PDFs effortlessly to access your treasure trove of knowledge.

Author
--

[eskimosa](https://github.com/eskimosa/)
