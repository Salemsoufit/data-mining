import pandas as pd
from apyori import apriori


def apriori_function(x, trans):
    regle_dassociation = apriori(transactions=trans, min_support=x,
                                 min_confidence=0.2, min_lift=2, min_length=1, max_length=4)
    resultats_dassociation = list(regle_dassociation)
    return list(resultats_dassociation)

# FONCTION D'AFFICHAGE


def inspect(output):
    lhs = [tuple(result[2][0][0])[0] for result in output]
    rhs = [tuple(result[2][0][1])[0] for result in output]
    support = [result[1] for result in output]
    confidence = [result[2][0][2] for result in output]
    lift = [result[2][0][3] for result in output]
    return list(zip(lhs, rhs, support, confidence, lift))


def apriori_for_csv(file_name):
    data = pd.read_csv(file_name, header=None)
    trans = []
    # REPLISSAGE DE LA LISTE DES LISTES
    for i in range(0, len(data)):
        trans.append([str(data.values[i, j]) for j in range(0, 4)])
    results = apriori_function(0.001, trans)
    return pd.DataFrame(inspect(results), columns=['Left_Hand_Side', 'Right_Hand_Side', 'Support', 'Confidence', 'Lift'])

def getCSVFromArff(fileName):
	with open(fileName, 'r') as fin :
		data = fin.read().splitlines(True)
	i = 0
	cols = []
	for line in data:
		line = line.lower()
		if ('@data' in line):
			i+= 1
			break
		else:
			#print line
			i+= 1
			if (line.startswith('@attribute')):
				if('{' in line):
					cols.append(line[11:line.index('{')-1])
				else:
					cols.append(line[11:line.index(' ', 11)])
	headers = ",".join(cols)
	with open(fileName[0: fileName.rfind('.')] + '.csv', 'w') as fout:
		fout.write(headers)
		fout.write('\n')
		fout.writelines(data[i:])
