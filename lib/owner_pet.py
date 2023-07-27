class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=""):
        self.pet_type = pet_type
        self.name = name
        self.owner = owner
        self.add_to_all(self)
    def get_pet(self):
        return self._pet_type
    
    def set_pet(self, pet_type):
        if (pet_type in self.PET_TYPES):
            self._pet_type = pet_type
        else:
            raise Exception

    pet_type = property(get_pet, set_pet)

    @classmethod
    def add_to_all(cls, pet):
        cls.all.append(pet)
    pass

class Owner:

    def __init__(self, name):
        self.name = name
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception

    def get_sorted_pets(self):
        return sorted(self.pets(), key = lambda instance: instance.name)
        pass
    
    pass