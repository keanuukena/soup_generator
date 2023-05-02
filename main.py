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

	print("""  ____                       ____                           _             
 / ___|  ___  _   _ _ __    / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 \___ \ / _ \| | | | '_ \  | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
  ___) | (_) | |_| | |_) | | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
 |____/ \___/ \__,_| .__/   \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                   |_|                                                    
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
C - Controls
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
	game_end = False
	bag_space = 8
	mega_wheats = False
	stick_bug = False
	deuce_beans = False
	silver_fish = False
	random_egg = False
	poohs_honey = False
	crystal_shard = False
	wisp_lily = False

	map = """▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒[grove][cave][marshes]▒
▒[woods][tower][fields]▒
▒[cove][farms][thicket]▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""
	print(menu)
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
			if stick_bug == False:
				print(f"\nFuzzy bugs buzz around the bramble.\nThe rest of the thicket is blocked by huge wooden thorns.")
			else:
				print(f"\nFuzzy bugs buzz around the bramble.\nAsh floats through the crisp, burnt air.")

		if room_name == "farms":
			if deuce_beans == False:
				print(f"\nTasty fruit ripens in the sun.\nThere is also a patch of ungrown bean seeds.")
			else:
				print(f"\nTasty fruit ripens in the sun.\nHuge duece bean stalks soar through the clouds.")

		if room_name == "cove":
			if silver_fish == False:
				print(f"\nSuspicious snails ooze on the rocky shore.\nYou can feel something watching you from the watery depths...")
			else:
				print(f"\nSuspicious snails ooze on the rocky shore.\nThe water ripples under the salty air.")

		if room_name == "woods":
			if random_egg == False:
				print(f"\nPlayful butterflies dance in the underbrush.\nA strange nest sits in the treetops.")
			else:
				print(f"\nPlayful butterflies dance in the underbrush.\nAn empty nest sits in the treetops.")

		if room_name == "grove":
			if poohs_honey == False:
				print(f"\nPeppery nuts fall from the leaves.\nA huge, watchful bear guards a stash of sparkly honey.")
			else:
				print(f"\nPeppery nuts fall from the leaves.\nA huge, watchful bear guards a slightly emptier stash of sparkly honey.")

#bag remover. This annoying limit automatically drops the last item in your bag if it's ever fuller than it should be. How rude.
		if len(bag) > bag_space:
			print("Your bag is full!")
			del bag[bag_space]

#this is the input engine, it re-prints the menu, takes and capitalizes your choice so it's ready for processing.
		choice = input("What is your choice?\n")
		choice = choice.upper()

#this is the map choice, and it prints my super cool-looking map.
		if choice == "M":
			print(map)

		elif choice == "C":
			print(menu)

#operator commands choice that gives you items to make the game easy to test.
		elif choice == "OPERATOR_COMMANDS_69":
			print("you fly up off the ground, activating cheats. The dragon stands no chance now.")
			bag_space += 100
			bag.append("dank shroom")
			bag.append("dank shroom")
			bag.append("sky-blue flower")
			bag.append("sky-blue flower")
			bag.append("funky root")
			bag.append("funky root")
			bag.append("fuzz-butt")
			bag.append("fuzz-butt")
			bag.append("magic tomato")
			bag.append("magic tomato")
			bag.append("sus snail")
			bag.append("sus snail")
			bag.append("bubbly butterfly")
			bag.append("bubbly butterfly")
			bag.append("deez nuts")
			bag.append("deez nuts")
			bag.append("light potion")
			bag.append("water - walking potion")
			bag.append("speed potion")
			bag.append("fire potion")
			bag.append("growth potion")
			bag.append("water - breathing potion")
			bag.append("hover potion")
			bag.append("invisibility potion")

#this is the bag check choice, it just tells you what you have in your bag using len() and a for loop.
		elif choice == "B":
			if len(bag) > 0:
				bag_count = 0
				for i in bag:
					bag_count += 1
				print(f"Your bag has {bag_count}/{bag_space} items.")
				print("Right now in your bag you have...")
				for item in bag:
					print(f"* {item}")
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
					ask_make = "n"
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
							ask_make = input("Do you want to make a water - walking potion? (y/n)\n")
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
							ask_make = input("Do you want to make a fire potion? (y/n)\n")
							ask_make = ask_make.lower()
							if ask_make == "y":
								print("Your hot red potion boils in a bottle!")
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
						if "magic tomato" in bag and "sky-blue flower" in bag and "deez nuts" in bag:
							ask_make = input("Do you want to make a growth potion? (y/n)\n")
							ask_make = ask_make.lower()
							if ask_make == "y":
								print("Your fizzy green potion seethes around in a bottle!")
								bag.remove("magic tomato")
								bag.remove("sky-blue flower")
								bag.remove("deez nuts")
								bag.append("growth potion")
								page = "6"

						if "sus snail" in bag and "dank shroom" in bag and "funky root" in bag:
							ask_make = input("Do you want to make a water - breathing potion? (y/n)\n")
							ask_make = ask_make.lower()
							if ask_make == "y":
								print("Your deep blue potion rolls around in a bottle!")
								bag.remove("sus snail")
								bag.remove("dank shroom")
								bag.remove("funky root")
								bag.append("water - breathing potion")
								page = "6"

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
						if "bubbly butterfly" in bag and "sky-blue flower" in bag and "fuzz-butt" in bag:
							ask_make = input("Do you want to make a hover potion? (y/n)\n")
							ask_make = ask_make.lower()
							if ask_make == "y":
								print("Your cloudy white potion floats around in a bottle!")
								bag.remove("bubbly butterfly")
								bag.remove("sky-blue flower")
								bag.remove("fuzz-butt")
								bag.append("hover potion")
								page = "6"

						if "deez nuts" in bag and "funky root" in bag and "magic tomato" in bag:
							ask_make = input("Do you want to make an invisibility potion? (y/n)\n")
							ask_make = ask_make.lower()
							if ask_make == "y":
								print("Your clear potion wisps around in a bottle!")
								bag.remove("deez nuts")
								bag.remove("funky root")
								bag.remove("magic tomato")
								bag.append("invisibility potion")
								page = "6"

					elif page == "5":
						print("""
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒            ~~~ Dragon Soup ~~~            ▒
▒                                           ▒
▒ #1 crystal shard ★   #2 wisp lily ★      ▒
▒ #3 mega wheats ★     #4 stick bug ★      ▒
▒ #5 deuce beans ★     #6 silver fish ★    ▒
▒ #7 random egg ★      #8 pooh's honey ★   ▒
▒                                           ▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
						if "crystal shard ★" in bag and "wisp lily ★" in bag and "mega wheats ★" in bag and "stick bug ★" in bag and "deuce beans ★" in bag and "silver fish ★" in bag and "random egg ★" in bag and "pooh's honey ★" in bag:
							ask_make = input("Do you want to make dragon soup? (y/n)\n")
							ask_make = ask_make.lower()
							if ask_make == "y":
								print("""
Your dragon soup smells delicious. The smell wafts out of the tower window just as the dragon was waking up from his nap.
*YAWN* says the dragon, following the smell. "What's that yo cookin!" he says with a yell.
And sharing your soup, the dragon is content. He'll no longer eat your sheep one-hundred percent.
"I daresay I'm sorry", the dragon replies. And back off too sleep, the dragon flies.

You saved your sheep! Grandma would be proud.

~~~       THE END       ~~~

""")
								page = "6"
								game_end = True
								choice = "Q"

					elif page == "6":
						if game_end == False:
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

#this is the use_item processor. It's the chunkiest block of code for sure, but it's the whole game pretty much. It uses your potions to pass/fail on collecting tier 2 ingredients.
#It also ensures you don't waste tier 2 ingredients, (because you can't get them back), upgrades your bag, drops worthless items, etc.
		elif choice == "U":
			if len(bag) > 0:
				print("These are your items...")
				for i in bag:
					print(f"* {i}")
				use_item = input("\nWhich item do you want to use? (Press 'n' to cancel)\n")
				use_item = use_item.lower()
				if use_item == "crystal shard" or use_item == "wisp lily" or use_item == "mega wheats" or use_item == "stick bug" or use_item == "deuce beans" or use_item == "silver fish" or use_item == "random egg" or use_item == "pooh's honey":
				 use_item += " ★"
				if "potion" not in use_item and use_item != "n" and "★" not in use_item:
					try:
						bag.remove(use_item)
						print(f"Removed {use_item} from your bag.")
					except ValueError:
						print("That wasn't in your bag. (Maybe a spelling error?)")
				if "potion" in use_item and use_item != "n":
					if use_item == "speed potion":
						if room_name == "cave" or room_name == "thicket" or room_name == "forest":
							bag.remove("speed potion")
							print("Your heartbeat beats super fast. Nothing can stop you. Except for the obstacle you just ran into. Oof.")
						elif room_name == "marshes" or room_name == "farms" or room_name == "cove" or room_name == "tower":
							bag.remove("speed potion")
							print("You zoom around the place, but this doesn't seem to help. The problem with being faster than light is you can only live in darkness.")
						elif room_name == "grove":
							bag.remove("speed potion")
							print("You try to speed past the bear, juke it and break its ankles, but huge grizzly claws are great at swatting pests like you. Ouch. It also ate your dank shrooms.")
							for i in bag:
								if i == "dank shroom":
									bag.remove("dank shroom")
						else:
							if mega_wheats == False:
								print("You zoom across the wide open plane, frolicking in the meadows. Oh hey, you found the legendary mega wheats! You've only ever eaten the mini kind.")
								bag_space += 1
								bag.remove("speed potion")
								bag.append("mega wheats ★")
								mega_wheats = True
							else:
								bag.remove("speed potion")
								print("You zoom around the place, but this doesn't seem to help. The problem with being faster than light is you can only live in darkness.")

					if use_item == "fire potion":
						if room_name == "cave" or room_name == "woods" or room_name == "grove":
							bag.remove("fire potion")
							print("Hot, stuffy smoke quickly fills the space and you're forced to retreat!")
						if room_name == "marshes" or room_name == "fields" or room_name == "farms" or room_name == "tower":
							bag.remove("fire potion")
							print("The arson is great, but it doesn't seem to help in this situation. Maybe don't be so HOT-headed. heh heh..")
						if room_name == "cove":
							bag.remove("fire potion")
							print("Congratulations! Your signal fire has attracted pirates to the cove! Unfortunately, the booty-ticklin crew is swift to plunder all of your fuzz-butts.")
							for i in bag:
								if i == "fuzz-butt":
									bag.remove("fuzz-butt")
						if room_name == "thicket":
							if stick_bug == False:
								bag.remove("fire potion")
								print("You torch the thicket, blasting through as 'how bad could I possibly be' plays in your head. Hey, you found a dancing stick bug on the other side.")
								bag_space += 2
								bag.append("stick bug ★")
								stick_bug = True
							else:
								bag.remove("fire potion")
								print("The arson is great, but it doesn't seem to help in this situation. Maybe don't be so HOT-headed. heh heh..")

					if use_item == "growth potion":
						if room_name == "cave" or room_name == "thicket" or room_name == "tower":
							bag.remove("growth potion")
							print("You grow tall enough to play basketball. Unfortunately, your size gets you stuck until it wears off. Kind of a BIG problem. heh heh..")
						if room_name == "marshes" or room_name == "cove" or room_name == "grove" or room_name == "fields":
							bag.remove("growth potion")
							print("You grow extraordinarily tall, but it's lonely up here. What would grandma think if she saw how fat you've gotten?")
						if room_name == "grove":
							bag.remove("growth potion")
							print("You grow taller than the grove, tall enough to squish a bear! You can't see it in the trees, though.")
						if room_name == "woods":
							bag.remove("growth potion")
							print("Giant butterflies are cool and all, but not when they eat all of your magic tomatoes!")
							for i in bag:
								if i == "magic tomato":
									bag.remove("magic tomato")
						if room_name == "farms":
							if deuce_beans == False:
								bag.remove("growth potion")
								print("The beans grow into rare deuce beans ★! The stinky smell grew a little, too.")
								bag_space += 1
								bag.append("deuce beans ★")
								duece_beans = True
							else:
								bag.remove("growth potion")
								print("You grow extraordinarily tall, but it's lonely up here. What would grandma think if she saw how fat you've gotten?")

					if use_item == "water - breathing potion":
						if room_name != "marshes" and room_name != "cove":
							bag.remove("water - breathing potion")
							print("Your respiratory system changes, and now no amount of water can stand in your way! ..if only there was some water nearby.")
						if room_name == "marshes":
							bag.remove("water - breathing potion")
							print("You dive into the lake, ready to swim to the other side. Suddenly, a swamp monster kindly removes you from his territory. He also took your funky roots!")
							for i in bag:
								if i == "funky root":
									bag.remove("funky root")
						if room_name == "cove":
							if silver_fish == False:
								bag.remove("water - breathing potion")
								print("You dive underwater and encounter a silver fish ★! Is soft scales glitter in the deep.")
								bag_space += 2
								bag.append("silver fish ★")
								silver_fish = True
							else:
								bag.remove("water - breathing potion")
								print("Unfortunately, water breathing snails are a bit harder to come by, and there's nothing interesting underwater.")

					if use_item == "hover potion":
						if room_name == "tower" or room_name == "cave":
							bag.remove("hover potion")
							print("You float up off the ground.. You can fly! Up until you bonk your head on the hard ceiling, that is.")
						if room_name == "fields" or room_name == "marshes" or room_name == "thicket" or room_name == "farms" or room_name == "cove" or room_name == "grove":
							bag.remove("hover potion")
							print("You hover in the air, but there's not very many potion ingredients up here. You crash land on your rump, most unhelpfully.")
						if room_name == "woods":
							if random_egg == False:
								bag.remove("hover potion")
								print("You easily float up to the tree with the butterflies. Hey, look, a random egg ★! Luckily, this egg's absent single father is off getting milk or something.")
								bag_space += 1
								bag.append("random egg ★")
								random_egg = True
							else:
								bag.remove("hover potion")
								print("You lazily float up to the top of the tree, only to find an empty home. Shoot, now you're depressed or something.")

					if use_item == "invisibility potion":
						if room_name != "grove":
							bag.remove("invisibility potion")
							print("Hey look, you're invisible! This would be the best prank ever, but there's no one around to spook!")
						else:
							if poohs_honey == False:
								bag.remove("invisibility potion")
								print("You stealthily creep past the bear. Luckily the bear has a stuffy nose and can't smell anything. You got pooh's honey ★!")
								bag_space += 2
								bag.append("pooh's honey ★")
								poohs_honey = True
							else:
								bag.remove("invisibility potion")
								print("You're invisibile, but grandma wouldn't want you to take such a risk for nothing. Best to play it safe.")

					if use_item == "light potion":
						if room_name != "cave":
							bag.remove("light potion")
							print("I said, oooooooooOOOOOOOOooooooooohhhhhhhhh I'm blinded by the lights~ Unfortunately, your glowing skin is most unhelpful.")
							if room_name == "woods":
								bag.remove("light potion")
								print("You glow defiantly under the shade of the trees. But your blinded butterflies are less impressed and leave you!")
								for i in bag:
									if i == "bubbly butterfly":
										bag.remove("bubbly butterfly")
						if room_name == "cave":
							if crystal_shard == False:
								bag.remove("light potion")
								print("You easily illuminate the back of the cave, and spot a shiny crystal shard ★! It sparkles in the light.")
								bag_space += 1
								bag.append("crystal shard ★")
								crystal_shard = True
							else:
								bag.remove("light potion")
								print("A soft glow fills the cave, but there's nothing left in here. It's super interesting how boring this cave is.")

					if use_item == "water - walking potion":
						if room_name != "marshes":
							bag.remove("water - walking potion")
							print("You feel the power of christ flowing within you. You know you can walk on water, but there's no water around to prove it. Well shoot.")
							if room_name == "cove":
								bag.remove("water - walking potion")
								print("You step across the water of the cove, feeling magical. Your seasick snails, on the other hand, don't. They're quick to abandon ship.")
								for i in bag:
									if i == "sus snail":
										bag.remove("sus snail")
						if room_name == "marshes":
							if wisp_lily == False:
								bag.remove("water - walking potion")
								print("You cross the lake, thoroughly confusing some boaters as you pass. On the other side you find a wisp lily ★! I thought they were extinct.")
								bag_space += 2
								bag.append("wisp lily ★")
								wisp_lily = True
							else:
								bag.remove("water - walking potion")
								print("You cross the lake, but there's nothing left on this side of the swamp but an ogre you'd rather not annoy.")

				if "★" in use_item:
					print("You ought to save that for later.")
			else:
				print("You have nothing to use!")

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