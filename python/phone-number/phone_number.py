

class PhoneNumber:
    def __init__(self, number):
        self.number = self.clean_number(number)

    def clean_number(self, number):
    	cleaned = [n for n in number if n.isnumeric()]
    	l = len(cleaned)
    	if not self.is_valid(l, cleaned):
    		raise ValueError("invalid number")
    	if l == 10:
    		return ''.join(cleaned)
    	else:
    		return ''.join(cleaned[1:])

    def is_valid(self, length, number):
        if not length in [10,11]:
            return False
        if length == 11:
            if number[0] != '1':
                return False
            number = number[1:]
        if int(number[0]) < 2 or int(number[3]) < 2:
            return False
        else:
            return True

    @property
    def area_code(self):
    	return self.number[:3]

    @property
    def exchange_code(self):
    	return self.number[3:6]

    @property
    def subscriber_number(self):
    	return self.number[6:]

    def pretty(self):
    	return f"({self.area_code}) {self.exchange_code}-{self.subscriber_number}"






    