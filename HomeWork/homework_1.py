"""
Homework 01
DO NOT RENAME THIS FILE OR ANY DEFINITIONS!
Place this file in your github repo inside of a folder titled "Homework".
"""


# String Functions
def fast_complement(dna):
    dictionary = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    comps = list(dna)
    comps = [dictionary[i] for i in comps]
    return ''.join(comps)

print(fast_complement("TAGC"))

    # """
    # Uses a dictionary to convert a DNA sequence into the complement strand.  C <--> G,  T <--> A
    # :param dna: a string containing only the characters C, T, A, and G
    # :return: a string containing only the characters C, T, A, and G
    # """


def remove_interval(s, start, stop):

    string = s
    newstring = string[:start] + string[stop + 1:]
    return newstring

print(remove_interval("ABCDEFGHI", 2, 5))

    # """
    # Removes the interval of characters from a string or list inclusively, 0 based
    # EX: remove_intervals('ABCDEFGHI', 2, 5) will return 'ABGHI'.
    # :param s: a string
    # :param start: a non-negative integer
    # :param stop: a non-negative integer greater than the start integer.
    # :return: a string
    # """
    # return

def kmer_list(s, k):

    length = len(s) - k + 1
    kmerlist = []
    for i in range(length):
        kmer = s[i:i +k]
        kmerlist.append(kmer)
    return kmerlist

print(kmer_list("GATGAT",3))

    # """
    # Generates all kmers of size k for a string s and store them in a list
    # :param s: any string
    # :param k: any integer greater than zero
    # :return: a list of strings
    # """
    # return

def kmer_set(s, k):

    length = len(s) - k + 1
    kmerlist = []
    for i in range(length):
        kmer = s[i:i + k]
        if not (kmer in kmerlist):
         kmerlist.append(kmer)
    return kmerlist

print(kmer_set("GATGAT",3))

    # """
    # Generates all kmers of size k for a string s and store them in a set
    # :param s: any string
    # :param k: any integer greater than zero
    # :return: a set of strings
    # """
    # return

def kmer_dict(s, k):

    dictionary = {}
    noofkmers = len(s) - k + 1
    for i in range(noofkmers):
        kmer = s[i:i + k]
        if kmer not in dictionary:
            dictionary[kmer] = 0
        dictionary[kmer] += 1
    return dictionary

print(kmer_dict("GATGAT",3))

    # """
    # Generates all kmers of size k for a string s and store them in a dictionary with the
    # kmer(string) as the key and the number of occurances of the kmer as the value(int).
    # :param s: any string
    # :param k: any integer greater than zero
    # :return: a set of strings
    # """
    # return

# Reading Files
import os
def head(file_name):
    
        f = open(file_name)
        lines = f.readlines()
        print(lines[0])
        print(lines[1])
        print(lines[2])
        print(lines[3])
        print(lines[4])
        f.close()
        
head("/Users/rashmithareddy/Desktop/mysql.txt")


    # """
    # Prints the FIRST 10 lines of a file
    # :param file_name: a string
    # :return: None
    # """
    # return

def tail(file_name):

    f = open(file_name)
    lines = f.readlines()
    print(lines[-5])
    print(lines[-4])
    print(lines[-3])
    print(lines[-2])
    print(lines[-1])
    f.close()
    
tail("/Users/rashmithareddy/Desktop/mysql.txt")


    # """
    # Prints the LAST 10 lines of a file
    # :param file_name: a string
    # :return: None
    # """
    

def print_even(file_name):

    i = 1
    f = open(file_name)
    for line in f.readlines():
        if i % 2 == 0:
            print(line)
        i += 1

print_even("/Users/rashmithareddy/Desktop/mysql.txt")
    # """
    # Prints the even numbered lines of a file
    # :param file_name: a string
    # :return: None
    # """
    

def csv_list(file_name):

    csvlist = list()
    with open(file_name, 'r')  as f:
        rows = f.readlines()
        for row in rows:
            csvlist.append(row.split(','))
    return csvlist

print(csv_list("/Users/rashmithareddy/Desktop/mysql.csv"))
    
    # """
    # Read in a CSV file to a 2D array (In python it is a list of lists)
    # :param file_name: a string
    # :return: a list of lists
    # """

def get_csv_column(file_name, column):
    csvlist = list()
    with open(file_name, 'r')  as f:
        rows = f.readlines()
        for row in rows:
            csvlist.append(row.split(',')[column])
    return csvlist
print(get_csv_column("/Users/rashmithareddy/Desktop/mysql.csv", 0))


    # """
    # Reads in a CSV file and returns a list of values belonging to the column specified
    # :param file_name: a string
    # :param column: a positive integer
    # :return: a list
    # """
    
def fasta_seqs(file_name):
    list = []
    with open(file_name, 'r') as infile:
        text = infile.read()
        seqs = text.split('>')
        for seq in seqs:
            try:
                x = seq.split('\n', 1)
                header = x[0]
                sequence = x[1].replace('\n', '')
                list.append(sequence)


            except Exception as e:
                print('')
                

    return list
print(fasta_seqs('/Users/rashmithareddy/Desktop/test_files/proper_fasta.fasta'))


    # """
    # Reads in a FASTA file and returns a list of only the sequences
    # :param file_name: a string
    # :return: a list of strings
    # """


