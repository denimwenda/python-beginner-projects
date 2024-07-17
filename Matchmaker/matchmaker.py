class Person:
    def __init__(self, name, age, gender, preferences):
        self.name = name
        self.age = age
        self.gender = gender
        self.preferences = preferences
        self.matched = False
        
def find_matches(people):
    matches = []
    for person in people:
        if not person.matched:
            for potential_match in people:
                if not potential_match.matched and person != potential_match:
                    if (person.preferences['gender'] == potential_match.gender and potential_match.preferences['gender'] == person.gender):
                        matches.append((person, potential_match))
                        person.matched = True
                        potential_match.matched = True
                        break
                    
    return matches

def main():
    # Define the list of people
    people = [
        Person("Alice", 25, "Female", {"gender": "Male"}),
        Person("Bob", 27, "Male", {"gender": "Female"}),
        Person("Charlie", 24, "Male", {"gender": "Female"}),
        Person("Diana", 23, "Female", {"gender": "Male"}),
        Person("Eve", 30, "Female", {"gender": "Female"}),
        Person("Frank", 29, "Male", {"gender": "Female"})
    ]
    
    # Find matches
    matches = find_matches(people)
    
    # Displa matches
    print("Matches found:")
    for match in matches:
        person1, person2 = match
        print(f"{person1.name} ({person1.gender}, {person1.age}) matched with {person2.name} ({person2.gender}, {person2.age})")
        
if __name__ == "__main__":
    main()