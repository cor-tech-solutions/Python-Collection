import os
import sys
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_paths, output_path):
    """Merges multiple PDF files into a single PDF.
    
    Args:
        pdf_paths: A list of paths to the PDF file to merge.
        output_path: The path to save the merged PDF.
        
    Returns:
        True if the merge was successful, False otherwise (e.g., if a file is not found).
        Prints error messages to stderr in case of issues.
    """
    merger = PdfMerger() # Initialize the PDF merger object
    
    for pdf_path in pdf_paths:
        if not os.path.exists(pdf_path):
            print(f"Error: PDF file not found: {pdf_path}", file=sys.stderr)
            return False # Return False immediately if a file is missing
        try:
            merger.append(pdf_path) # Append the current PDF to the merger
        except Exception as e:
            print(f"Error processing {pdf_path}: {e}", file=sys.stderr)
            return False # Return False if there is an issue with a PDF
        
    try:
        merger.write(output_path) # Write the merged PDF to the output file
        merger.close() # Close the merger object to release resources
        print(f"Error writing the merged PDF: {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error writing the merged PDF: {e}", file=sys.stderr)
    

def main():
    if len(sys.argv) < 3:
        print("Usage: python merge_pdfs.py output.pdf input1.pdf [input2.pdf ...]", file=sys.stderr)
        return 1 # Indicate an error
    
    output_pdf = sys.argv[1] # Get the output PDF path from the command line
    input_pdfs = sys.argv[2:] # Get the input PDF path from the command line
    
    # Call merge_pdfs and handle the return value.
    if merge_pdfs(input_pdfs, output_pdf):
        return 0 # Indicate success
    else:
        return 1 # Indicate failure
    
if __name__ == "__main__":
    sys.exit(main()) # Execute the main function when the script is run