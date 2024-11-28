"""
PDF Content Extraction Script using PDFium2

This script demonstrates the use of PyPDFium2Loader from LangChain to extract text content 
from PDF files. PDFium2 is Google Chrome's PDF rendering engine, wrapped for Python use,
offering high-fidelity PDF processing capabilities.

Dependencies:
   - langchain_community.document_loaders: For PDF loading interface
   - pypdfium2: Python bindings for PDFium engine
   - PDFium: Google's PDF rendering engine

Usage:
   Run the script directly to process a specified PDF file and print its content.
   Different sample files can be uncommented in the main function to test various PDF types.

Advantages:
   - High-fidelity text extraction
   - Fast processing speed (C++ backend)
   - Accurate layout preservation
   - Robust handling of complex PDFs
   - Support for modern PDF features
"""

from langchain_community.document_loaders import PyPDFium2Loader

def main():
   """
   Main function to demonstrate PDF content extraction using PDFium2.
   
   Tests different types of PDF files:
       - sample-1.pdf: Contains standard tables
       - sample-2.pdf: Contains image-based simple tables
       - sample-3.pdf: Contains image-based complex tables
       - sample-4.pdf: Contains mixed content (text, images, complex tables)
   
   PDFium2 advantages:
       - Chrome's PDF rendering engine (production-grade)
       - Better text positioning and layout preservation
       - Efficient processing of large documents
       - Robust handling of various PDF features:
           * Complex layouts
           * Modern PDF features
           * Various text encodings
           * Forms and interactive elements
       
   Returns:
       None: Prints extracted content to console
   """
   # Select PDF file to process - uncomment desired sample file
   #file_path = "input/sample-1.pdf" # Table in pdf
   #file_path = "input/sample-2.pdf" # Image based simple table in pdf
   #file_path = "input/sample-3.pdf" # Image based complex table in pdf
   file_path = "input/sample-4.pdf"  # Complex PDF with mixed content types
   
   # Initialize PDFium2 loader
   # Uses Google's PDFium engine for high-quality PDF processing
   loader = PyPDFium2Loader(file_path)
   
   # Extract content from PDF
   # Returns list of Document objects with extracted text and metadata
   # Preserves layout and positioning information
   docs = loader.load()
   
   # Output options
   #print(docs)  # Uncomment to see full Document objects including metadata
   print(docs[0].page_content)  # Print text content of first page

if __name__ == "__main__":
   main()