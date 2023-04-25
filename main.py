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
inherited her tower. Only you can
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
		print(f"\nRight now you're at the {room_name}")

		if room_name == "tower":
			print(f"\nGrandma's cookbook is still on the table. (Press 'I' to interact.)")

		if room_name == "cave":
			print(f"\nDank yellow-brown mushrooms glow in the darkness.\nThere is also a dark area of the cave you can't see.")
		
		if room_name == "marshes":
			print(f"\nSky blue flowers poke out of the swamp.\nThere is also a foggy area across a lake.")

		if room_name == "fields":
			print(f"\nOrange roots sprout up out of the grass.\nThe vast land looks too far to travel though.")
		
		if room_name == "thicket":
			print(f"\nGlowing bugs buzz around the bramble.\nThe rest of the thicket is blocked by huge wooden thorns.")

		if room_name == "farms":
			print(f"\nTasty fruit ripens in the sun.\nThere is also a patch of ungrown bean seeds.")

		if room_name == "cove":
			print(f"\nSuspicious snails ooze on the rocky shore.\nYou can feel something watching you from the watery depths...")

		if room_name == "woods":
			print(f"\nPlayful butterflies dance in the underbrush.\nA strange nest sits in the treetops.")

		if room_name == "grove":
			print(f"\nPeppery nuts fall from the leaves.\nA huge, watchful bear guards a stash of sparkly honey.")

		print(menu)
		choice = input("What is your choice?\n")
		choice = choice.upper()

		if choice == "M":
			print(map)

		elif choice == "N":
			r.room_y_axis += 1
			room_name = (room(r))

		elif choice == "S":
			r.room_y_axis -= 1
			room_name = (room(r))

		elif choice == "E":
			r.room_x_axis += 1
			room_name = (room(r))

		elif choice == "W":
			r.room_x_axis -= 1
			room_name = (room(r))
			
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