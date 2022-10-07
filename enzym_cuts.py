input_file = ......

def lees_inhoud(input_file):
    '''
    Here we will read the file and split the enzym from their sequence which we put in a separate list.
    :param input_file:
    :return list:
    '''
    list = [[],[]]
    with open(input_file) as file:
        read = True
        while read == True:
            regel = file.readline()

            if regel == '':
                read = False
            else:
                enzym, seq = regel.split()
                seq = seq.replace("^", "")
                list[0].append(enzym)
                list[1].append(seq)
                
        return list

def match(list):
    '''
    Here we will see what enzym cuts in the sequence and what the name of the enzym is. 
    :param list:
    :return sequentie, restrictie_enzym:
    '''
    sequentie = 'ACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCC'

    for i in range(len(list[1])):
        if list[1][i] in sequentie:
            restrictie_enzym = list[0][i]

    return sequentie, restrictie_enzym

def position(sequentie, list):
    '''
    Here we figure out the position where the enzym cuts.
    :param sequentie:
    :param list:
    :return positie:
    '''
    for i in list[1]:
        if i in sequentie:
            c = i
            positie = sequentie.find(c)
            
    return positie


def main():
    list = lees_inhoud(input_file)
    sequentie, restrictie_enzym = match(list)
    positie = position(sequentie, list)
    print('Het enzym dat knipt is', restrictie_enzym, 'op de positie', positie)
    print(sequentie)

main()
