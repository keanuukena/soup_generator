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
room_x_axis = 2
room_y_axis = 2

map = """▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒[grove][cave][marshes]▒
▒[woods][tower][fields]▒
▒[cove][farms][thicket]▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""


while choice != "Q":
	print(menu)
	choice = str(input("What is your choice?\n"))
	choice = choice.upper()
	print()

	if choice == "M":
		print(map)
		print()
		print(f"Right now you're at the {room_name}")

	if choice == "N":
		room_y_axis += 1
		print(room(data))

print("Goodbye.")

def room(data):
	data = "gay"
	return data