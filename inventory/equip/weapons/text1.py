import json
import os
from uuid import uuid4

class Person:
    def __init__(self, name, age, city):
        self.id = str(uuid4())  # Unique identifier for each person
        self.name = name
        self.age = age
        self.city = city
    
    def to_dict(self):
        """Convert Person object to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "city": self.city
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create Person object from dictionary."""
        return cls(data["name"], data["age"], data["city"])

class PersonManager:
    def __init__(self, filename):
        self.filename = filename
        self.persons = self.load_persons()

    def load_persons(self):
        """Load persons from JSON file."""
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as file:
            data = json.load(file)
            return [Person.from_dict(person) for person in data]

    def save_persons(self):
        """Save persons to JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([person.to_dict() for person in self.persons], file, indent=4)

    def add_person(self, name, age, city):
        """Add a new person and save to file."""
        person = Person(name, age, city)
        self.persons.append(person)
        self.save_persons()
        return person

    def search_persons(self, key, value):
        """Search for persons by key-value pair."""
        return [person for person in self.persons if hasattr(person, key) and getattr(person, key) == value]

# Example usage
if __name__ == "__main__":
    # Initialize manager with JSON file
    manager = PersonManager("persons.json")

    # Add some initial persons
    manager.add_person("John", 30, "New York")
    manager.add_person("Alice", 25, "Los Angeles")
    manager.add_person("Bob", 35, "New York")
    manager.add_person("Emma", 28, "Chicago")

    # Print all persons
    print("All persons:")
    for person in manager.persons:
        print(person.to_dict())

    # Search for persons in New York
    ny_persons = manager.search_persons("city", "New York")
    print("\nPersons in New York:")
    for person in ny_persons:
        print(person.to_dict())

    # Search for persons with age 25
    age_25_persons = manager.search_persons("age", 25)
    print("\nPersons with age 25:")
    for person in age_25_persons:
        print(person.to_dict())

    # Add a new person
    manager.add_person("Sarah", 27, "Boston")
    print("\nAfter adding Sarah:")
    for person in manager.persons:
        print(person.to_dict())
