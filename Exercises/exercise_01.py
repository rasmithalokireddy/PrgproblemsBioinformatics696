"""
Exercise 1
Place this script inside a new folder in your github repository called "Exercises".
This will be the directory for all of your in-class exercises this semester.

By the end of class on Thursday 1/25, students should have:
    - Created a private github repo for this class
    - Added their information to this sheet:
        https://docs.google.com/spreadsheets/d/1EKNYOqTnxelmBT4jqotRbUer5eVvWYM9RloN5doScyo/edit?usp=sharing
    - Added my github account (kylelevi) as a collaborator for their private repository
    - Completed these definitions and pushed this script to a folder called "Exercises" in their repo

"""
def hello():
    print("Hello World")


def percent_decimal(i):

    if i<1:

       answer = i * 100
       print ("decimal to percentage is " , answer)

    else:
       answer = i/100
       print("percent to decimal is" , answer)

# def percent_decimal(i):
#     """
#     Converts a percentage to a decimal or a decimal to a percentage depending on the input i
#     :param i: a float between 0 and 100
#     :return: a float between 0 and 100
#     """
#     return

def exponent(integer, power):

    # for x in range (0 , power ):
        y= 1
        for x in range(0, power):
          y= y * integer

        print (y)


    # """
    # Using a loop (no imports!), raise the integer given to the power provided. (integer^power)
    # :param integer: a positive, non zero, integer
    # :param power: a positive, non zero, integer
    # :return: an integer
    # """
    # return

def complement(dna):

    if dna == 'C' :
        print ('G')
    elif dna == 'G' :
        print('C')
    elif dna == 'A' :
        print('T')
    elif dna == 'T' :
        print('A')
    else: return -1





    """
    Returns the complement strand of DNA to the input.  C <--> G,  A <--> T
    :param dna: String containing only C, T, A, and G
    :return: String containing only C, T, A, and G
    """
    return

hello()
percent_decimal(0.5)
exponent(2, 2)
complement('F')