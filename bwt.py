#last = list(seq[-1])
#seq = seq[:-1]
#seq[0] = last
#seq = list(seq[-1]) + seq[:-1]
#print(last)
#print(seq)

def permutation(seq) :
    last = []
    transf = []
    seq_new = []
    for i in range(len(seq)) :
        last = list(seq[-i:]) + seq[:-i]
        seq_new.append(last)
        #print(last)
    return seq_new
    #print(last)

def bwt(sequence) :
    transf = []
    sequence.sort()
    for seq in sequence :
        transf.append(seq[-1])
    return transf

def find_original(sequence, bwt_seq) :
    
    col_1 = []
    dico_col1 = {}
    P = []
    for seq in sequence :
        col_1.append(seq[0])

    for index, letter in enumerate(col_1):
        if letter not in dico_col1 :
            dico_col1[letter] = index
 
        if bwt_seq[index]  not in bwt_seq[:index] :
            P.append(0)
        #elif bwt_seq[index] in bwt_seq[:index] :
        else :
            #P.append(bwt_seq[:index].count(letter))
    
            P.append(bwt_seq[:index].count(bwt_seq[index]))

    return P,dico_col1 
'''
def posbwt(bwtseq, N, P) :
    i = len(seq) - 1
    pos = [-1] * len(bwtseq)
    j = 0
    while bwtseq[j] != '$' :
        pos[j] = i
        j = N[bwtseq[j]] + P[j]
        i -= 1
    return pos
'''



'''
    for occ1, occ2 in col_1, bwt_seq :
        if occ1 not in dico_col1 :
            dico_col1[occ1] = 1
        else :
            dico_col1[occ1] += 1
    return dico_col1
'''



if __name__ == "__main__" :
    seq = ['A', 'T', 'A' , 'T' , 'C' , 'G' , 'T' , '$']
    perm = permutation(seq)
    #print(perm)
    bwt_seq = bwt(perm)
    print("Original is {} and bwt is {}".format(seq, bwt_seq))
    #print(bwt_seq)
    P_list, dico_1 = find_original(perm, bwt_seq)
