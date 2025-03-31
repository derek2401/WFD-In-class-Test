class Pet:
    #A2
    def __init__(self, name, age, sex, petID, owner_name):
        
        self.name = name
        self.age = age
        self.sex = sex
        self.petID = petID
        self.owner_name = owner_name

    #A3
    def pet_details(self):
        print("\nPet Details In System:\n")
        print("Pet Name: ", self.name)
        print("Pet Age: ", self.age)
        print("Pet Sex: ", self.sex)
        print("Pet ID: ", self.petID)
        print("Owner Name: ", self.owner_name)

    #A4
    def update_name(self, new_name):
        self.name = new_name

    def update_age(self, new_age):
        self.age = new_age

    def update_sex(self, new_sex):
        self.sex = new_sex

    def update_petID(self, new_petID):
        self.petID = new_petID

    def update_owner_name(self, new_owner_name):
        self.owner_name = new_owner_name

#A5
class Dog(Pet):

    def __init__(self, name, age, sex, petID, owner_name, breed, weight):
        super().__init__(name, age, sex, petID, owner_name)
        self.breed = breed
        self.weight = weight

    #A6
    def pet_details(self):
        super().pet_details()
        print("Breed: ", self.breed)
        print("Weight(KG): ", self.weight)

    #A7
    def update_breed(self, new_breed):
        self.breed = new_breed

    def update_weight(self, new_weight):
        self.weight = new_weight

#A8
sys_pet = Pet("Spot", 6, "Male", "PID0121", "Derek Lattimore")

sys_dog = Dog("Fluffy", 2, "Female", "PID0122", "Derek Lattimore", "Labrador", 16)

#A9
sys_pet.pet_details()
sys_dog.pet_details()

#A10
