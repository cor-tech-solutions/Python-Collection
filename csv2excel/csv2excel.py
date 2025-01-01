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

    # Check if the output folder exists. If not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder) # Create output folder if it doesn't exist

    # Use glob to get a list of all CSV files in the input folder
    csv_files = glob.glob(os.path.join(cv_folder, "*.csv"))

    # Check if any CSV files were found.
    if not csv_files:
        print(f"No CSV files found in: {cv_folder}")
        return

    # Iterate through each CSV file.
    for csv_file in csv_files:
        try:
            # Read the CSV file into a pandas DataFrame.
            df = pd.read_csv(csv_file)
            
            # Extract the base filename (without extension).
            base_name = os.path.splitext(os.path.basename(csv_file))[0]
            
            # Create the output Excel filename.
            excel_file = os.path.join(output_folder, f"{base_name}.xlsx")
            
            # Save the DataFrame to an Excel file (without the index).
            df.to_excel(excel_file, index=False)
            
            # Print a success message.
            print(f"Converted: {csv_file} to {excel_file}")
            
        except pd.errors.ParserError as e:
            # Handle errors that occur during CSV parsing (e.g., malformed CSV).
            print(f"Error parsing CSV file {csv_file}: {e}") # Include the error message
        except Exception as e:
            # Handle any other unexpected errors during file processing.
            print(f"An unexpected error occurred processing {csv_file}: {e}")

if __name__ == "__main__":
    # Get the input folder path from the user.
    csv_folder = input("Enter the path to the folder containing CSV files: ")

    # Basic input validation: Check if the folder exists and is a directory.
    if not os.path.exists(csv_folder) or not os.path.isdir(csv_folder):
        print("Invalid folder path provided.")
    else:
        # Get the output folder path from the user (or use the default).
        output_folder = input("Enter the output folder (or press Enter for 'excel_output'): ")
        if not output_folder:
            convert_cv_to_excel(csv_folder) # Use default output folder
        else:
            convert_cv_to_excel(csv_folder, output_folder)
            
    # Keep the console window open until the user presses Enter
    input("Press Enter to exit.")
