from calculation_functions.size_functions import calc_circle, calc_contents
from name_functions.conversion_funcctions import capitalize_names

#my_diameter = float(input("Insert the diameter:\n"))

#my_size, my_radius = calc_circle(double_up=True, diameter=10, rounding=5)

my_size = calc_contents(2, 4, 10)
my_names = ['jim', 'john', 'marc', 'danny', 'peter']

my_new_names = capitalize_names(my_names)

print(my_size)
print(my_new_names)
pass

