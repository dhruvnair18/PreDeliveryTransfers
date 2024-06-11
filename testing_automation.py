import os
import pandas as pd
#step 4c
#deleting all files in the folder ChangedFiles
print("step 4c \n")
def delete_files_in_directory(folder_path):
    try:
        files = os.listdir(folder_path)
        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                print("Deleting file:", file_path)
                os.remove(file_path)
        print("All files from CIR/ChangedFiles deleted successfully.")
    except OSError:
        print("Error occurred while deleting files.")

folder_path = r"Z:\Production\New CDP Folder Structure\CIR\ChangedFiles"
delete_files_in_directory(folder_path)

#copying and pasting all files from RAW Unity Files

# folder_path2="C:/Users/naird/OneDrive - Dun and Bradstreet/Documents/Productions/New CDP Folder Structure/RAW Unity Files/Reports"

#from pathlib import Path
import shutil

src = r"Z:\Production\New CDP Folder Structure\RAW Unity files"
trg1 = r"Z:\Production\New CDP Folder Structure\CIR\ChangedFiles"
trg2 = r"Z:\Production\New CDP Folder Structure\CIR\PDF"

def copy_and_rename_files(src_dir, trg1_dir, trg2_dir):
    try:
        # Copy files from source to target directories
        for root, dirs, files in os.walk(src_dir):
            if os.path.basename(root) == "CIR":
                for fname in files:
                    src_file_path = os.path.join(root, fname)
                    trg1_file_path = os.path.join(trg1_dir, fname)
                    trg2_file_path = os.path.join(trg2_dir, fname)
                    
                    print("\nCopying file:", src_file_path)
                    shutil.copy2(src_file_path, trg1_file_path)
                    shutil.copy2(src_file_path, trg2_file_path)
                    
        print("\nAll files from 'RAW Unity Files' CIR folders copied to CIR/ChangedFiles and CIR/PDF.")
        
        # Check and rename files in target directories
        for target_dir in [trg1_dir, trg2_dir]:
            for fname in os.listdir(target_dir):
                file_path = os.path.join(target_dir, fname)
                
                if os.path.isfile(file_path):
                    if "China Mainland" in fname:
                        new_file_path_1 = os.path.join(target_dir, fname.replace("China Mainland", "China"))
                        new_file_path_2 = os.path.join(target_dir, fname.replace("China Mainland", "Mainland China"))
                        
                        shutil.copy2(file_path, new_file_path_1)
                        os.rename(file_path, new_file_path_2)
                        
                        print(f"Renamed {fname} to Mainland China and created a copy as China in {target_dir}")
                    
                    elif "Turkei" in fname:
                        new_file_path = os.path.join(target_dir, fname.replace("Turkei", "Turkey"))
                        
                        shutil.copy2(file_path, new_file_path)
                        print(f"Created a copy of {fname} as Turkey in {target_dir}")

                    elif "Taiwan" in fname:
                        new_file_path_1 = os.path.join(target_dir, fname.replace("Taiwan", "Taiwan"))
                        new_file_path_2 = os.path.join(target_dir, fname.replace("Taiwan", "Taiwan Region"))
                        
                        shutil.copy2(file_path, new_file_path_1)
                        shutil.copy2(file_path, new_file_path_2)
                        print(f"Created copies of {fname} as Taiwan and Taiwan Region in {target_dir}")
                        
    except Exception as e:
        print("An error occurred:", str(e))

copy_and_rename_files(src, trg1, trg2)

#Step 4d
print("\n \n step 4d \n")
def delete_files_in_directory2(folder_path):
    try:
     files = os.listdir(folder_path)
     for file in files:
         file_path = os.path.join(folder_path, file)
         if os.path.isfile(file_path):
             print("\n Deleting file:", file_path)
             os.remove(file_path)
     print("\n All files deleted from CIS/ChangedFiles successfully.")
    except OSError:
     print("\n Error occurred while deleting CIS/ChangedFiles files.")

folder_path2=r"Z:\Production\New CDP Folder Structure\CIS\ChangedFiles"
delete_files_in_directory2(folder_path2)

#from pathlib import Path
#import shutil

# defining source and destination 
# paths

source = r"Z:\Production\New CDP Folder Structure\RAW Unity files"
target = r"Z:\Production\New CDP Folder Structure\CIS\ChangedFiles"
pdf_folder = r"Z:\Production\New CDP Folder Structure\CIS\PDF"
html_folder = r"Z:\Production\New CDP Folder Structure\CIS\HTML"

