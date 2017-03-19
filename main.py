import periodictable as pt
import sys 


# Avogadro's number = 6.022x10^23

avocado_number = 6.022e-23

def toScience(a_num):
	first = str(a_num)[:str(a_num).find("e")]
	second = "x10^"+str(a_num)[str(a_num).find("e")+2:]
	return first+second

def output(input_string):
	print('')
	print("--------------------------------")
	print(input_string)
	print("--------------------------------")

output("--LOADED)\n-This is a message to let you know that main.py has\n-successfully reloaded")
def main(string):
	
	x = string

	if x == "Value":
		output("ERROR: Unrecognized value.")
	elif x == "Mass of an atom":
		user_input = str(raw_input("Element name: ")).lower()
		try:	
			output("Mass: %famu"%pt.elements.name(user_input).mass)
		except ValueError:
			output("ERROR: Unknown element.")

	
	elif x == "Name of an atom":
		user_input = str(raw_input("Element abbreviation: "))
		try:
			output("Name: %s"%(pt.elements.symbol(user_input).name))
		except ValueError:
			output("ERROR: Unknown element.")
	elif x == "Abbreviation of an atom":
		user_input = str(raw_input("Element name: ")).lower()
		try:
			output("Abbreviation: %s"%pt.elements.name(user_input))
		except ValueError:
			output("ERROR: Unknown element.")
	elif x == "Grams to moles":
		user_input = str(raw_input("Element name: ")).lower()
		element = pt.elements.name(user_input)
		element_mass = element.mass
		user_input = float(raw_input("Amount of grams: "))
		grams_per_mole = user_input/element_mass
		
		o = "Element: %s\n"%str(element.name)
		u = "Grams: %f\n"%user_input
		t = "Moles: %f"%grams_per_mole

		output(o+u+t)
		
	elif x == "Moles to grams":
		user_input = str(raw_input("Element name: ")).lower()
		try:
			elem = pt.elements.name(user_input)
		except ValueError:
			print("ERROR: Element not recognized, using hydrogen.")
			elem = pt.elements.name("hydrogen")
		mass = elem.mass
		user_input = float(raw_input("Enter amount of moles: "))

		output("%s g/mol: %f/mol\n"%(elem.name, mass)+ "Total grams: %f"%(mass*user_input))
	elif x == "Moles to atoms":
		user_input = float(raw_input("Number of moles: "))
		out = 'Computer: %g\n'%(avocado_number*user_input)+'Scientific notation: %s'%(toScience(avocado_number*user_input))
		output(out)
	elif x == "Atoms to moles":
		user_input = float(raw_input("Number of atoms: "))
		output('Number of moles: %g'% (user_input/avocado_number))
	elif x == "Mass of a molecule":
		user_input_int = int(raw_input("Number of atoms: "))
		molecule = {} #Element, amount
		string = ''
		for num in range(0, user_input_int):
			user_input = str(raw_input("Element symbol: "))
			elem = pt.elements.symbol(user_input)
			user_input_int = int(raw_input("Amount: "))
			molecule[elem] = user_input_int
			if user_input_int > 1:
				string += user_input+str(user_input_int)
			else: 
				string += user_input
		out = 0.0
		for m, num in molecule.iteritems():
			out = out + m.mass*num
		output("Mass of molecule: %famu\n"%out+"Full molecule: %s"%string)
	elif x == "Conversion Factors":
		o = "-- Some Conversion utils --\n"
		u = "- Kg = 1000g\n"
		t = "- 1 amu = 1.66x10^-24 g\n"
		p = "- 1 mol = 6.02x10^23 atom/molecule\n"
		u = "- An atom's amu is the same as the amount of grams per mole.\n"
	
		output(o+u+t+p+u)
	elif x == "Diatomic atoms":
		o = "-- Diatomic Elements --\n"
		u = "Bromine, Iodine, Nitrogen, Chlorine,\n"
		t = "Hydrogen, Oxygen, and Flourine.\n"
		put = "Have No Fear Of Ice Cold Beer"
		output(o+u+t+put)
	elif x == "Run some code":
		try:
			code = input("Enter some code to run here: ")
			output(code)
		except:
			e = sys.exc_info()[0:5]
			output("Unable to run that: " + str(e))
			
	else:
		output("ERROR: Value out of range.")
	
inputs = [
	"Exit",
	"Mass of an atom",
	"Name of an atom",
	"Abbreviation of an atom",
	"Grams to moles",
	"Moles to grams",
	"Moles to atoms",
	"Atoms to moles",
	"Mass of a molecule",
	"Conversion Factors",
	"Diatomic atoms",
	"Run some code",
	"Reload main.py"
]

if __name__ == "__main__":
	while True:
		print('')
		for line in range(0, len(inputs)):
			print("%d)"%(line) + ' ' + inputs[line])

		print('')
		
		try:
			x = int(raw_input("Enter a number: "))
		except ValueError:
			x = 0
		if x == 0:
			break;
		main(inputs[x])
