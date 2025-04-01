# Mocking email addresses with accurate demo|test|fake t/s-level domain names
# 
# SEE: RFC 2606 and RFC 6761
# 

import random
from  mocky.generic import Generic
class Email:

    
    tlds = ['.test', '.example','.invalid', '.localhost']
    slds = ['example.com', 'example.net', 'example.org']
    
    def get_mail_prf(fullname:str, mode:int=5):
        """ Generating mail address prefix (part b4 '@')
            from given full name ('jane Foe')
            TODO: Handle mid names, midding spaces error handling in general etc.
        """
        tmp = fullname.split(' ')
        
        first, last = fullname.split(' ')
        
        if mode == 5: #J.Foe
            return first[0:1] + '.' + last
        elif mode == 4: #Foe.Jane
            return last + '.' + first
        elif mode == 3: #janefoe
            return first + last
        elif mode == 2: #jfoe
            return first[0:1] + last
        elif mode == 1: #foejane
            return last + first
        else: #jane.f
            return first + '.' + last[0:1]

    
        
    def get_random_domain_type(self, which:int=666):
        if type != 666:
            pass
        else:
             number = random.randrange(100)
             if number > 66: # tld
                 return Generic.rnd_element(self.tlds)
             else: # sld
                 return Generic.rnd_element(self.slds)
             