def copy_and_rename_files(src_dir, trg1_dir):
    try:
        # Walk through all subdirectories in src_dir
        for root, dirs, files in os.walk(src_dir):
            if os.path.basename(root) == "CIS":
                # Look for HTML and PDF folders within CIS
                for subdir in ["HTML", "PDF"]:
                    subfolder_path = os.path.join(root, subdir)
                    if os.path.exists(subfolder_path) and os.path.isdir(subfolder_path):
                        for fname in os.listdir(subfolder_path):
                            src_file_path = os.path.join(subfolder_path, fname)
                            trg1_file_path = os.path.join(trg1_dir, fname)

                            print("\nCopying file:", src_file_path)
                            shutil.copy2(src_file_path, trg1_file_path)

        print("\nAll files from CIS/HTML and CIS/PDF folders copied to CIS/ChangedFiles.")

        # Check and rename files in the target directory
        for fname in os.listdir(trg1_dir):
            file_path = os.path.join(trg1_dir, fname)

            if os.path.isfile(file_path):
                if "China Mainland" in fname:
                    new_file_path_1 = os.path.join(trg1_dir, fname.replace("China Mainland", "China"))
                    new_file_path_2 = os.path.join(trg1_dir, fname.replace("China Mainland", "Mainland China"))

                    shutil.copy2(file_path, new_file_path_1)
                    os.rename(file_path, new_file_path_2)
                    print(f"Renamed {fname} to Mainland China and created a copy as China in {trg1_dir}")

                elif "Turkei" in fname:
                    new_file_path = os.path.join(trg1_dir, fname.replace("Turkei", "Turkey"))

                    shutil.copy2(file_path, new_file_path)
                    print(f"Created a copy of {fname} as Turkey in {trg1_dir}")
                
                elif "Taiwan" in fname:
                    new_file_path_1 = os.path.join(trg1_dir, fname.replace("Taiwan", "Taiwan"))
                    new_file_path_2 = os.path.join(trg1_dir, fname.replace("Taiwan", "Taiwan Region"))
                    
                    shutil.copy2(file_path, new_file_path_1)
                    shutil.copy2(file_path, new_file_path_2)
                    print(f"Created copies of {fname} as Taiwan and Taiwan Region in {trg1_dir}")

    except Exception as e:
        print("An error occurred:", str(e))

# Call the function to copy and rename files
copy_and_rename_files(source, target)

try:
    for item in os.listdir(target):
        if os.path.isfile(os.path.join(target, item)):
            if item.endswith('.pdf'):
                 shutil.copy2(os.path.join(target, item), pdf_folder)
                 print(f"\n Copied {item} to {pdf_folder}")
            elif item.endswith('.htm'):
                shutil.copy2(os.path.join(target, item), html_folder)
                print(f"\n Copied {item} to {html_folder}")
    print("\n All files from RAW Unity Files/Reports copied successfully to pdf folder and html folder.")
except OSError:
    print("\n Error occurred while copying from RAW Unity Files/Reports to pdf folder and html folder")



#4e 
print("\n \n step 4e \n")
# src = "Z:/Dhruv(Intern)/Productions/New CDP Folder Structure/RAW Unity Files"
trge = r"Z:\Production\New CDP Folder Structure\MasterFile"
heatmap= r"Z:\Communal Stuff\New Masterfile reports\csv"
bulkdata_folder = r"Z:\Communal Stuff\Bulkdata"
def copy_files_from_reports(src_dir, trg1_dir):
    try:
        for root, dirs, files in os.walk(src_dir):
            if os.path.basename(root) == "MasterFile":
                for fname in files:
                    src_file_path = os.path.join(root, fname)
                    trg1_file_path = os.path.join(trg1_dir, fname)

                    print("\nCopying file:", src_file_path)
                    shutil.copy2(src_file_path, trg1_file_path)

        print("\nAll files from RAW Unity Files' Reports folders copied to MasterFile.")
   
    except Exception as e:
        print("An error occurred:", str(e))

copy_files_from_reports(src, trge)

try:
    for item in os.listdir(trge):
        if os.path.isfile(os.path.join(trge, item)):
            if item.startswith('2024'):
                shutil.copy2(os.path.join(trge, item), heatmap)
                print(f"\nCopied {item} to {heatmap}")
    print("\nFiles from MasterFile copied successfully to Heatmap folder.")
except OSError as e:
    print(f"\nError occurred while copying files to Heatmap folder: {e}")

