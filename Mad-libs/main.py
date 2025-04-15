import random
import time

print("Welcome to the Ultimate Mad Libs Adventure! 🚀")
print("***********************************************")  

def play_mad_libs():
    
    time.sleep(1)  # Adds a slight pause for better experience
    print("\n🌟 Fill in the blanks with your words! 🌟\n")

    adjective = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    profession = input("Enter a profession: ")
    character = input("Enter a fictional character: ")
    noun = input("Enter a random noun: ")

    stories = [
        f"One day, a {adjective} {animal} decided to {verb} all the way to {place}. "
        "Everyone was amazed, and it became the talk of the town!",

        f"In a distant {place}, there was a {adjective} {profession} who always dreamed to {verb}. "
        f"One day, they found a magic {noun}, and their life changed forever!",

        f"Once upon a time, a {adjective} {character} discovered a secret {place}. "
        f"With the help of a {adjective2} {animal}, they {verb} their way to victory!"
    ]

    final_story = random.choice(stories)

    print("\n✨ Here is Your Mad Libs Story! ✨\n")
    print( final_story )  
    print("\n🎉 Hope you enjoyed it! 🎉\n")

    if input("Do you want to play again? (yes/no): ").strip().lower() == "yes":
        print("\nRestarting...\n")
        time.sleep(1)
        play_mad_libs()
    else:
        print("\nThanks for playing! Goodbye! 👋")

play_mad_libs()
