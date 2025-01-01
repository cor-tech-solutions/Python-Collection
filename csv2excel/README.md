Author: Alex
Date: 1/1/2025
Description: This script converts CSV files in a folder to Excel files.

Features:

Converts all CSV files in a specified folder to Excel format.
Creates the output folder ("excel_output") if it doesn't exist.
Handles potential errors like malformed CSV files.
Provides informative messages about conversions and errors.
Allows users to specify an output folder (optional).
Requirements:

Python 3 (tested with 3.x)
pandas library (pip install pandas openpyxl) - pandas is used for reading and writing CSV/Excel files. openpyxl is a dependency for pandas to write Excel files.
How to Use:

Save the script: Save the script as a Python file (e.g., csv_to_excel.py).
Install pandas: Open a terminal or command prompt and run pip install pandas openpyxl.
Run the script: Navigate to the directory where you saved the script and run it: python csv_to_excel.py
Enter the folder path: The script will prompt you for the path to the folder containing your CSV files.
Optional: Specify output folder: The script will ask you for the output folder (or press Enter to use the default "excel_output" folder).
Review the output: The script will print messages about which files are converted and any errors encountered. Check the specified output folder for the converted Excel files.
Example Usage:

python csv_to_excel.py

Enter the path to the folder containing CSV files: /path/to/your/csv_folder

Enter the output folder (or press Enter for 'excel_output'): (Press Enter)
Converted: /path/to/your/csv_folder/data.csv to excel_output/data.xlsx
Converted: /path/to/your/csv_folder/report.csv to excel_output/report.xlsx
Additional Notes:

This script assumes your CSV files use a comma (",") as the delimiter.
For more advanced CSV parsing options, you may refer to the pandas documentation.
