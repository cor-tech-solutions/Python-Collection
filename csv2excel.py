import pandas as pd
import os
import glob

def convert_cv_to_excel(cv_folder, output_folder="excel_output"):
    """
    Converts all CSV files in a given folder to Excel files.

    Args:
        cv_folder: Path to the folder containing CSV files.
        output_folder: Path to the folder where Excel files will be saved.
                       Defaults to "excel_output" in the same directory.
    """

    if not os.path.exists(output_folder):
        os.makedirs(output_folder) # Create output folder if it doesn't exist

    csv_files = glob.glob(os.path.join(cv_folder, "*.csv")) # Get all CSV files

    if not csv_files:
        print(f"No CSV files found in: {cv_folder}")
        return

    for csv_file in csv_files:
        try:
            df = pd.read_csv(csv_file)
            base_name = os.path.splitext(os.path.basename(csv_file))[0] # Extract filename without extension
            excel_file = os.path.join(output_folder, f"{base_name}.xlsx")
            df.to_excel(excel_file, index=False) # Save to Excel, don't include index
            print(f"Converted: {csv_file} to {excel_file}")
        except pd.errors.ParserError as e:
            print(f"Error parsing CSV file {csv_file}: {e}") # Include the error message
        except Exception as e: # Catch other potential errors
            print(f"An unexpected error occurred processing {csv_file}: {e}")

if __name__ == "__main__":
    csv_folder = input("Enter the path to the folder containing CSV files: ")

    # Basic input validation (check if folder exists)
    if not os.path.exists(csv_folder) or not os.path.isdir(csv_folder):
        print("Invalid folder path provided.")
    else:
        output_folder = input("Enter the output folder (or press Enter for 'excel_output'): ")
        if not output_folder:
            convert_cv_to_excel(csv_folder) # Use default output folder
        else:
            convert_cv_to_excel(csv_folder, output_folder)
    input("Press Enter to exit.") # Keep console open until user presses enter