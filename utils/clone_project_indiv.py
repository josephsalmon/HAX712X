# Provide the code snippet to clone several projects from their sources to the target specified by the user (using an input dialog box).
# The user would specify the source as a CSV file having as columns:
# Prénom, Nom Patronymique, Code, URL.
# The script would clone each project in a folder named as Prénom, family_name+Prénom

import csv
import os
import subprocess
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Get the CSV file from the user
Tk().withdraw()
filename = askopenfilename()
# get the local directory of the filename file:
local_dir = os.path.dirname(filename)
# Open the CSV file
with open(filename, newline="") as csvfile:
    # Read the CSV file
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Get the first name, family name, student ID, and project URL
        first_name = row["Prénom"]
        family_name = row["Nom Patronymique"]
        student_id = row["Code"]
        project_url = row["URL"]

        # Create the folder name
        folder_name = family_name + "_" + first_name

        # Clone the project in the folder local_dir/folder_name
        os.chdir(local_dir)
        # if the URL is empty, skip this row
        if project_url == "":
            continue
        # Clone the project
        subprocess.call(["git", "clone", project_url, folder_name])

        os.chdir(folder_name)
        os.chdir("..")

        # Print the student ID
        print(student_id, family_name)
