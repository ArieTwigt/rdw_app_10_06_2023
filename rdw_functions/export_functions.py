from typing import List
import pandas as pd
import os
from datetime import datetime


IDENTIFIER = str(datetime.now()).replace("-", "").replace(" ", "").replace(":", "").replace(".", "")


def export_cars_list_to_csv(cars_list: List, brand_name="Unkown") -> None:
    """
    Function to export a list object with cars to a csv file

    Inputs:
    * cars_list: list with cars

    Output:
    * None in Python, csv in directory
    
    """

    # convert the list to a pandas DataFrame
    cars_df = pd.DataFrame(cars_list)

    # specify the folder name
    folder_name = f"data/{brand_name}"

    # Create the folder if it does not already exists
    files_folders_in_data = os.listdir("data")

    # check if the name already exists
    if brand_name not in files_folders_in_data:
        os.mkdir(folder_name)

    # specify the filename
    file_name = f"{folder_name}/export_{IDENTIFIER}_{brand_name}.csv"

    # export the file
    cars_df.to_csv(file_name, sep=";", index=False)

