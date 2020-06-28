import re

def find_longest_sequence_of_1(binary):
    sequences_of_1 = re.findall(r'(1*)', str(binary))
    longest_sequence = max([len(sequence) for sequence in sequences_of_1])
    print(longest_sequence)
    
if __name__ == '__main__':
    n = bin(int(input()))

    find_longest_sequence_of_1(n)
