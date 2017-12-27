def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    
    return len (dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    countt = 0
    for char in dna:
        if char == nucleotide:
            countt = countt + 1
    return countt
 

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1


def is_valid_sequence (seq):
    
    """(str) -> bool
    
    Return if the sequence is a valid DNA sequence.
    
    >>>is_valid_sequence ('ATCG')
    True
    >>>is_valid_sequence ('ATCGMC')
    Flase
    >>>is_valid_sequence ('ATCGGc')
    False
    
    """
    nonvalidch = 0
    for char in seq:
        if char not in 'AGCT':
            nonvalidch= nonvalidch + 1
    return nonvalidch == 0

def insert_sequnce (seq1, seq2, ind):
    
    """(str,str,int) -> int
    
    Inserts seq2 inside seq1 i the the provided index. 
    
    pre-condition: seq1 and aeq2 must be valid DNA sequences.
    
    >>>insert_sequnce ('ATGCC', 'AT', 3)
    'ATGATCC'
    >>>insert_sequnce ('ATAT', 'CG', 0)
    'CGATAT'
    
    """
    return seq1[:ind] + seq2 + seq1[ind:]

def get_complement (s):
    
    """ (str) -> str
    
    Retrun the corresponding complementary of single charachters.
    
    Pre-condition: the s must be a vlid DNA charachter. 
    
    >>>get_complement ('A')
    'T'
    >>>get_complement ('T')
    'A'
    >>>get_complement ('C')
    'G'
    >>>get_complement ('G')
    'C'
    
    """
    for char in s:
        if char == 'A':
            return 'T'
        elif char == 'T':
            return 'A'
        elif char == 'G':
            return 'C'
        elif char == 'C':
            return 'G'
        
    
def   get_complementary_sequence (seq):  
    
    """(str)-> str
    
    Return the corresponding complementary sequence
    of input sequence. 
    
    Pre-condition: the seq must be a vlid DNA sequence. 

    >>>get_complementary_sequence ('ATCG')
    'TAGC'
    >>>>>>get_complementary_sequence ('ATTCGGA')
    'TAAGCCT'
    
    """
    new_seq = ''
    for char in seq:
        compel = get_complement(char)
        new_seq = new_seq + compel
        
        
    return new_seq 
    
    

        
            
        
        
            
     
    
        
        
    
    
    
