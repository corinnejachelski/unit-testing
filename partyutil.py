"""Utility functions for the party app."""


def is_mel(name, email):
    """Return True if name and email are related to Mel.

    >>> is_mel('Mel Melitpolski', 'mel@ubermelon.com')
    True
    >>> is_mel('mel', 'personalemail@gmail.com')
    True
    >>> is_mel('M', 'mel@ubermelon.com')
    True
    >>> is_mel('Megan', 'megan@gmail.com')
    False
    """
    name = name.islower()
    email = email.lower()

    return name == 'mel melitpolski' or name == 'mel' or email == 'mel@ubermelon.com'


def most_and_least_common_type(treats):
    """Given list of treats, return most and least common treat types.

    Return most and least common treat types in tuple of format
    (most, least). If there's a tie, the dessert that appears
    first in alphabetical order should win.

    >>> treats = [{"type" : "drink"}]
    >>> most_and_least_common_type(treats)
    ('drink', 'drink')

    >>> treats = [{"type" : "drink"}, {"type" : "dessert"}]
    >>> most_and_least_common_type(treats)
    ('dessert', 'dessert')
    
    >>> treats = [{"type" : "drink"}, {"type" : "dessert"}, 
    ...         {"type" : "dessert"}, {"type" : "appetizer"}]
    >>> most_and_least_common_type(treats)                                        
    ('dessert', 'appetizer')

    >>> treats = []
    >>> most_and_least_common_type(treats)
    (None, None)
    """

    if not treats:
        return (None, None)

    types = {}

    # Count number of each type
    for treat in treats:
        types[treat['type']] = types.get(treat['type'], 0) + 1

    # Get tuples of (treat type, count) in alphabetical order
    types = sorted(types.items())

    # Find the min & max using the count of each tuple (which
    # is stored at index 1)
    most_type, _ = max(types, key=lambda treat_type: treat_type[1])
    least_type, _ = min(types, key=lambda treat_type: treat_type[1])

    return (most_type, least_type)
