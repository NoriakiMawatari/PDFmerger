"""
PDF merger
Description:
Python code that merge selected .pdf files into one unique file.
Execution:
Script is meant to be executed in the terminal:
- python3 PDFmerger.py 1st_filename.pdf 2nd_filename.pdf ...
"""
import PyPDF2
import sys
import os


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        name_splited = os.path.splitext(pdf)
        if name_splited[1] == '.pdf':
            merger.append(pdf)
            print(pdf)
        else:
            print('There´s one file that is not a pdf')
            raise Exception('Please use just .pdf files')
    merger.write('merged.pdf')


if __name__ == '__main__':
    try:
        if len(sys.argv) >= 3:
            inputs = sys.argv[1:]
            pdf_combiner(inputs)
        else:
            print('Please select 2 or more pdf files')
    except Exception as error:
        print(f'Error detected: {error}')
