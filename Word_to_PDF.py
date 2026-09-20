# word_to_pdf_converter.py

from docx2pdf import convert
import os

def convert_word_to_pdf(input_path):
    if not os.path.exists(input_path):
        print("File not found. Please check the path and try again.")
        return

    if not input_path.lower().endswith(".docx"):
        print("Please provide a valid .docx file.")
        return

    print("Converting file, please wait...")
    convert(input_path)
    print("Conversion complete! Check the same folder for your PDF file.")

if __name__ == "__main__":
    file_path = input("Enter the path of the Word file (.docx): ")
    convert_word_to_pdf(file_path)