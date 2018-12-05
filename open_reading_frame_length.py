f = open('dna2.fasta', 'r')

def record_count(f):
    '''Returns the number of sequences in a file'''
    f = open('dna2.fasta', 'r')
    counter = 0
    for line in f:
        if '>' in line:
            counter += 1
    print(counter)

def dict_of_sequences(f):
    '''Generates a dictionary with id of sequence as a key and sequence itself 
    as a value. Contains an inner function that prints out longest and shortest 
    sequences in a given file'''
    #f = open(input(), 'r')
    seqs = {}
    for line in f:
        line = line.rstrip()
        if line[0] == '>':
            words = line.split()
            name = words[0][1:]
            seqs[name] = ''
        else:
            seqs[name] = seqs[name] + line
    #return seqs
    #print(seqs)
    def len_of_seqs(seqs):
        seqs_len = {}
        for i in seqs:
            seqs_len[i] = len(seqs[i])
        #print('longest sequence:', max(seqs_len.values()))
        #print('shortest sequence:', min(seqs_len.values()))
        for sequence, length in seqs_len.items():
            if length == max(seqs_len.values()):
                print('longest sequences:', sequence, length)
        for sequence, length in seqs_len.items():
            if length == min(seqs_len.values()):
                print('shortest sequences:', sequence, length)
    len_of_seqs(seqs)
 
    def orf_start_gen(seq):
        '''A program that returns a list of indices corresponding to the 
        first base of the start codons'''
        orf_start = []
        for i in range(len(seq) - 2):
            if seq[i] == 'A' and seq[i+1]+seq[i+2] == 'TG':
                orf_start.append(i)
        return orf_start        
    #a list containing stop codons    
    stop_codon_list = ['TAA','TAG', 'TGA']
    
    def find_a_codon(seq, start, codon):
        '''A function that returns an index which corresponds to the first base 
        of a given codon'''
        for i in range(start, len(seq)-2, 3):
            if seq[i:i+3]==codon:
                return i
                    
    def find_stop_codon(seq, start):
        '''Returns an index of the first base of the closest stop codon, 
        returns None of there is no stop codon'''
        orf_ends = []
        for stopCodon in stop_codon_list:
            pos = find_a_codon(seq, start, stopCodon)
            if pos != None:
                orf_ends.append(pos)
        if len(orf_ends)>0:
            return min(orf_ends)
        else:
            return None
    
    def findORFs(seq):
        '''Returns a list of tuples with two integers, where the first integer
        corresponds to the beginning of the start codon and the second integer 
        corresponds to the beginning of a stop codon'''
        compL = []
        startPos = orf_start_gen(seq)
        for i in startPos:
            stopPos = find_stop_codon(seq, i)
            compL.append((i, stopPos))
        return compL       
    seqs_orfs = {} 
    for key, value in seqs.items():
        seqs_orfs[key] = findORFs(value)   
    return seqs_orfs      


def longest_orf(lb):
    diff = {}
    
    for key, value in lb.items():
        for k in range(len(lb.values())):
            vals = []
            for j in range(len(value)):
                
                if None not in value[j]:
                    vals.append(value[j][1] - value[j][0])
                else:
                    vals.append(0)
            diff[key] = vals
    return diff

ac = longest_orf(dict_of_sequences(f))
def get_max_val():
    '''gets the max value of the ORF in ac dictionary'''
    max_vals = []
    for listik in ac.values():
        max_vals.append(max(listik))
    print(max(max_vals))