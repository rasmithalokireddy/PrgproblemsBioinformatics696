"""
exercise_07  Regular Expressions

"""
test_protein = """MHMWSFMMRFRKGGKPYHTVADARGPYDNGHLHKTYYLKNLMYYTVGMWVKEQLCCRHEP
RSFLLAFIWSWCLAGVYRLTHRGSGPEMNRVVMFQYQDECSYLLQVTDVAYCNEQAWYAR
FWSCIASSFEMSSHELHTQHYYTLTGSVDWNMYVQNGVWAHGIACSMTDNQDGSCRQPIM
DTDYVDTHDHEKRYRQRGLCSTPCNDQFPGYEFPTVHGTMAWISGEMMCASGYKPYNFKH
GEFSPKSIWEWQLFACCCCGKTEWSNVMIFMVVEIEIFASKSNEENWSGMNIIEDDDPQH
HFKNIYRKYLDFQFYLIYGGYRMGFLHHRDSMINALVCKTGRWQQMHSFLKCDRRCKYLI
NIYADGKWYDNWSKVEDKVLDRGIRFLQSWNATEMVNSSMYRKPFYQSQYAPRFCWETFC
QHEIYFHQEYASNCKARCGSYQSSAQSATLAIKYSELYQGFWGTSEWGHHQLFIHRWGVQ
IYQVKLHDSIMRPWIDWSRKCKWLLHRLHCDIELVPIHWEHKPQRVSFYYFKAMTDVLRE
ICWSAQYHVVIQKFAFITMAWICTFYVHMYPSLDRHGSVTGIAWKLSGQWTGQEAYSKLN
TEKETITEHNCPRVANIIVDCLEHEQVEMRMKRCHTWMVEVMKYPEQKFLWQCEHFRALY
GLVGHNCPIKAWVRWIPHMEQKVCSYFRRAYFMMLKNPMSRDSVCRREMEYDMAISRMPY
GDCHAVGKWLPYFLNRYTPWWVWIWMAPFQGNRFFYHYKKDWRHCGNYLGGLCVLMTFWH
HPIYVPCPKTKADFKQACCYCGKTRQACTDENMDTQRQKFQALHQARICQPYTVRNMSIQ
CGKNPIKANHNNNVRRPTMHICNLPAMTRRFVYTPFMKLKQSLGHDKWHIPEIQPYMDFT
YHSVWIHQPHMNSCAACTGTVALALALALHYYTHPIQGEYIIYTSCDARYKSQKQEDIYQ
ITSTCLEFSSKFKAQMMGTTWEIAGMNFCKVIETSCRQKI""".replace('\n', '')


import re
def kinase2(string):

    """
    Using re.findall(), return a list of matched motifs to the Casein Kinase II phosphorylation site
    in the string.  The motif is:
    a S or T
    followed by any 2 Amino Acids
    followed by a D or E
    :param string: the protein sequence to be searched
    :return: a list of strings
    """
    return re.findall("[ST]..[DE]",string)

print(kinase2(test_protein))
# #['TVAD', 'SGPE', 'SSFE', 'SSHE', 'SMTD', 'SIWE', 'SNEE', 'SKVE', 'TGQE', 'TEKE', 'TITE', 'TKAD', 'TSCD', 'TCLE', 'TTWE']


def atp_binding_site(string):

    """
    Using re.findall(), return a list of matched motifs to the ATP binding motif in the string.
    the ATP binding motif is:
    An "A" or "G"
    followed by any 4 Amino Acids
    followed by a "G"
    followed by a "K"
    followed by a "S" or "T"
    :param string: the protein sequence to be searched
    :return: a list of strings
    """
    return re.findall("[AG]....[G][K][ST]", string)

print(atp_binding_site(test_protein))
# # ['ACCCCGKT', 'ACCYCGKT']

def atp_variable_region(string):

    """
    Using re.search() and a capture group, return the 4 variable amino acids within
    the first matched ATP binding motif.  EX:
    If the matched motif is ACCCCGKS, this definition should return "CCCC"
    the ATP binding motif is:
    An "A" or "G"
    followed by any 4 Amino Acids
    followed by a "G"
    followed by a "K"
    followed by a "S" or "T"
    :param string: the protein sequence to be searched
    :return: a strings
    """
    return re.search("[AG](....)[G][K][ST]", string).group(1)

print(atp_variable_region(test_protein))
# #CCCC

def atp_start_pos(string):
    """
    Using re.search(), find the start position of the first match to the ATP binding site motif.
    the ATP binding motif is:
    An "A" or "G"
    followed by any 4 Amino Acids
    followed by a "G"
    followed by a "K"
    followed by a "S" or "T"
    :param string: the protein sequence to be searched
    :return: int
    """
    return re.search("[AG]....[G][K][ST]", string).start()

print(atp_start_pos(test_protein))
# # 254

def zinc_finger(string):

    """
    Using re.findall(), return a list of matched motifs to the zing finger domain
    in the string.  The motif is:
    a C
    followed by 2 to 4 of any Amino Acid
    followed by a C
    followed by 3 of any Amino Acid
    followed by a single L, I, V, M, F, Y, W, or C
    followed by any 8 Amino Acids
    followed by a single H
    followed by 3 to 5 of any Amino Acid
    followed by a single H
    :param string: the protein sequence to be searched
    :return: a list of strings
    """
    return re.findall("[C].{2,3}...[L, I, V, M, F, Y, W, C]........[H].{3,5}[H]", string)

print(zinc_finger(test_protein))
# # ['CAACTGTVALALALALHYYTH']