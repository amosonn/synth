"""
num_to_str_iter
"""
def num_to_str_iter(i):
    """
    Takes a 16bit unsigned number iterator, and yields for each value,
    a tuple of 2bytes representation of the number (shifted by 0x8000 up),
    and the length.
    """
