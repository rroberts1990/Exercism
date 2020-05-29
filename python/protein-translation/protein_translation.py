
protein_dict = {'Methionine':'AUG', 'Phenylalanine':['UUU', 'UUC'], 'Leucine':['UUA', 'UUG'], \
'Serine':['UCU', 'UCC', 'UCA', 'UCG'], 'Tyrosine':['UAU', 'UAC'], 'Cysteine':['UGU', 'UGC'], \
'Tryptophan':'UGG', 'Stop':['UAA', 'UAG', 'UGA']}


def proteins(strand):
    res = []
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    for item in codons:
    	for key,values in protein_dict.items():
    		if item in values:
    			if key == 'Stop':
    				return res
    			else: 
    				res.append(key)
    return res