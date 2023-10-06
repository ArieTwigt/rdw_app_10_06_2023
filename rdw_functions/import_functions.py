import requests
from typing import List, Dict


# function to import RDW data
def import_cars_by_brand(brand: str) -> List[Dict]:
    """
    Imports the car from the RDW, based on the specified brand.

    Input:
    * brand: brand of a car 

    Output:
    * list of cars
    """

    # uppercase the brand
    brand_upper = brand.upper()

    # specif the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"

    # execute the request
    response = requests.get(endpoint)

    # get the cars from the response
    cars_list = response.json() 

    return cars_list