def aDNA_complem(input):
    """Returns the complementary DNA sequence for the provided DNA sequence in upper case."""

    try:
        inp_up = input.upper()
    except AttributeError:
        print('Please input characters A, T, C or G.')
        return

    bases = ['A', 'T', 'C', 'G']

    check = set(inp_up).issubset(bases)

    if not check:
        print('Please ensure that the string only has characters A, T, C or G.')
    else:
        result = ''
        for char in inp_up:
            if char in bases:
                if char == 'A':
                    result += 'T'
                elif char == 'T':
                    result += 'A'
                elif char == 'C':
                    result += 'G'
                elif char == 'G':
                    result += 'C'
        print(result)
        return result
