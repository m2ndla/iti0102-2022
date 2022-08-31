"""EX01 Greetings."""
"""
3. GreetingsGreetingsGreetings
Example output:

Enter a greeting: Hello
Enter a recipient: world
How many times to repeat: 3
Hello world! Hello world! Hello world!

"""
# Entering a greeting.
greeting = input("Enter a greeting:")
# Entering a recipient.
recipient = input("Enter a recipient:")
# Asking how many times to repeat.
repeat_times = int(input("How many times to repeat:"))
# Defining the final greeting based on input.
final_greeting = greeting + " " + recipient + " "
# Printing the final answer.
print(final_greeting * repeat_times)
