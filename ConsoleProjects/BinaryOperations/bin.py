from bigO import BigO  # !pip install big-O-calculator


def to_bin(num: list):
    """
    Takes a list of integers and returns the binary representation of each number.
    :param num: list of integers
    :return: string representation of binary numbers
    """
    for each in num:
        if each < 0:
            print(f'{each * -1} is {each * -1:b} in binary format')
        else:
            print(f'{each} is {each:b} in binary format')


def reverse_bin(num: list):
    """
    Takes a list of integers and returns the reverse bin representation of each number.

    :param num: A list of integers
    :return: an integer, representing the reversed binary number of the input.
    """
    for each in num:
        if each < 0:
            binary = bin(each)[3:]
            length = len(binary)
            # Shift the bits 32 places minus the length of the binary form. This way LSB becomes MSB.
            try:
                # Try to convert a 32-bit integer
                reversed = (-1 * each) << 32 - length
            except ValueError:
                # In case of overflow use 64-bit format
                reversed = (-1 * each) << 64 - length
            print(f"The {each * -1} is {reversed} if reversed in binary form")
        else:
            binary = bin(each)[2:]
            length = len(binary)
            # Shift the bits 32 places minus the length of the binary form. This way LSB becomes MSB.
            try:
                # Try to convert a 32-bit integer
                reversed = each << 32 - length
            except ValueError:
                # In case of overflow use 64-bit format
                reversed = each << 64 - length
            print(f"The {each} is {reversed} if reversed in binary form")


if __name__ == '__main__':
    # This library is used to find the BigO notation of the functions.
    lib = BigO()
    # Test with big inputs
    lib.test(to_bin, array='small', prtResult=True)
