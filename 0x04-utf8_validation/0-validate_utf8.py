#!/usr/bin/python3
"""
UTF-8 Validation function to check if data is valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given dataset represents a valid UTF-8 encoding.

    Args:
        data (list of int): A list where each integer
        represents a byte (8 bits).

    Returns:
        bool: True if the data is valid UTF-8 encoding, otherwise False.
    """
    expected_continuation_bytes = 0

    for byte in data:
        byte = byte & 0xFF  # Consider only the last 8 bits of the integer

        if expected_continuation_bytes == 0:
            """ Determine the number of bytes in the
            character based on leading
            """
            if (byte >> 5) == 0b110:         # 2-byte character
                expected_continuation_bytes = 1
            elif (byte >> 4) == 0b1110:      # 3-byte character
                expected_continuation_bytes = 2
            elif (byte >> 3) == 0b11110:     # 4-byte character
                expected_continuation_bytes = 3
            elif (byte >> 7):   # Invalid single byte if it starts with '1'
                return False
        else:
            # For continuation bytes, check if the leading bits are '10'
            if (byte >> 6) != 0b10:
                return False
            expected_continuation_bytes -= 1

    return expected_continuation_bytes == 0
