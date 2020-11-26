from typing import List

def is_valid(isbn: str) -> bool:
    parsed_isbn = parse_isbn(isbn)
    if len(parsed_isbn) != 10:
    	return False
    return sum(parsed_isbn) % 11 == 0


def parse_isbn(isbn: str):
	try:
		l = [i for i in isbn if i.isalnum()][::-1]
		if l[0] == 'X':
			del l[0]
			['10'].extend(l)
	except:
		return []
	return [(index+1)*int(val) for index, val in enumerate(l)]


