def slices(series, length):
	l = len(series)
	if l < 1 or length < 1 or length > l:
		raise ValueError("bad values")
	return [series[i:i+length] for i in range(l) if len(series[i:i+length]) == length]

