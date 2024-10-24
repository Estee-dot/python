weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in inches: "))

weight_in_kilograms = weight * 0.45359237
height_in_meters = height * 0.0254

body_mass_index= weight_in_kilograms / height_in_meters * height_in_meters

print(" the body mass ndex is ", body_mass_index)