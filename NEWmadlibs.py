print(" \nWelcome to my Mad Libs Game!")
message = """

The story will be a surprise. Just enter the words you \n want, and the program will reveal the story you've created \nwhen you've filled everything out. Hint: It's medical related!
"""
print(message)

word = ["Adjective", "Place", "Adjective2", "Adjective3", "Piece of Clothing", "Body Part",
        "Body Part2", "Body Part3", "Adjective4", "Noun", "Noun2", "Place2", "Adjective5"]
list = []

for wordtype in word:
    while True:
        answer = input(f"Enter {wordtype}: ")
        if answer != "":
            list.append(answer)
            break
        else:
            print("Please enter a word.")


print("\nHere's your story. Hope you enjoy!")
story_formatted = f"""\nEvery year, you should visit 
a doctor. It is a very {list[0]} visit. Usually, you 
have to skip going to {list[1]} to go. Your doctor is 
usually a {list[2]} person who is wearing a {list[3]} {list[4]}.
They will look at your {list[5]}, {list[6]}, and {list[7]}.
Sometimes, they can be very {list[8]}. Afterwards, they 
will give you a {list[9]} and a {list[10]} and your dad's 
mistress will take you to {list[11]} as a treat. All in all, 
the doctor's office isn't so {list[12]}!"""
print(story_formatted)
