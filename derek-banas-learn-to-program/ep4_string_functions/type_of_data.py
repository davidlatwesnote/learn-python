letter_z = "z"
num_3 = "3"
a_space = " " 
float_val = "3.14"
print("Is z a letter or number: ", letter_z.isalnum())
print("Is z a letter: ", letter_z.isalpha())
print("Is 3 a number: ", num_3.isdigit())
print("Is z is lower: ", letter_z.islower())
print("Is space a space: ", a_space.isspace())

def isfloat(str_val):
	try:
		float(str_val)
		return True
	except ValueError:
		return False
print("is Pi Float:", isfloat(float_val))