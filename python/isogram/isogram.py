def is_isogram(string):
    string = [s.lower() for s in string if s.isalpha()]
    return len(set(string)) == len(string)
