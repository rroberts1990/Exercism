rain_dict = {
'3' : 'Pling',
'5' : 'Plang',
'7' : 'Plong'
}

def convert(number):
    res = ''
    for n, sound in rain_dict.items():
        if number%int(n) == 0:
            res += sound
    if len(res) == 0:
        return str(number)
    else:
        return res