def fasta_headers(file_name):
    list = []
    with open(file_name, 'r') as infile:
        text = infile.read()
        seqs = text.split('>')
        for seq in seqs:
            try:
                x = seq.split('\n', 1)
                header = x[0]
                sequence = x[1].replace('\n', '')
                list.append(x[0])


            except Exception as e:
                print(e)
                # print(seq)


    return list
print(fasta_headers('/Users/rashmithareddy/Desktop/test_files/proper_fasta.fasta'))

    # """
    # Reads in a FASTA file and returns a list of only the headers (Lines that start with ">")
    # :param file_name: a string
    # :return: a list of strings
    # """
    # return

def fasta_dict(file_name):
    dict = {}
    with open(file_name, 'r') as infile:
        text = infile.read()
        seqs = text.split('>')
        for seq in seqs:
            try:
                x = seq.split('\n', 1)
                header = x[0]
                sequence = x[1].replace('\n', '')
                dict[header] = sequence

                # print(header, sequence)
            except Exception as e:
                print(e)
                print(seq)

    return dict
print(fasta_dict('/Users/rashmithareddy/Desktop/test_files/proper_fasta.fasta'))

    # """
    # Reads in a FASTA file and returns a dictionary of the format {header: sequence, ...}, where
    # the sequence headers are keys and the sequence is the value
    # :param file_name: a string
    # :return: a dictionary
    # """
    # return

def fastq_to_fasta(file_name, new_name=None):

    with open(file_name, 'r') as src :
        temp = src.read()
        newtemp = temp.replace('@','>')
        if new_name != None:
            f = open(new_name+'.fasta', 'w')
            f.write(newtemp)
        else:
            f = open(file_name.split('.')[0]+'.fasta', 'w')
            f.write(newtemp)


fastq_to_fasta('/Users/rashmithareddy/Desktop/test_files/proper_fastq.fastq',
                   'd_fasta')
fastq_to_fasta('/Users/rashmithareddy/Desktop/test_files/proper_fastq.fastq')


    # """
    # Reads in a FASTQ file and writes it to a new FASTA file. This definition should also
    # keep the same file name and change the extension to from .fastq to .fasta if new_name is not specified.
    # EX: fastq_to_fasta('ecoli.fastq') should write to a new file called ecoli.fasta
    # :param file_name: a string
    # :param new_name: a string
    # :return: None
    # """
    # return

# Transcription and Translation
def reverse_complement(dna):
    complement=""

    for i in dna:

        if i == "T":
            complement += "A"
        elif i == "A":
            complement += "T"
        elif i == "C":
            complement += "G"
        elif i == "G":
            complement += "C"
        else:
            return -1


    reversingcomplement = ""

    for i in complement:
     reversingcomplement = i + reversingcomplement
    return reversingcomplement

print(reverse_complement("ATGCATGC"))

    # """
    # Returns the strand of DNA that is the reverse complement of the sequence given
    # :param dna: a string containing only the characters C, T, A, and G
    # :return: a string containing only the characters C, T, A, and G
    # """
    # return

def transcribe(dna):
    rna = ""

    for i in dna:

        if i == "T":
            rna += "U"
        else:
            rna += i
    return rna


print(transcribe("CTAG"))

    # """
    # Transcribes a string of DNA into RNA
    # :param dna: a string containing only the characters C, T, A, and G
    # :return: a string containing only the characters C, U, A, and G
    # """


def translate(rna):
    RNA_CODON_TABLE = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
                       "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
                       "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
                       "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
                       "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
                       "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                       "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
                       "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                       "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
                       "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                       "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
                       "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                       "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
                       "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                       "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
                       "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
    string = ""
    for i in range(0, len(rna) - (3 + len(rna) % 3), 3):
        if RNA_CODON_TABLE[rna[i:i + 3]] == "*":
            break
        string += RNA_CODON_TABLE[rna[i:i + 3]]
    return string

print(translate("CUAGCUAGCUAGAUGGCCAUCUGAGAUCAAUAGUACCCGUAUUAACGGGUGAUGAUAGUAG"))
    # """
    # Translates the strand of RNA given into its amino acid composition.
    # DO NOT INCLUDE * IN YOUR RETURN STRING
    # :param rna: a string containing only the characters C, U, A, and G
    # :return: a string containing only the characters G, A, L, M, F, W, K, Q, E, S, P, V, I, C, Y, H, R, N, D, and T
    # """
    # RNA_CODON_TABLE = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    #        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    #        "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
    #        "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
    #        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    #        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    #        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    #        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    #        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    #        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    #        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    #        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    #        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    #        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    #        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    #        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
    # return

def reading_frames(dna):
    orflist= []

    orflist.append(dna)
    orflist.append(dna[1:-2])
    orflist.append(dna[2:-1])

    my_dictionary = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    dnas =  list(dna)
    dnas = [my_dictionary[i] for i in dnas]
    dna = ''.join(dnas)[::-1]

    orflist.append(dna)
    orflist.append(dna[1:-2])
    orflist.append(dna[2:-1])

    return orflist

print(reading_frames("CGCTACGTCTTACGCTGGAGCTCTCATGGATCGGTTCGGTAGGGCTCGATCACATCGCTAGCCAT"))

    # """
    # Generates a list of all 6 possible reading frames for a given strand of DNA
    # For the non-biologists: https://en.wikipedia.org/wiki/Open_reading_frame
    # :param dna: a string containing only the characters C, T, A, and G
    # :return: a list of 6 strings containing only C, T, A, and G
    # """
    # return

