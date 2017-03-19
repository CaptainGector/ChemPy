import main


if __name__ == "__main__":
	while True:
		print('')
		for x in range(0, len(main.inputs)):
			print("%d) "%x + main.inputs[x])
		print('')
		
		try:
			num_input = int(raw_input("Enter a number: "))
		except ValueError:
			main.output("ERROR: Please use a valid number.")
		# Hardcoded so that 0 exits the program
		if num_input == 0:
			break;
		elif main.inputs[num_input] == "Reload main.py": # Hardcoded to reload main.py
			reload(main)
		else:
			main.main(main.inputs[num_input])


