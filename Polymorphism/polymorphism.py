class Bird:
    def sound(self):
        print("Birds chirp!")

class Dog:
    def sound(self):
        print("Dogs bark!")

# Polymorphism in action
def make_sound(animal):
    animal.sound()

b = Bird()
d = Dog()

make_sound(b)  # Bird's sound
make_sound(d)  # Dog's sound