try:
    # Check if the old file named MasterFileMDA exists and delete it
    old_file_path = os.path.join(trge, "MasterFileMDA.csv")
    if os.path.isfile(old_file_path):
        os.remove(old_file_path)
        print(f"Old file MasterFileMDA deleted from {trge}")
    else:
        print("No old file named MasterFileMDA found to delete.")

    # Iterate through the files in the source folder
    for item in os.listdir(trge):
        if os.path.isfile(os.path.join(trge, item)):
            if item.startswith('202'):
                try:
                    new_file_path = os.path.join(trge, "MasterFileMDA.csv")
                    os.rename(os.path.join(trge, item), new_file_path)
                    print(f"File {item} renamed to MasterFileMDA")
                except PermissionError:
                    print(f"Permission denied when trying to rename {item}.")
                    continue
                except Exception as e:
                    print(f"Error occurred while renaming {item}: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

# Save the MasterFile.csv as .xls in Bulkdata folder and replace the old file
try:
    old_bulkdata_file_path = os.path.join(bulkdata_folder, "MasterFile.xls")
    if os.path.isfile(old_bulkdata_file_path):
        os.remove(old_bulkdata_file_path)
        print(f"Old MasterFile.xlsx deleted from {bulkdata_folder}")
    else:
        print("No old MasterFile.xlsx found to delete.")
    master_file_path = os.path.join(trge, "MasterFile.csv")
    bulkdata_file_path = os.path.join(bulkdata_folder, "MasterFile.xls")

    # Read the CSV file
    df = pd.read_csv(master_file_path)

    # Save it as .xlsx
    df.to_excel(bulkdata_file_path, index=False, engine='openpyxl')

    print(f"MasterFile.csv saved as .xlsx in {bulkdata_folder}")

    # Replace the old file in Bulkdata folder
    

    # Rename the new file to the original name
    # os.rename(bulkdata_file_path, old_bulkdata_file_path)
    # print(f"New MasterFileMDA.xlsx renamed to MasterFile.xlsx in {bulkdata_folder}")

except Exception as e:
    print(f"An error occurred while saving or replacing the file: {e}")
    
#4f

news=r"Z:\Production\New CDP Folder Structure\Newsfiles"

print("Step 4f")

# Function to delete old files starting with 'country_1022'
def delete_old_files(target_dir, prefix):
    try:
        for filename in os.listdir(target_dir):
            if filename.startswith(prefix):
                old_file_path = os.path.join(target_dir, filename)
                if os.path.isfile(old_file_path):
                    os.remove(old_file_path)
                    print(f"Old file {filename} deleted from {target_dir}")
                else:
                    print(f"{filename} is not a file.")
        print("Deletion process completed.")
    except Exception as e:
        print(f"An error occurred while deleting files: {e}")

# Function to copy files from Newsfiles folders in src_dir to trg1_dir
def copy_files_from_newsfiles(src_dir, trg1_dir):
    try:
        for root, dirs, files in os.walk(src_dir):
            if os.path.basename(root) == "Newsfiles":
                for fname in files:
                    src_file_path = os.path.join(root, fname)
                    trg1_file_path = os.path.join(trg1_dir, fname)
                    print(f"\nCopying file: {src_file_path}")
                    shutil.copy2(src_file_path, trg1_file_path)
        print("\nAll files from RAW Unity Files' Newsfiles folders copied to News Files.")
    except Exception as e:
        print(f"An error occurred while copying files: {e}")

# Delete old files starting with 'CountryRisk_Data_File'
delete_old_files(news, "CountryRisk_Data_File")

# Copy files from Newsfiles folders
copy_files_from_newsfiles(src, news)

print("Step: 4g")
import zipfile
from datetime import datetime

base_dir = "Z:/Dhruv(Intern)/Productions/New CDP Folder Structure"
folders_to_zip = ['CIR', 'CIS', 'MasterFile', 'Newsfiles', 'Economic_Indicators']
output_archive_base_dir = r"Z:\Dhruv(Intern)\Productions\New CDP Folder Structure\Output Archive\2024"

current_date = datetime.now().strftime('%Y%m%d')
current_month = datetime.now().strftime('%B') 
current_year_month = datetime.now().strftime('%Y%m')
zip_filename = f"{current_date}.zip"
zip_filepath = os.path.join(base_dir, zip_filename)

# Create a zip file with the selected folders
with zipfile.ZipFile(zip_filepath, 'w') as zipf:
    for folder_name in folders_to_zip:
        folder_path = os.path.join(base_dir, folder_name)
        if os.path.isdir(folder_path):
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, base_dir)
                    zipf.write(file_path, arcname)
                    print(f"Added {file_path} to zip as {arcname}")
        else:
            print(f"Folder {folder_name} does not exist and will be skipped.")

try:
    # Ensure the output archive base directory exists
    if not os.path.exists(output_archive_base_dir):
        os.makedirs(output_archive_base_dir)

    # Create the month-specific directory within the output archive
    year_month_folder = os.path.join(output_archive_base_dir, current_year_month)
    if not os.path.exists(year_month_folder):
        os.makedirs(year_month_folder)

    # Move the zip file to the month-specific folder
    shutil.move(zip_filepath, year_month_folder)
    print(f"Zip file {zip_filename} moved to {year_month_folder}")
except Exception as e:
    print(f"An error occurred while moving the zip file: {e}")





























