def DNA_complem():
    """Returns the complementary DNA sequence for the provided DNA sequence in upper case."""

    string = input('Please input the DNA string that you want the complementary sequence for here. ')
    upper_str = string.upper()
    bases = ['A', 'T', 'C', 'G']
    result = ''
    for char in upper_str:
        if char in bases:
            if char == 'A':
                result += 'T'
            elif char == 'T':
                result += 'A'
            elif char == 'C':
                result += 'G'
            elif char == 'G':
                result += 'C'
    if result == '':
        return 'Wrong input type for DNA sequence. Please ensure that it is a string with characters A, T, C or G.'
    return result

print(DNA_complem())