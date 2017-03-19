
eq = [
	"Cl10N2O6"	# Equation 1
]

eq2 = [
	"Rb",
	"N",
	"O",
	"Cl"
]

diatomics = [
	"H",
	"N",
	"F",
	"O",
	"I",
	"Cl",
	"Br"
]


#	 	 Hydrogen, Nitrogen, Flourine, Oxygen, Iodine, Chlrorine, Bromine
#		 Have	   No 	     Fear      Of      Ice     Cold	  Beer

#--------------------#
#---Function Stuff---#
#--------------------#

def makeFormula(atom_str, number):
	if number == '':
		print("%s%s"%(number, atom_str))
		return "%s%s"%(number, atom_str)

	print("%d%s"%(number, atom_str))
	return "%d%s"%(number, atom_str)

def isDiatomic(one, two, three): # Atom, equation
	# Get the atom
	atom_str = one
	# Get the next atom
	atom_str_2 = three
	# Get the equation
	equation_str = two
	
	#print("Atom: %s"%atom_str)
	#print("Equation: %s"%equation_str)
	
	
	for atom in diatomics:
		if atom_str == atom:
			#print("Diatomic: %s"%atom_str)

			# If parts[x+1] is null (end of equation), check with atom onward (parts[x:])
			try:
				if int(getNum(atom_str, parts[atom_str_2], equation_str)) % 2 == 0:
					resulting_number = int(getNum(atom_str, parts[atom_str_2], equation_str)) / 2
					if resulting_number != 1:	
						return True, True, makeFormula(atom_str+"2 + ", resulting_number)
					else:
						return True, True, makeFormula(atom_str+"2 + ", '')
				else:
					return True, False, "false"
			except IndexError: # Last value reached
				if int(getNum(atom_str, '', equation_str)) % 2 == 0:
					resulting_number = int(getNum(atom_str, '', equation_str)) / 2
					if resulting_number != 1:
						return True, True, makeFormula(atom_str+"2", resulting_number)
					else:
						return True, True, makeFormula(atom_str+"2", '')
				else:
					return True, False, "false"
	print('')
	# If the atom is diatomic, check if it's divisible by 2

def getNum(one, two, main):
	start = main.find(one)
	if len(one) == 2:
		start = main.find(one)+1
	end = main.find(two)
	result = main[start+1:end]
	if two == '':
		result = main[start+1:]
	if one == '':
		result = ''
	return result

#---------------------------#
# Format the first part of 
# equation into the second part
#---------------------------#

for y in range(0, len(eq)):
	print('-'*15 + 'Equation %d'%(y+1) + '-'*15)
	string = ''
	parts = []
	numbers = ''
	end = ''
	for char in eq[y]:
		for num in range(0, len(eq2)):
			if char == eq2[num]:
				string += char
				parts.append(char)
			elif eq[y][ eq[y].find(char) : eq[y].find(char)+2 ] == eq2[num]:
				string += eq[y][ eq[y].find(char) : eq[y].find(char)+2 ]
				parts.append(eq[y][ eq[y].find(char) : eq[y].find(char)+2 ])

	for x in range(0, len(parts)):
		is_diatomic, is_solvabe, chem_formula = isDiatomic(parts[x], eq[y], x+1)
		if is_diatomic:
			end += chem_formula


	print("Original: %s"%eq[y])
	print("Bits: %s"%string)
	print("Bobs: %s"%numbers)
	print("End: %s --> %s"%(eq[y], end))
	






