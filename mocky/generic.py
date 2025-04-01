# Generic (mainly random) functions generating mock data
# 

import random

class Generic:
    
    def __init__(self):
        pass
    
    def rnd_element(cls, data:list):
        """ Getting random element from given list """
        return data[random.randrange(len(data))]
    
    