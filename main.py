class Data():
	def __init__(self):
		self.room_x_axis = 2
		self.room_y_axis = 2
	
	@property
	def room_y_axis(self):
		return self.__room_y_axis
	@room_y_axis.setter
	def room_y_axis(self, new):
		if 1 <= new and new <= 3:
			self.__room_y_axis = new

	@property
	def room_x_axis(self):
		return self.__room_x_axis
	@room_x_axis.setter
	def room_x_axis(self, new):
		if 1 <= new and new <= 3:
			self.__room_x_axis = new

def main():
	r = Data()

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
			r.room_y_axis += 1
			room_name = (room(r))
			print(f"\nRight now you're at the {room_name}")

		elif choice == "S":
			r.room_y_axis -= 1
			room_name = (room(r))
			print(f"\nRight now you're at the {room_name}")

		elif choice == "E":
			r.room_x_axis += 1
			room_name = (room(r))
			print(f"\nRight now you're at the {room_name}")

		elif choice == "W":
			r.room_x_axis -= 1
			room_name = (room(r))
			print(f"\nRight now you're at the {room_name}")
			
		elif choice == "Q":
			print("Goodbye.")

		else:
			print("That wasn't a choice!")



def room(r):
	data = "cheese"
	if r.room_x_axis == 1 and r.room_y_axis == 1:
		data = "cove"

	if r.room_x_axis == 2 and r.room_y_axis == 1:
		data = "farms"

	if r.room_x_axis == 3 and r.room_y_axis == 1:
		data = "thicket"

	if r.room_x_axis == 1 and r.room_y_axis == 2:
		data = "woods"

	if r.room_x_axis == 1 and r.room_y_axis == 3:
		data = "grove"

	if r.room_x_axis == 2 and r.room_y_axis == 2:
		data = "tower"

	if r.room_x_axis == 2 and r.room_y_axis == 3:
		data = "cave"

	if r.room_x_axis == 3 and r.room_y_axis == 2:
		data = "fields"

	if r.room_x_axis == 3 and r.room_y_axis == 3:
		data = "marshes"

	return data

main()