import random
import string


class Robot:
    assigned_names = []
    letters = (string.ascii_uppercase) * 2
    digits = '0123456789'*3

    def __init__(self):
    	self.name = self._name()

    def _name(self):
    	ret = ''.join(random.sample(Robot.letters, 2) + random.sample(Robot.digits, 3))
    	if ret in Robot.assigned_names:
    		self._name()
    	else:
    		Robot.assigned_names.append(ret)
    		return ret
    
    def reset(self):
    	random.seed()
    	self.__init__()




