def get_input(word_type):
    return input(f"Enter a {word_type}: ")

def create_madlib():
    # Template story with placeholders
    story_template = """
    Once upon a time, in a far away {place}, there lived a {adjective} {animal}. 
    This {animal} loved to {verb} all day long. 
    One day, while {verb_ing}, it found a {adjective_2} {object}. 
    It was the happiest day in the {animal}'s life.
    """
    
    # Collect user inputs
    place = get_input("place")
    adjective = get_input("adjective")
    animal = get_input("animal")
    verb = get_input("verb")
    verb_ing = get_input("verb ending in -ing")
    adjective_2 = get_input("another adjective")
    obj = get_input("object")

    # Fill in the placeholders
    story = story_template.format(
        place=place,
        adjective=adjective,
        animal=animal,
        verb=verb,
        verb_ing=verb_ing,
        adjective_2=adjective_2,
        object=obj
    )

    # Display the completed story
    print("\nHere is your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    create_madlib()