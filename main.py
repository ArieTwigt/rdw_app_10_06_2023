from rdw_functions.import_functions import import_cars_by_brand
from rdw_functions.export_functions import export_cars_list_to_csv
from tqdm import tqdm

# specify the brand
selected_brand =  input("Insert a car brand:\n")

# convert to a list
selected_brands_list = selected_brand.split("+")

for brand in tqdm(selected_brands_list):
    # get the cars from the RDW
    cars_list = import_cars_by_brand(brand)

    # check if the list is not empty
    if len(cars_list) == 0:
        continue

    # export the to a csv
    export_cars_list_to_csv(cars_list, brand)

