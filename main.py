#room class. I'm still not 100% there with how this magic goober works. But it does and it has royally saved my broken room coordinate system. :/
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

#start the main function, and print the intro + the menu the first time around.
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

#dear furture programming keanu, please consider making a 'pro-mode' that hides the menu. It's getting on my nerves. -testing keanu
	menu = """
M - Open your map
N, E, S, or W - Move
B - Bag
U - Use an item
I - Interact
Q - Quit
"""

#make the default variables, empty bag list and the super cool map.
	choice = "M"
	room_name = "tower"
	bag = []

	map = """▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒[grove][cave][marshes]▒
▒[woods][tower][fields]▒
▒[cove][farms][thicket]▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""

#start the infinite loop, that will end if you choose the quit option. It also starts by telling you what room you're in so you don't get lost.
	while choice != "Q":
		print(f"\nRight now you're at the {room_name}")

#room information processor. This takes your room name, processes it with 'if' statements and prints your room info.
		if room_name == "tower":
			print(f"\nGrandma's cookbook is still on the table. (Press 'I' to interact.)")

		if room_name == "cave":
			print(f"\nDank yellow-brown mushrooms glow in the darkness.\nThere is also a dark area of the cave you can't see.")
		
		if room_name == "marshes":
			print(f"\nSky blue flowers poke out of the swamp.\nThere is also a foggy area across a lake.")

		if room_name == "fields":
			print(f"\nOrange roots sprout up out of the grass.\nThe vast land looks too far to travel though.")
		
		if room_name == "thicket":
			print(f"\nFuzzy bugs buzz around the bramble.\nThe rest of the thicket is blocked by huge wooden thorns.")

		if room_name == "farms":
			print(f"\nTasty fruit ripens in the sun.\nThere is also a patch of ungrown bean seeds.")

		if room_name == "cove":
			print(f"\nSuspicious snails ooze on the rocky shore.\nYou can feel something watching you from the watery depths...")

		if room_name == "woods":
			print(f"\nPlayful butterflies dance in the underbrush.\nA strange nest sits in the treetops.")

		if room_name == "grove":
			print(f"\nPeppery nuts fall from the leaves.\nA huge, watchful bear guards a stash of sparkly honey.")

#bag remover. This annoying limit automatically drops the last item in your bag if it's ever fuller than 8 items. How rude.

#dear future programming keanu, OMG I had an idea, what if you have limited bag space at the start but every time you pick up a tier 2 ingredient it upgrades?
#this sounds like a baller idea, yo. -testing keanu
		if len(bag) > 8:
			print("Your bag is full!")
			del bag[8]

#this is the input engine, it re-prints the menu, takes and capitalizes your choice so it's ready for processing.
		print(menu)
		choice = input("What is your choice?\n")
		choice = choice.upper()

#this is the map choice, and it prints my super cool-looking map.
		if choice == "M":
			print(map)

#this is the bag check choice, it just tells you what you have in your bag using len() and a for loop.
		elif choice == "B":
			if len(bag) > 0:
				print("Right now in your bag you have...")
				for item in bag:
					print(item)
			else:
				print("Your bag is empty!")
		
#interaction engine. If you pick this choice, This thingamajig uses if statements to give you teir 1 ingredients based on your location. It just adds them to your bag list.
		elif choice == "I":
			if room_name == "cave":
				print("You scooped up 1 dank mushroom. What a fun-guy.")
				bag.append("dank shroom")

			elif room_name == "marshes":
				print("You picked a sky-blue flower! It smells nice...")
				bag.append("sky-blue flower")

			elif room_name == "fields":
				print("You pulled up a funky root! It doesn't taste like grandma's potatoes though, trust me.")
				bag.append("funky root")

			elif room_name == "thicket":
				print("You caught a fuzz-butt! These fuzzy bugs look hella goofy ngl.")
				bag.append("fuzz-butt")

			elif room_name == "farms":
				print("You harvested a magic tomato! Yes, it's a fruit! ¯\_(ツ)_/¯")
				bag.append("magic tomato")

			elif room_name == "cove":
				print("You have acquired a suspicious snail. It might have commited tax fraud and might be wanted for war crimes.")
				bag.append("sus snail")

			elif room_name == "woods":
				print("You snatched a bubbly butterfly! Its license to live has expired.'")
				bag.append("bubbly butterfly")

			elif room_name == "grove":
				print("You gathered some nuts. You can feel the holiday magic.")
				bag.append("deez nuts")

#the cookbook. This is technically still part of the interaction engine, but it's a real mess. Huge chunk of code that just uses a quick page menu to print cool pages.
			else:
				page = 1
				while page != "6":
					print("""Table o' Contents
