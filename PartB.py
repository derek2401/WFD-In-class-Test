#B2
import unittest
from PartA import Pet, Dog

class TestInstances(unittest.Testcase):
    def test_pet_instance(self):
        pet = Pet("Fido", 4, "Male", "PID0167", "John Smith")
        self.assertIsInstance(pet, Pet)

    def test_dog_instance(self):
        dog = Dog("Ruby", 11, "Female", "PID0232", "Tim Rivers", "German Shepherd", 22)
        self.assertIsInstance(dog, Pet)
        self.assertIsInstance(dog, Dog)

    #B3
    def test_pet_not_instance(self):
        not_pet = "Not pet"
        self.assertNotIsInstance(not_pet, Pet)

    def test_dog_not_instance(self):
        not_dog = "Not dog"
        self.assertNotIsInstance(not_dog, Pet)
        self.assertNotIsInstance(not_dog, Dog)

#B4



#B5



#B6
unittest.main()


