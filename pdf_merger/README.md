Author: Alex
Date: 1/1/2025
Description: This Python script that combines multiple PDF files into a single PDF.

Features
Merges multiple PDF files into one.
Handles potential errors like missing files or invalid PDFs.
Provides informative error messages for troubleshooting.
Usage
Install PyPDF2:
Bash

pip install PyPDF2
Save the script: Save the code as a Python file (e.g., merge_pdfs.py).
Run from the command line:
Bash

python merge_pdfs.py output.pdf input1.pdf input2.pdf [input3.pdf ...]
Replace output.pdf with the desired name for the merged PDF file.
Replace input1.pdf, input2.pdf, etc., with the paths to the PDF files you want to merge.
Example:

To merge file1.pdf, file2.pdf, and file3.pdf into a new file called merged.pdf, you would run:

Bash

python merge_pdfs.py merged.pdf file1.pdf file2.pdf file3.pdf
How it Works
The script iterates through the provided input PDF paths. For each path:

It checks if the file exists.
If the file exists, it uses the PyPDF2 library to append the PDF content to the merger object.
Finally, it writes the merged content to the specified output PDF file.
Error Handling
The script checks for missing input files and invalid PDFs.
In case of errors, it prints informative error messages to the console.
The script returns a success or failure code for easy integration with other scripts.
Contributing
If you find a bug or have a suggestion for improvement, feel free to submit a pull request.
