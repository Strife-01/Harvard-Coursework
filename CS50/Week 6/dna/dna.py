import csv
import sys


def main():

    # TODO: Check for command-line usage
    cla = sys.argv
    if len(cla) != 3 :
        print('Usage python dna.py database_csv sequence_txt')
        quit(1)

    # TODO: Read database file into a variable
    db_name = cla[1]
    try :
        db_hand = open(db_name)
        print(f"{db_name} opened successfully")
    except :
        print(f"Can't open {db_name}")
        quit(2)

    dna_seq_name = cla[2]
    try :
        dna_seq_hand = open(dna_seq_name)
        print(f"{dna_seq_name} opened successfully")
    except :
        print(f"Can't open {dna_seq_name}")
        quit(3)
    
    # TODO: Read DNA sequence file into a variable
    try :
        dna = dna_seq_hand.read()
        print(f"Successfully loaded {dna_seq_name} into memory")
    except :
        print(f"Can't load {dna_seq_name} into memory")
        quit(4)
    
    rows = list()
    try :
        db = csv.DictReader(db_hand)
        print(f"Successfully loaded {db_name} into memory")
    except :
        print(f"Can't load {db_name} into memory")
        quit(5)

    for row in db :
        rows.append(row)

    # TODO: Find longest match of each STR in DNA sequence
    index = 0
    dna_dict = dict()
    for dna_seq, dna_nr in row.items() :
        if index > 0 :
            number_times = longest_match(dna, dna_seq)
            dna_dict[dna_seq] = number_times
        index += 1

    # TODO: Check database for matching profiles
    match = None
    for row in rows :
        found = True
        index = 0
        for dna_seq, dna_app in row.items() :
            if index > 0 :
                if dna_dict[dna_seq] != int(dna_app) : 
                    found = False
                    break
            index += 1
        if found == True : 
            for value in row.values() :
                match = value
                break

    if match != None : print(match)
    else : print('No match')
    
    db_hand.close()
    dna_seq_hand.close()
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