~~~~~~~~~~~~~~~~~
1 - light and water walking potions
2 - speed and fire potions
3 - growth and water breathing potions
4 - hover and invisibility potions
5 - dragon soup
6 - leave\n""")

					page = input("Which page do you flip to?\n")

					if page == "1":
						print("""
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒ light potion:       ▒ water - walking:    ▒
▒                     ▒                     ▒
▒ #1 dank shroom      ▒ #1 sky-blue flower  ▒
▒ #2 fuzz-butt        ▒ #2 magic tomato     ▒
▒ #3 sus snail        ▒ #3 bubbly butterfly ▒
▒                     ▒                     ▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n""")
						if "dank shroom" in bag and "fuzz-butt" in bag and "sus snail" in bag:
							ask_make = input("Do you want to make a light potion? (y/n)\n")
							ask_make = ask_make.lower()
							if ask_make == "y":
								print("Your glowy yellow potion swirls around in a bottle!")
								bag.remove("dank shroom")
								bag.remove("fuzz-butt")
								bag.remove("sus snail")
								bag.append("light potion")
								page = "6"

						if "sky-blue flower" in bag and "magic tomato" in bag and "bubbly butterfly" in bag:
							ask_make = input("Do you want to make a water - walking potion?\n")
							ask_make = ask_make.lower()
							if ask_make == "y":
								print("Your ice-blue potion splashes around in a bottle!")
								bag.remove("sky-blue flower")
								bag.remove("magic tomato")
								bag.remove("bubbly butterfly")
								bag.append("water - walking potion")
								page = "6"


					elif page == "2":
						print("""
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒ speed potion:       ▒ fire potion:        ▒
▒                     ▒                     ▒
▒ #1 funky root       ▒ #1 fuzz-butt        ▒
▒ #2 deez nuts        ▒ #2 bubbly butterfly ▒
▒ #3 sus snail        ▒ #3 dank shroom      ▒
▒                     ▒                     ▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n""")
						if "funky root" in bag and "deez nuts" in bag and "sus snail" in bag:
							ask_make = input("Do you want to make a speed potion? (y/n)\n")
							ask_make = ask_make.lower()
							if ask_make == "y":
								print("Your silvery potion swooshes around in a bottle!")
								bag.remove("funky root")
								bag.remove("deez nuts")
								bag.remove("sus snail")
								bag.append("speed potion")
								page = "6"

						if "fuzz-butt" in bag and "bubbly butterfly" in bag and "dank shroom" in bag:
							ask_make = input("Do you want to make a fire potion?\n")
							ask_make == ask_make.lower()
							if ask_make == "y":
								print("Your hot red potion bubbles around in a bottle!")
								bag.remove("fuzz-butt")
								bag.remove("bubbly butterfly")
								bag.remove("dank shroom")
								bag.append("fire potion")
								page = "6"

					elif page == "3":
						print("""
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒ growth potion:      ▒ water - breathing:  ▒
▒                     ▒                     ▒
▒ #1 magic tomato     ▒ #1 sus snail        ▒
▒ #2 sky-blue flower  ▒ #2 dank shroom      ▒
▒ #3 deez nuts        ▒ #3 funky root       ▒
▒                     ▒                     ▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n""")


					elif page == "4":
						print("""
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒ hover potion:       ▒ invisibility:       ▒
▒                     ▒                     ▒
▒ #1 bubbly butterfly ▒ #1 deez nuts        ▒
▒ #sky-blue flower    ▒ #2 funky root       ▒
▒ #3 fuzz-butt        ▒ #3 magic tomato     ▒
▒                     ▒                     ▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n""")


					elif page == "5":
						print("""
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒            ~~~ Dragon Soup ~~~            ▒
▒                                           ▒
▒ #1 crystal shard   #2 wisp lily           ▒
▒ #3 mega wheats     #4 stick bug           ▒
▒ #5 deuce beans     #6 silver fish         ▒
▒ #7 random egg      #8 pooh's honey        ▒
▒                                           ▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")


					elif page == "6":
						print("You close the book.")

					else:
						print("That page is still empty.")

#movement engine. These choices add/subtract to your coordinates on the map, then talk to the room class up top and set your current room. Pretty spiffy.
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

#quit choice, it just says goodbye and since the infinite loop doesn't like Q it will exit the program after.
		elif choice == "Q":
			print("Goodbye!")

#else, print "that wasn't a choice!". This is just a bootleg try/except failsafe to catch silly responses. It does nothing but loop back around.
		else:
			print("That wasn't a choice!")

#data processor, this thing uses if statements to process your coordinates and change 'data' to the right room, which can be used by the room class I think.
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

#I stuck this main() doodad here because it didn't work without it. I'm fairly certain this just tells it to run the main function in the first place.
main()