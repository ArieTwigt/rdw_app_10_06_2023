import os


# check if the 'data' folder already exists
files_folders = os.listdir()

# check if 'data' already exists
data_folder = 'data'

if data_folder not in files_folders:
    print(f"📂 Created the data folder")
    os.mkdir(data_folder)