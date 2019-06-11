# Import String and Random methods
import string , random

# Define letters and numbers choices
letters = string.ascii_uppercase
numbers = string.digits
    
usedNames = []

class Robot(object):


    def __init__(self):
        self.name = self.reset()
        usedNames.append(self.name)

    def reset(self):
        # define using random.choices 'Return list with replacement' so possible to get BB or 111
        name_chars = random.choices(letters) + random.choices(letters)
        name_numbers = random.choices(numbers) + random.choices(numbers) + random.choices(numbers)            
        
        nameChoice = name_chars + name_numbers

        if nameChoice in usedNames :
            self.reset()
        
        return nameChoice
