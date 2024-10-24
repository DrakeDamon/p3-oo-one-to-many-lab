class Pet():
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner =owner
        Pet.all.append(self)

        if pet_type in self.__class__.PET_TYPES:
            return None
        else:
            raise Exception("Invalid pet type")

class Owner():
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise TypeError("Can only add Pet objects")
    

    def get_sorted_pets(self):
        owner_pets = self.pets()
           # Sort pets by their 'name' attribute
        sorted_pets = sorted(owner_pets, key=lambda pet: pet.name)

        # Return the sorted list of pets
        return sorted_pets
        