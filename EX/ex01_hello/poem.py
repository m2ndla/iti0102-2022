"""EX01 Poem."""
"""
2. Poem
Example output:

Roses are red,
violets are blue,
I love to code
And so will you!

"""
# Telling the user what im asking for.
print("Hi! Help me write a poem, what word do you think would best fit in these gaps?")
print("Roses are [some color],")
print("[some plural noun] are blue,")
print("I love to [some verb]")
print("And so will you!")
# Asking for a color.
color = input("Name a color!")
# Asking for an object.
objects = input("Great! Now name a plural noun")
# Asking for an activity.
activity = input("OK! One more thing, name a verb")
# Printing the whole poem.
print("Thanks for the help! Here's the poem:")
print(f"Roses are {color},")
print(f"{objects} are blue")
print(f"I love to {activity}")
print("And so will you!")
