"""
PDF Content Extraction Script using PDFPlumber

This script demonstrates the use of PDFPlumberLoader from LangChain to extract text and tabular 
content from PDF files. PDFPlumber excels at extracting both textual content and tables,
making it particularly useful for documents with mixed content types.

Dependencies:
   - langchain_community.document_loaders: For PDF loading functionality
   - pdfplumber: Backend PDF processing library with enhanced table extraction

Usage:
   Run the script directly to process a specified PDF file and print its content.
   Different sample files can be uncommented in the main function to test various PDF types.

Advantages:
   - Better table extraction compared to PDFMiner
   - Maintains text positioning and layout information
   - Can extract table borders and cell properties
"""

from langchain_community.document_loaders import PDFPlumberLoader

def main():
   """
   Main function to demonstrate PDF content extraction using PDFPlumber.
   
   Tests different types of PDF files:
       - sample-1.pdf: Contains standard tables
       - sample-2.pdf: Contains image-based simple tables
       - sample-3.pdf: Contains image-based complex tables
       - sample-4.pdf: Contains mixed content (text, images, complex tables)
   
   The function uses PDFPlumber which is particularly good at:
       - Extracting tables while maintaining structure
       - Preserving text positioning
       - Handling complex layouts
       
   Returns:
       None: Prints extracted content to console
   """
   # Select PDF file to process - uncomment desired sample file
   #file_path = "input/sample-1.pdf" # Table in pdf
   #file_path = "input/sample-2.pdf" # Image based simple table in pdf
   #file_path = "input/sample-3.pdf" # Image based complex table in pdf
   file_path = "input/sample-4.pdf"  # Complex PDF with mixed content types
   
   # Initialize PDFPlumber loader with target file
   loader = PDFPlumberLoader(file_path)
   
   # Extract content from PDF
   # Returns list of Document objects containing both text and table data
   docs = loader.load()
   
   # Output options
   #print(docs)  # Uncomment to see full Document objects including metadata
   print(docs[0].page_content)  # Print only the text/table content of first page

if __name__ == "__main__":
   main()