#!/usr/bin/env python3
__author__ = "Kerti Alev"
__copyright__ = "Copyright 2018, minufirma"
__credits__ = ["Kerti Alev"]
__version__ = "0.2"
__email__ = "spetsk@gmail.com"

import random

RNA_INTERMEDIATE_CODON_TABLE = {
'CUU': 'Leu', 'ACA': 'Thr', 'AAA': 'Lys', 'AUC': 'Ile', 'AAC': 'Asn', 'AUA': 'Ile',
'AGG': 'Arg', 'CCU': 'Pro', 'ACU': 'Thr', 'AGC': 'Ser', 'AAG': 'Lys', 'AGA': 'Arg', 'CAU': 'His',
'AAU': 'Asn', 'AUU': 'Ile', 'CUG': 'Leu', 'CUA': 'Leu', 'CUC': 'Leu', 'CAC': 'His', 'UGG': 'Trp',
'CAA': 'Gln', 'AGU': 'Ser', 'CCA': 'Pro', 'CCG': 'Pro', 'CCC': 'Pro', 'UAU': 'Tyr', 'GGU': 'Gly',
'UGU': 'Cys', 'CGA': 'Arg', 'CAG': 'Gln', 'UCU': 'Ser', 'GAU': 'Asp', 'CGG': 'Arg', 'UUU': 'Phe',
'UGC': 'Cys', 'GGG': 'Gly', 'GGA': 'Gly', 'ACG': 'Thr', 'UAC': 'Tyr',
'UUC': 'Phe', 'UCG': 'Ser', 'UUA': 'Leu', 'UUG': 'Leu', 'UCC': 'Ser', 'ACC': 'Thr', 'UCA': 'Ser',
'GCA': 'Ala', 'GUA': 'Val', 'GCC': 'Ala', 'GUC': 'Val', 'GGC': 'Gly', 'GCG': 'Ala', 'GUG': 'Val',
'GAG': 'Glu', 'GUU': 'Val', 'GCU': 'Ala', 'GAC': 'Asp', 'CGU': 'Arg', 'GAA': 'Glu', 
'CGC': 'Arg'
}

def generateRNA(intermediate_codons):
    
    # apply start codon
    rna_string = 'AUG';
    
    # apply n valid intermediate codons
    for i in range(intermediate_codons):
        rna_string += random.choice(RNA_INTERMEDIATE_CODON_TABLE.keys())
        
    # apply stop codon
    rna_string += random.choice(['UGA', 'UAG', 'UAA'])
    
    return rna_string



def convertToDNA(rna):

    return rna.replace('U', 'T')

def main():
	codons = 7
	rna = generateRNA(codons-2)
	print 'Random RNA with ' + str(codons) + ' codons: ' + rna
	dna = convertToDNA(rna)
	print 'The above as DNA: ' + dna

if __name__ == "__main__":
	main()



