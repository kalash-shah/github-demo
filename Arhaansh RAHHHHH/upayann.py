# upayan small child i love ayman too <3

import random
import time

class Upayan:
    def __init__(self, name):
        self.name = name
        print("Initializing tiny child...")

    def greet(self):
        return f"Hello, {self.name}! Upayan Mazumdar babbababab!"

    def chaos(self):
        phrases = [
            "AYMANNNNN",
            "Giving birth to upayan",
            "Upayan vs child.",
            "Upayan gayness increasing..",
            "Warning: Too much aura detected."
        ]
        print(random.choice(phrases))

u = Upayan("Upayan")
print(u.greet())
u.chaos()
