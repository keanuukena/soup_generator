def main():
	data = "cheese"
	room_x_axis = 2
	room_y_axis = 2

	print("""	Welcome to Soup Generator!
------------------------------------------
~Deep in the enchanted forest...
A terrible dragon has been eating
your sheep! Since you have 0 fighting
skills, the only way to defeat him is
to feed him something else...
	
Luckily, you have your magical cookbook
your grandma gave you when you
inherited the farm. Only you can
save your flock from a terrible doom!""")

	menu = """
M - Open your map
N, E, S, or W - Move
U - Use an item
I - Interact
Q - Quit
"""

	choice = "M"
	room_name = "tower"

	map = """▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒[grove][cave][marshes]▒
▒[woods][tower][fields]▒
▒[cove][farms][thicket]▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""

	while choice != "Q":
		print(menu)
		choice = input("What is your choice?\n")
		choice = choice.upper()

		if choice == "M":
			print(map)
			print(f"\nRight now you're at the {room_name}")

		elif choice == "N":
			room_y_axis += 1
			room_name = (room(data, room_x_axis, room_y_axis))
			print(f"\nRight now you're at the {room_name}")

		elif choice == "S":
			room_y_axis -= 1
			room_name = (room(data, room_x_axis, room_y_axis))
			print(f"\nRight now you're at the {room_name}")

		elif choice == "E":
			room_x_axis += 1
			room_name = (room(data, room_x_axis, room_y_axis))
			print(f"\nRight now you're at the {room_name}")

		elif choice == "W":
			room_x_axis -= 1
			room_name = (room(data, room_x_axis, room_y_axis))
			print(f"\nRight now you're at the {room_name}")
			
		elif choice == "Q":
			print("Goodbye.")

		else:
			print("That wasn't a choice!")



def room(data, room_x_axis, room_y_axis):
	if room_x_axis > 3:
		room_x_axis -= 1
	if room_y_axis > 3:
		room_y_axis -= 1
	if room_x_axis == 1 and room_y_axis == 1:
		data = "cove"

	if room_x_axis == 2 and room_y_axis == 1:
		data = "farms"

	if room_x_axis == 3 and room_y_axis == 1:
		data = "thicket"

	if room_x_axis == 1 and room_y_axis == 2:
		data = "woods"

	if room_x_axis == 1 and room_y_axis == 3:
		data = "grove"

	if room_x_axis == 2 and room_y_axis == 2:
		data = "tower"

	if room_x_axis == 2 and room_y_axis == 3:
		data = "cave"

	if room_x_axis == 3 and room_y_axis == 2:
		data = "fields"

	if room_x_axis == 3 and room_y_axis == 3:
		data = "marshes"

	return data

main()