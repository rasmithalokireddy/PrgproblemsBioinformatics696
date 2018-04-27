"""
exercise_03
2/8/2018

For this Exercise you will write one definition that will take in the name of a
directory as a string, and return a dictionary containing every sequence in every FASTA file where
the sequence header is the key and the DNA sequences are values.

Your definition will be tested with improperly formatted FASTA files and should handle the following cases:
    1) If there are extra new line characters, or empty lines, your program should still process sequences normally
    2) If a duplicate header exists between two entries your definition should check to see if the sequences are the same
        * If the headers and sequences are identical, your program should print a message that "a duplicate entry exists
          for <header>" and continue normally.
        * If the only the headers match, you should print a message that "duplicate headers with non-identical
          sequences were found for <header>" and neither entry should be added in the dictionary.
          (your print statements don't need to be identical to what I have written here)
    3) If a file in the directory is not a fasta file, your program should not open it.
    4) If a sequence contains characters that are not A, C, G, or T, then it should not be added to the dictionary.

If your program is working correctly, the dictionary should only contain the 4 "good sequence"s in the test folder.


The following syntax may be helpful:

# deleting from a dictionary
del my_dictionary[key]

# printing and formatting a string
x = 'my_variable'
print('Error related to variable: {}'.format(x))

# checking your final dictionary by printing out key, value pairs
for key, value in my_dictionary.items():
    print('Key is: {}\tValue is: {}'.format(key, value))

"""

import os
import re

def fasta_folder_to_dict(folder_path):

    fasta_dict = {}
    allowedcharacters = re.compile(r'[^ACTG]')

    for filename in os.listdir(folder_path):
        if not filename.endswith('.fasta'):
            continue
        with open(folder_path +'/'+ filename,'r') as infile:

            entries=infile.read()
            seqs = entries.split (">")
            for entry in seqs[1:]:
                try:
                  x = entry.split('\n',1)
                  header = x[0]
                  sequence= x[1].replace('\n','')
                  if header in fasta_dict:
                      if fasta_dict[header]==sequence:
                          print("a duplicate entry exists for" + header )
                          continue
                      else:
                          print("duplicate headers with non identical sequences were found for" + header)
                          del new_dict[header]
                          continue
                  if sequence=="":
                      print("empty sequence for" +header)
                      continue
                  if not bool(allowedcharacters.search(sequence)):
                      fasta_dict[header]=sequence
                  else:
                      print("protein for" + header)

                except:
                  print("error")
                  continue
    for keys,values in fasta_dict.items():
        print(keys,"-->",values)


    return


    #     if header in fasta_dict and seq== fasta_dict[header]:
    #         print("Duplicate header and sequence for {}".format(header))
    #
    #     elif header in fasta_dict:
    #         print("duplicate header is {}, but non matching sequence". format(header))
    #         del fasta_dict[header]
    #         continue
    #
    #     # unallowed_charactes=''.join([allowedcharacters[x] if x in allowedcharacters else x for x in fasta_dict])
    #     # if(len(unallowed_charactes))>0:
    #     #     print("sequence for entry {} contains unallowed characters : {}".format(header,unallowed_charactes))
    #     #     continue
    #
    #     fasta_dict[header]=seq
    # return fasta_dict

print(fasta_folder_to_dict('/Users/rashmithareddy/Desktop/test/'))
    # """
    # Constructs a dictionary of all of the FASTA formatted entries from a folder containing FASTA files.
    # :param folder_path: string
    # :return: dictionary
    # """
    # return