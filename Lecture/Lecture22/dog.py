"""
File: dog.py
------------
Defines a Dog class.
"""

class Dog:

    def __init__(self, breed):
        """
        Constructor for Dog.  We set the breed of the dog when
        the dog object is created.
        """
        print('A new dog is born')
        self.times_barked = 0
        self.breed = breed

    def bark(self):
        """
        The kind of bark the dog makes depends on its breed.
        """
        if self.breed == 'pomeranian':
            print('yip')
        else:
            print('woof')
        self.times_barked += 1
